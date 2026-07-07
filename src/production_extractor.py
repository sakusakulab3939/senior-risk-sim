import argparse
import csv
import json
import re
import sys
from pathlib import Path

for stream in (sys.stdout, sys.stderr):
    if hasattr(stream, "reconfigure"):
        stream.reconfigure(encoding="utf-8")

SCENE_HEADER_RE = re.compile(r"^## SCENE (\d{3}) \[zone: ([A-Za-z0-9_]+)\]$")
TAG_RE = re.compile(r"^(NARRATION|SPEAKER|IMAGE_PROMPT|SE): (.*)$")


def parse_script(text: str):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("先頭にメタブロック(---)がありません")
    meta, body_start = _parse_meta_block(lines)
    scenes = _parse_scenes(lines[body_start:])
    return meta, scenes


def _parse_meta_block(lines):
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        raise ValueError("メタブロックの終端(---)が見つかりません")

    meta = {}
    current_nested_key = None
    for line in lines[1:end]:
        if not line.strip():
            continue
        if line.startswith("  ") and current_nested_key:
            key, value = _split_kv(line.strip())
            meta[current_nested_key][key] = _coerce(value)
            continue
        key, value = _split_kv(line.strip())
        if value == "":
            meta[key] = {}
            current_nested_key = key
        else:
            meta[key] = _coerce(value)
            current_nested_key = None
    return meta, end + 1


def _split_kv(line):
    key, _, value = line.partition(":")
    return key.strip(), value.strip()


def _coerce(value):
    return int(value) if value.isdigit() else value


def _parse_scenes(lines):
    scenes = []
    current = None
    for line in lines:
        header = SCENE_HEADER_RE.match(line)
        if header:
            if current:
                scenes.append(current)
            current = {
                "scene_id": header.group(1),
                "zone_id": header.group(2),
                "narration": "",
                "speaker": "ナレーター",
                "image_prompt": "",
                "se": "",
            }
            continue
        if current is None:
            continue
        tag = TAG_RE.match(line)
        if not tag:
            continue
        name, value = tag.group(1), tag.group(2)
        if name == "NARRATION":
            current["narration"] = value
        elif name == "SPEAKER":
            current["speaker"] = value
        elif name == "IMAGE_PROMPT":
            current["image_prompt"] = value
        elif name == "SE":
            current["se"] = value
    if current:
        scenes.append(current)
    return scenes


def load_zone_budgets(genre_path: Path, duration_sec: int) -> dict:
    genre = json.loads(genre_path.read_text(encoding="utf-8"))
    chars_per_min = genre["narration_speed"]["chars_per_min"]
    ratio = genre["narration_speed"]["effective_char_ratio"]
    budgets = {}
    for zone in genre["zones"]:
        zone_duration = max(duration_sec * zone["duration_ratio"], zone.get("min_sec", 0))
        max_sec = zone.get("max_sec")
        if max_sec is not None:
            zone_duration = min(zone_duration, max_sec)
        budgets[zone["zone_id"]] = zone_duration / 60 * chars_per_min * ratio
    return budgets


def validate_total_scenes(meta, scenes, warn):
    expected = meta.get("total_scenes")
    actual = len(scenes)
    if expected is not None and expected != actual:
        warn(f"total_scenes不一致: メタブロック={expected} 実際={actual}")


def validate_zone_char_budgets(meta, scenes, genre_path, warn):
    duration_sec = meta.get("duration_sec")
    if duration_sec is None:
        warn("メタブロックにduration_secが無いためゾーン文字数チェックをスキップ")
        return
    if not genre_path.exists():
        warn(f"genres/risk_sim.jsonが見つからないためゾーン文字数チェックをスキップ: {genre_path}")
        return

    budgets = load_zone_budgets(genre_path, duration_sec)
    actual_chars = {}
    for scene in scenes:
        actual_chars[scene["zone_id"]] = actual_chars.get(scene["zone_id"], 0) + len(scene["narration"])

    for zone_id, budget in budgets.items():
        if budget == 0:
            continue
        actual = actual_chars.get(zone_id, 0)
        diff_ratio = (actual - budget) / budget
        if abs(diff_ratio) > 0.15:
            warn(
                f"{zone_id}: NARRATION文字数が予算から{diff_ratio:+.0%}乖離"
                f"（実測{actual}字 / 予算{budget:.0f}字）"
            )


def validate_image_prompts(scenes, warn):
    for scene in scenes:
        if not scene["image_prompt"].strip():
            warn(f"SCENE {scene['scene_id']}: IMAGE_PROMPTが空です")


def validate_metrics_columns(metrics_path: Path, warn):
    if not metrics_path.exists():
        warn(f"metrics.csvが見つかりません: {metrics_path}")
        return
    with metrics_path.open(encoding="utf-8-sig", newline="") as f:
        header = next(csv.reader(f), [])
    for col in ("ending_pattern", "explanation_layout"):
        if col not in header:
            warn(f"metrics.csvに列 '{col}' が見つかりません")


def write_voice_plain_text(scenes, out_dir: Path):
    text = "\n\n".join(scene["narration"] for scene in scenes)
    (out_dir / "voice_plain_text.txt").write_text(text, encoding="utf-8")


def write_voice_assignment_csv(scenes, out_dir: Path):
    with (out_dir / "voice_assignment.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["scene_id", "zone_id", "speaker"])
        for scene in scenes:
            writer.writerow([scene["scene_id"], scene["zone_id"], scene["speaker"]])


def write_image_prompts(scenes, out_dir: Path):
    data = {
        "scenes": [
            {"scene_id": s["scene_id"], "zone_id": s["zone_id"], "image_prompt": s["image_prompt"]}
            for s in scenes
        ]
    }
    (out_dir / "image_prompts_final.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def _keywords(text: str):
    return [p for p in re.split(r"[・、,／/\s]+", text) if p]


def build_metadata_draft(blueprint: dict) -> dict:
    theme = blueprint.get("theme", "")
    focus = blueprint.get("explanation_focus", "")

    title_candidates = [
        f"{theme}で人生が狂った話",
        f"【実録シミュレーション】{theme}の末路",
        f"{focus}を知らずに払った代償——{theme}",
    ]

    plot_summary = blueprint.get("plot_summary", "")
    description = (
        f"{plot_summary}\n\n"
        f"この動画では「{theme}」をテーマに、判断ミスがどのように積み重なっていくかを再現しています。\n"
        f"予防策として「{focus}」についても解説しています。"
    ).strip()

    tags = []
    for text in (theme, focus):
        if text:
            tags.append(text)
            tags.extend(_keywords(text))
    tags = list(dict.fromkeys(tags))

    return {"title_candidates": title_candidates, "description": description, "tags": tags}


def write_metadata_draft(blueprint: dict, out_dir: Path):
    data = build_metadata_draft(blueprint)
    (out_dir / "metadata_draft.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def write_thumbnail_prompts(blueprint: dict, out_dir: Path):
    directions = blueprint.get("thumbnail_direction", [])[:3]
    data = {
        "thumbnail_prompts": [
            {"direction_ja": d, "prompt_draft": d, "needs_refinement": True} for d in directions
        ]
    }
    (out_dir / "thumbnail_prompts.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def main():
    parser = argparse.ArgumentParser(
        description="FINAL_SCRIPT_FULL.mdから制作データ（ナレーション・画像プロンプト・メタデータ叩き台）を抽出する"
    )
    parser.add_argument("script_path", type=Path, help="videos/{video_id}/FINAL_SCRIPT_FULL.md")
    args = parser.parse_args()

    script_path = args.script_path.resolve()
    if not script_path.exists():
        sys.exit(f"[ERROR] ファイルが見つかりません: {script_path}")

    video_dir = script_path.parent
    repo_root = Path(__file__).resolve().parent.parent
    blueprint_path = video_dir / "blueprint.json"
    genre_path = repo_root / "genres" / "risk_sim.json"
    metrics_path = repo_root / "metrics.csv"
    out_dir = video_dir / "output"

    if not blueprint_path.exists():
        sys.exit(f"[ERROR] blueprint.jsonが見つかりません: {blueprint_path}")
    blueprint = json.loads(blueprint_path.read_text(encoding="utf-8"))

    meta, scenes = parse_script(script_path.read_text(encoding="utf-8"))

    warnings = []
    validate_total_scenes(meta, scenes, warnings.append)
    validate_zone_char_budgets(meta, scenes, genre_path, warnings.append)
    validate_image_prompts(scenes, warnings.append)
    validate_metrics_columns(metrics_path, warnings.append)

    out_dir.mkdir(parents=True, exist_ok=True)
    write_voice_plain_text(scenes, out_dir)
    write_voice_assignment_csv(scenes, out_dir)
    write_image_prompts(scenes, out_dir)
    write_metadata_draft(blueprint, out_dir)
    write_thumbnail_prompts(blueprint, out_dir)

    for w in warnings:
        print(f"[WARNING] {w}", file=sys.stderr)
    print(f"抽出完了: {out_dir}")


if __name__ == "__main__":
    main()

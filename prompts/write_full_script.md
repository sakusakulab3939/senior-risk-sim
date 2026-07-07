# 台本全文一括執筆プロンプト（Phase 0-4 / B-2用）

対象モデル：Claude Code / Opus 4.8（新規セッション。過去の企画検討セッションの履歴は引き継がない）

---

## あなたの役割

あなたは risk_sim ジャンル（シニア向け人生リスク・失敗シミュレーション）の
台本を全文一括で執筆するライターです。Part分割・MISSION方式は使いません。
この1回の応答で `FINAL_SCRIPT_FULL.md` の内容を最初から最後まで書き切ってください。

## 読み込むファイル（これ以外を正としない）

- `videos/{video_id}/blueprint.json` — この動画1本の企画データ。今回書く台本の内容そのものを規定する
  （形は `videos/_template/blueprint_template.json` を参照。実際に読むのは `blueprint.json` インスタンス）
- `genres/risk_sim.json` — ジャンル設計（ゾーン構造・尺計算・結末パターン分岐・解説レイアウト定義）

このプロンプト文と上記2ファイル以外の情報（過去のチャット履歴、記憶）には依存しないこと。

## 出力

`FINAL_SCRIPT_FULL.md` の中身のみを出力する。前置き・後書き・確認の相槌などの
余計なテキストを一切含めないこと。

---

## 執筆手順

### 1. duration_sec を決定する

`blueprint.json.duration_mode` に対応する `risk_sim.json.duration_options_sec[duration_mode]`
の `min`〜`max` の範囲内で `duration_sec` を1つ決定する。範囲の中央値を基本とし、
`blueprint.json` の内容量（key_misjudgmentsの複雑さ等）に応じて微調整してよい。
決定した値は後述のメタブロックに記録する。

### 2. 各ゾーンの zone_char_budget を計算する

`risk_sim.json.zones` を `order` 順に処理する。計算式は `risk_sim.json.chars_per_scene_calc`
のものをそのまま使う（下に明示する。数値・ロジックはrisk_sim.json側が正本なので、
本ファイルとrisk_sim.jsonの内容が食い違う場合はrisk_sim.jsonを優先する）：

```
zone_duration_sec = max(duration_sec * zone.duration_ratio, zone.min_sec ?? 0)
zone_duration_sec = min(zone_duration_sec, zone.max_sec ?? Infinity)
zone_char_budget   = zone_duration_sec / 60 * chars_per_min * effective_char_ratio
```

- `chars_per_min` = `risk_sim.json.narration_speed.chars_per_min`（現行417）
- `effective_char_ratio` = `risk_sim.json.narration_speed.effective_char_ratio`（現行0.85）

計算した `zone_char_budget` は、そのゾーン内の全シーンの `NARRATION:` 本文の
合計文字数の目安とする（±10%程度の許容誤差は可）。

### 3. シーン分割ルール（scene_split_rule）

`zone_char_budget` をそのゾーンの想定シーン数で割る。シーン数の目安：

| zone_id | シーン数の目安 |
|---|---|
| hook_ending_glimpse | 1 |
| daily_life | 2 |
| misjudgment_accumulation | `blueprint.json.key_misjudgments` の項目数（3つ）と1:1対応させる。budgetに余裕がある場合のみ、いずれか1項目を2シーンに分割してよい（対応関係が視覚的にわかる範囲に留める） |
| crisis_regret | 2（前半：分岐点への接近／後半：ending_patternに応じた帰結。branch_specsの内容次第でシーン配分を微調整してよい） |
| explanation | `blueprint.json.explanation_layout` による（下記セクション参照） |
| checklist | 1 |

端数は切り捨てず、余りは `misjudgment_accumulation` ゾーンの最終シーンに加算する
（最も内容の伸縮に耐えるゾーンのため）。

### 4. crisis_regret ゾーン：ending_pattern による分岐（branch_specs）

`blueprint.json.ending_pattern` の値に応じて、`risk_sim.json.zones[crisis_regret].branch_specs`
の該当する記述を必ず反映すること。参考として現行の定義を下に示すが、
実際に適用する際は必ず `risk_sim.json` 側の最新の記述を確認すること：

- `complete_failure`：回避できた分岐点を1つ明示的に通り過ぎさせてから帰結を描く。救済・軽減は入れない
- `near_miss`：帰結直前に介入または踏みとどまりのトリガーを1つ明確に置く。何が効いたかを解説ゾーンに引き渡せる形にする
- `small_lesson`：実害は限定した範囲に収め、主人公が誤りに気づく瞬間を明確なビートとして描く
- `recovery`：支えの主体（家族／制度／地域のいずれか1つに絞る）を明示し、カタルシスの瞬間を配置する

`blueprint.json.ending_pattern` が `risk_sim.json.ending_patterns.available` 側で
`available: false`（現状 `recovery`）になっている場合は、`blueprint.json` の指定を
疑い、執筆を止めて確認を求めること（B-1の判断ミスの可能性があるため）。

### 5. explanation ゾーン：explanation_layout による配置切り替え

`blueprint.json.explanation_layout` の値に応じて、解説要素（`blueprint.json.explanation_focus`
の内容）の配置方法を変える。3パターンとも `## SCENE ... [zone: explanation]` の
シーンブロック自体は必ず出力すること（後述の出力フォーマット契約を維持するため）。

- **`trailing_block`**（デフォルト）：解説内容はすべて `crisis_regret` の後、
  `explanation` ゾーンのシーン群にまとめて配置する。zone_char_budget通りの尺で書く
- **`distributed`**：解説の要素（制度知識・予防策）を `daily_life` および
  `misjudgment_accumulation` ゾーンのシーンのナレーション内に、伏線・気づきの
  ひと言として自然に分散させる。その上で `explanation` ゾーンは要点の再整理のみに
  圧縮する（zone_char_budgetの6〜7割程度を目安にする）
- **`compressed`**：解説そのものの尺を短縮する。`explanation` ゾーンの
  zone_char_budgetは通常計算値の6割程度を目安に圧縮し、checklistゾーンへの
  橋渡しを速める。浮いた尺は他ゾーンに再配分せず、単純に総尺を短縮してよい

> **注記**：上記の6〜7割・6割という数値はDRAFT値・根拠なし。初期10本の実測後、
> metrics.csvの維持率データを見て見直す。

### 6. 各ゾーン共通の制約

各ゾーンを執筆する際は、`risk_sim.json.zones` の該当オブジェクトの
`purpose` / `pacing` / `requires`（存在する場合）/ `avoid`（存在する場合）を必ず読み、
それらを執筆時の制約としてそのまま適用すること。要約・意訳をせず、
`requires` に挙げられた項目は本文中に明示的な描写として含めること。

特に `misjudgment_accumulation` ゾーンでは、独立した判断ミスを3つ以上、
`blueprint.json.key_misjudgments` の各項目と対応させて時系列で積み重ねて描くこと。
どのシーンがどの `key_misjudgments` 項目に対応するかが読んでわかる構成にする。

---

## 出力フォーマット契約（厳守・Phase 0-5のPython抽出処理がこれをパースする）

以下のルールから逸脱しないこと。逸脱するとPython側のパースが失敗する。

### ファイル冒頭のメタブロック

ファイルの最初に、YAML形式のメタブロックを `---` で囲んで出力する：

```
---
genre: risk_sim
theme: {blueprint.jsonのtheme}
ending_pattern: {blueprint.jsonのending_pattern}
explanation_layout: {blueprint.jsonのexplanation_layout}
duration_mode: {blueprint.jsonのduration_mode}
duration_sec: {手順1で決定した値}
total_scenes: {シーン総数}
zone_scene_counts:
  hook_ending_glimpse: {シーン数}
  daily_life: {シーン数}
  misjudgment_accumulation: {シーン数}
  crisis_regret: {シーン数}
  explanation: {シーン数}
  checklist: {シーン数}
---
```

### シーンブロック

メタブロックの後、シーンごとに以下の見出しで区切る：

```
## SCENE {3桁連番} [zone: {zone_id}]
```

- 連番はファイル全体を通した通し番号（ゾーンごとにリセットしない）。`001`から開始し3桁ゼロ埋め
- `zone_id` は `risk_sim.json.zones` の `zone_id` の値をそのまま使う

シーン見出しの直後に、行頭タグで要素を分けて書く。タグの出現順は固定：

```
NARRATION: {ナレーション本文}
SPEAKER: {話者名。ナレーターのみの場合はこの行自体を省略}
IMAGE_PROMPT: {画像生成プロンプト。英語で1行}
SE: {効果音の指定。無い場合はこの行自体を省略}
```

- 各タグの値は同じ物理行の中に収める（改行を含めない）。1タグ＝1行。
- `NARRATION:` は必須。この行の `NARRATION: ` 以降の文字数（前置き除く）を
  `zone_char_budget` との照合対象とする
- `IMAGE_PROMPT:` は必須。`SPEAKER:` と `SE:` は該当が無ければ行ごと省略可
- シーンとシーンの間は空行1行のみで区切る。空行を2行以上続けない

### 出力例（形式確認用。内容はダミー）

```
---
genre: risk_sim
theme: 退職金の運用詐欺
ending_pattern: complete_failure
explanation_layout: trailing_block
duration_mode: fast_validation
duration_sec: 810
total_scenes: 11
zone_scene_counts:
  hook_ending_glimpse: 1
  daily_life: 2
  misjudgment_accumulation: 3
  crisis_regret: 2
  explanation: 2
  checklist: 1
---

## SCENE 001 [zone: hook_ending_glimpse]
NARRATION: （本文）
IMAGE_PROMPT: (english prompt)

## SCENE 002 [zone: daily_life]
NARRATION: （本文）
SPEAKER: ナレーター
IMAGE_PROMPT: (english prompt)
SE: 生活音
```

---

## 執筆前の自己チェック（出力前に必ず確認する）

- `total_scenes` とメタブロックの `zone_scene_counts` の合計が一致しているか
- 各ゾーンの `NARRATION:` 合計文字数が、そのゾーンの `zone_char_budget` から
  大きく外れていないか（目安±10%）
- `ending_pattern` に対応する `branch_specs` が `crisis_regret` ゾーンに反映されているか
- `explanation_layout` に応じた配置切り替えが行われているか
- `key_misjudgments` の3項目すべてが `misjudgment_accumulation` ゾーンに対応しているか
- シーン見出し・行頭タグの表記が上記フォーマット契約と1文字も違わないか

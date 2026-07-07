# YouTube動画制作ワークフロー v6 — 全工程とモデル指定

チャンネル：シニア向け人生リスク系（失敗シミュレーション＋解説構成）
基盤：台本自動生成パイプライン v5.1 を軽量化して移行

## 使用ツールと役割（固定ルール）

| ツール | 役割 | コスト |
|---|---|---|
| Claude Code / Opus 4.8 | 台本執筆（品質の核。ここだけ投資） | Claude枠・高消費 |
| Claude Code / Fable 5 | 品質批評の監査のみ。枠に余裕がある時だけ | Claude枠・最高消費 |
| Claude Code / Sonnet 4.6 | 企画案生成、日常作業のデフォルト | Claude枠・中消費 |
| Haiku 4.5 | 定型変換（メタデータ整形など） | Claude枠・低消費 |
| ChatGPT (GPT Plus) | ブレスト、リサーチ深掘り、コピー案、画像プロンプト改良 | Claude枠を消費しない |
| Codex (GPT Plus) | Pythonスクリプトの保守・改修すべて | Claude枠を消費しない |
| Antigravity (Gemini) | 月次バッチ収集専用 | 無料枠 |
| Python（LLMなし） | バリデーション、制作データ抽出 | 無料 |

**セッション運用ルール**
- 同一セッション内で /model を切り替えない（履歴再読み込みで高コスト）
- 工程の区切りでセッションを終了し、受け渡しはファイルで行う（blueprint.json、FINAL_SCRIPT_FULL.md 等を正本とする）
- Claude Code に渡すのは前工程の成果物ファイルのみ。過去の会話履歴に依存させない

---

## Phase 0：移行作業（1回だけ）

| # | 工程 | 成果物 | 担当 |
|---|---|---|---|
| 0-1 | リポジトリをAntigravity依存から切り離しローカル化。Git初期化、現状に v5.1 タグ | Gitリポジトリ | 手作業＋Codex |
| 0-2 | CLAUDE.md 作成（モデル指定、セッション分割ルール、ファイル正本方式、.py編集禁止等の運用ルール） | CLAUDE.md | ChatGPTで下書き→確定 |
| 0-3 | risk_sim ジャンルJSON設計（ゾーン構造：結末フック→日常→判断ミス累積→危機・後悔→解説→チェックリスト／結末3パターンのパラメータ化／chars_per_scene） | genres/risk_sim.json | 叩き台：ChatGPT → 最終レビュー：Claude Opus 1回 |
| 0-4 | MISSION方式・Part分割の廃止。全文一括執筆用プロンプトへ改修 | 執筆プロンプト1本 | Codex |
| 0-5 | 10_production_extractor 拡張：タイトル候補3案・概要欄・タグ・サムネ用プロンプト2〜3案を出力に追加 | 改修済み .py | Codex |
| 0-6 | DaVinci 解説パート用テロップテンプレ作成（分岐点整理・チェックリスト画面） | .drt テンプレ | 手作業（LLM不要） |
| 0-7 | docs/decisions/（ADR）と metrics.csv の初期化。ADRテンプレ：背景／決定／捨てた選択肢と理由／結果 | フォルダ＋CSV | Codex |

移行中の各判断は ADR に1件1ファイルで記録（商材の素材になるため必須）。

---

## Phase A：月次の資産更新（動画制作から切り離す）

| # | 工程 | 成果物 | 担当 |
|---|---|---|---|
| A-1 | 競合データ収集バッチ実行（YouTube API → candidate_videos.csv → ranked_themes.csv） | テーマストック更新 | Antigravity（Gemini） |
| A-2 | タイトルパターン・構成傾向の分析更新 | title_patterns.md 更新 | Antigravity または ChatGPT |
| A-3 | 収益化動向ウォッチ（競合の停止・復活、新規参入チャンネルの構成確認） | メモ（ADR随時） | 手動＋ChatGPT |

---

## Phase B：動画1本あたりの工程

### 制作準備（Claude Code）

| # | 工程 | 成果物 | 担当 | 人間の判断 |
|---|---|---|---|---|
| B-1 | 企画3案生成：テーマ＋プロット＋結末パターン（完全失敗/寸前回避/小失敗学習）＋サムネ方向をセットで提示 | blueprint.json | Claude Code / **Sonnet 4.6**（セッション①） | ★ 1案を選択 |
| B-2 | 台本執筆：blueprint.json のみ読み込み、全文一括執筆 | FINAL_SCRIPT_FULL.md | Claude Code / **Opus 4.8**（新セッション②） | — |
| B-3 | 構造バリデーション（シーン番号・文字数・推定尺） | 検査ログ | Python（LLM不要） | — |
| B-4 | 6軸ルーブリック品質批評＋修正指示 | quality_report.md | **Fable 5**（余裕時）／**Opus 4.8**（通常）（セッション③） | ★ 台本を承認 |
| B-5 | 制作データ抽出：voice_plain_text.txt、voice_assignment.csv、image_prompts_final.json、メタデータ案、サムネプロンプト案 | output/ 一式 | Python（LLM不要） | — |
| B-6 | メタデータ磨き（タイトル3案・概要欄・タグの整形） | 確定メタデータ | **Haiku** または ChatGPT | — |

### 制作実務（クライアント案件と同一フロー）

| # | 工程 | 担当 |
|---|---|---|
| B-7 | 音声生成（voice_plain_text.txt → ElevenLabs） | 手作業 |
| B-8 | 画像生成（image_prompts → nanobanana）。プロンプト不調時の改良は ChatGPT | 手作業 |
| B-9 | 字幕（Vrew） | 手作業 |
| B-10 | 編集（DaVinci Resolve）。解説パートは 0-6 のテンプレ流用。Fairlight は既定値（ナレーション +7〜+9 LU、SE +3〜+5、BGM −3〜0、Bus1 +9 LU） | 手作業 |
| B-11 | サムネ2〜3案生成→選定。コピー案は ChatGPT、画像は nanobanana | 手作業 ★ 1案を選択 |
| B-12 | 公開。metrics.csv に所要時間・使用モデル・詰まった箇所を1行記録 | 手作業（記録は Claude Code に一言でも可） |

**人間の判断は3回だけ**：B-1（企画選択）、B-4（台本承認）、B-11（サムネ選択）。

---

## クレジット消費の目安（1本あたりの Claude 枠）

- 消費するのは B-1（Sonnet・軽）、B-2（Opus・重）、B-4（Opus or Fable・中）、B-6（Haiku・微）の4箇所のみ
- 枠が逼迫した週の縮退運転：B-2 を Sonnet 4.6 に落とし、B-4 の批評を Opus で厚めに行う（執筆を落として監査で拾う）
- Fable は B-4 限定。他工程では使わない

## 検証フェーズの初期方針（最初の10本）

- 尺は検証速度優先なら 12〜15 分、通常 20〜24 分（開始前に決定）
- テーマ約5種 × フック2型で配分し、CTR・冒頭30秒維持率・平均視聴維持率（特に解説パート突入時の離脱）で柱を絞る
- 解説パートの離脱率が高い場合：後置きの塊 → 物語内分散 or 圧縮をテスト

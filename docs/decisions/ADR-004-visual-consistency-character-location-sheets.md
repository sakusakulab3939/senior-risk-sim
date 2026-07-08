# ADR-004: キャラクター/ロケーションシート仕様とビジュアル一貫性の統合

## 背景
旧パイプライン（senior_story_workflow）で実際に使われていた最終版の
キャラクターシート（全身三面図＋表情4種）・ロケーションシート（2x2グリッド＋広角）仕様、
確定スタイルタグ、テキスト除外ガードが発見された。これをrisk_simの現行パイプラインへ
移植するにあたり、そのまま流用せず、以下2つの前提差分を踏まえて再設計する必要があった。

- risk_simは基本的に1話完結（年齢を跨ぐキャラバリアント切替は不要。ADR-003で見送り済み）。
- 旧仕様の内部に矛盾（character sheet 末尾の `labeled '[名前]'` と、テキスト除外ガードの
  `no letters, no words` が衝突）があり、また汎用の表情セット（happy/surprised/crying/pained）が
  risk_simの感情アーク（自信→不安→恐怖→絶望）とズレていた。

前提の決定的論点だった「画像生成ツールが参照画像条件付けに対応しているか」は、
**nanobanana（Nano Banana Pro / Gemini 3 Pro Image、最大5人まで一貫性維持・参照画像条件付け可）**
の採用により「対応ツール」として確定した。これによりシート方式が実効性を持つ前提が成立した。

## 決定
ビジュアル一貫性の仕様を `genres/risk_sim.json` の `visual_style` ブロックとして確定し
（本決定はCLAUDE.md『risk_sim.json確定前のOpus 4.8で1回レビュー』枠として同一セッションで実施）、
以下を反映した。適用タイミングを「即時（1本目含む）」と「次回作（2本目以降）」に分離する。

### 即時反映（1本目 001_sns_investment_scam を含む）
- **確定スタイルタグ（変更禁止）**：`manga anime style, cel shading, crisp clean linework, controlled color palette`。
  旧タグの `high quality illustration`（情報量の薄いフィラー語）を除去し、線の明確化と
  シニア視聴者の可読性のため `cel shading, crisp clean linework` を採用。
- **彩度・トーン（項目J）**：ヴィヴィッドな高彩度はこのジャンル（深刻な失敗談）にトーン不一致のため不採用。
  `controlled color palette` をグローバル固定とし、彩度・明度・色温度は `zone_color_grading` で
  ゾーンの感情に合わせて振る（DRAFT・根拠なし、初期10本の実測後に見直す）。
- **テキスト除外ガードのスコープ限定（項目C）**：本編フレーム（SCENE/CUT）にのみ付与。
  DaVinci解説パートでテロップを別途載せるため画像内文字は禁止。シートには付与しない。
- **シートのラベル方針（項目B）**：画像内に文字を焼き込まない（文字化け＋ガードと矛盾）。
  ラベルはファイル名で管理（例 `P1_fujita_kenichi.png`）。旧仕様の `labeled '[名前]'` は廃止。
- **1本目への軽量トレイトロック（項目E）**：`FINAL_SCRIPT_FULL.md` の全11 IMAGE_PROMPT を、
  主人公・妻の確定描写文字列＋確定スタイルタグ＋ゾーン別グレーディング＋テキストガードで統一。
  ナレーション本文（B-4承認対象）は一切変更していない。

### 次回作（2本目以降）から
- **blueprint.json スキーマ拡張（項目F）**：`visual_cast`（char_id・name・role・appearance・
  `locked_prompt_fragment`）と `locations`（loc_id・name・`locked_prompt_fragment`）を追加する。
- **表情セットのrisk_sim化（項目G）**：`confident, uneasy, shocked, despairing`（DRAFT、Opus確定）。
- **B-1.5 ビジュアル基盤生成**：シート生成は独立工程にせずB-1（企画確定）に畳み込む
  （人間判断3回=B-1/B-4/B-11の枠を増やさない）。人間がシートを目視確認し、
  実際に良い結果が出た表現で `locked_prompt_fragment` を凍結する（＝ロック文字列を検証済みにする）。
- **production_extractor 機械連結（項目I／案B）**：CUTごとに参照（char_id/loc_id）と演技だけを台本に書き、
  extractorが `[base_style_tag]+[location fragment]+[character fragment]+[演技]+[zone grading]+[text guard]`
  を機械連結する。ロック文字列をLLMの手に触れさせずドリフトを構造的にゼロにする。

### 項目K（三面図の背面図の扱い）：保留 → 採用
背面図はシート＝人間の目視確認用の1枚絵には残す。生成時は各パネル（front/side/back/表情）を
個別の参照画像としてnanobananaに渡すため、背面図も無駄にならない。
条件：パネル切り出しが参照画質として使えるよう、シートは高解像度で生成する（DRAFT: 2K以上目安）。

## 捨てた選択肢と理由
- **旧仕様のそのまま移植**：内部矛盾（ラベルvsガード）とジャンル不適合（汎用表情セット、
  高彩度前提）を抱えるため不採用。
- **上位モデルにFableを充てる**：ユーザー質問はFableを名指ししたが、CLAUDE.mdのモデル表では
  Fableは B-4（台本品質批評）専用レーンで、ジャンルJSON設計の最終レビューは Opus 4.8（1回だけ）と
  規定されている。よって本ビジュアル設計の確定は Opus が担当（本セッションで実施）。
- **ロック文字列をblueprintの構造化フィールドから毎回再合成**：語順・言い回しがドリフトし
  トレイトロックにならないため不採用。確定した1本の文字列を正本とし使い回す。
- **画像内にラベル文字を焼き込む**：拡散系モデルで文字化けし、テキスト除外ガードとも矛盾するため
  ファイル名ラベルへ変更。
- **B-1.5を独立した人間判断工程として新設**：CLAUDE.mdの「人間判断3回のみ」と正本表がB-1中心に
  組まれていることに抵触するため、B-1へ畳み込む。
- **画像プロンプトの美的作り込みをClaude枠で実施**：CLAUDE.mdモデル表で「画像プロンプト改良は
  ChatGPT（Claude枠を使わない）」と規定。構造・スキーマ・Python連結はSonnet、ロック文字列確定は人間、
  プロンプトの発散的作り込みはChatGPTに割り当てる。

## 結果
- `genres/risk_sim.json` を v0.3 に更新し `visual_style` ブロックを追加。
- `videos/001_sns_investment_scam/FINAL_SCRIPT_FULL.md` の全IMAGE_PROMPTを統一（軽量トレイトロック）。
- 2本目以降の統合（F/G/H/I）は本ADRを設計正本として別セッションで実装する。
- 未確定（後日追記）：nanobananaでの初号生成テストによる base_style_tag / zone_color_grading /
  シート解像度（2K目安）のDRAFT解除。初期10本の維持率実測による zone_color_grading の見直し。
- 1本目（001_sns_investment_scam）のカット密度：全11シーンでcut_pacing警告
  （1カットあたり33〜103秒）が出ているが、これは1本目の画像枚数増加を
  スコープ外とした既存決定（SCENE 001のみカット分割、他はKen Burns等の
  編集で吸収）によるものであり、仕様不備ではない。SCENE 002〜011は
  1画像/シーンのままDaVinci編集（Ken Burns効果等）で通す。
- **参照画像併用によるシーン生成の検証結果**：P1キャラクターシートを実際に参照画像として
  nanobananaにアップロードした状態でSCENE 001の一部CUTを試験生成し、カーディガン・眼鏡・
  髪型等の一貫性が保たれることを確認した。Opusが前提としていた「参照画像条件付け対応ツール
  ならシートが一貫性エンジンとして機能する」という仮説が実証された。これにより
  P1〜P2/LOC01〜LOC02のシート方式は本番運用可と判断する。
  検証中、和室背景の掛け軸に読めない筆文字が描かれる事例があったが、これは装飾書道として
  許容範囲と判断した（読める設定のラベル・見出し・UI要素が壊れて文字化けする場合とは区別する。
  前者は許容、後者はtext_exclusion_guardの対象として引き続き注意する）。

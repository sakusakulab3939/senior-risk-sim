# サムネイル生成プロンプト（001_sns_investment_scam）

`blueprint.json` の `thumbnail_direction`（3案）を、実際の2段階生成ワークフロー
（段階1：nanobananaで文字なしの画像を生成 → 段階2：GPT Image 2.0でタイトルコピーを合成）
向けのプロンプトに展開したもの。

タイトルコピーは `metadata_final.json` の `confirmed_title`（案2のみ）および
`output/metadata_draft.json` の `title_candidates`（案1・案3）から、各方向性に
最も合うものを1つずつ、3案とも別の候補を割り当てている。

> **注記**：案2は `metadata_final.json` の確定タイトルに更新済み。案1・案3は
> 引き続きmetadata_draft.jsonの候補から参照（B-6後の見直しは案2のみ実施）。

## サムネ生成時の参照画像について

**重要**：nanobanana で段階1プロンプトを実行する際は、必ず以下のキャラクターシート
を参照画像として添付すること。プロンプト本文の `locked_prompt_fragment` はテキスト側の
保険であり、視覚的なトレイトロック（髪型・眼鏡・衣装の一貫性）を確保するには、
参照画像添付が本体である。

参照画像：`videos/001_sns_investment_scam/visual_sheets/P1_fujita_kenichi.png`

---

## 案1：「元経営者だから大丈夫」という慢心を煽るコピー＋青ざめた表情

### 段階1（nanobanana／文字なし）

**参照画像**：P1_fujita_kenichi.png を必ず参照画像として添付すること（トレイトロックの一貫性を保つため）

a Japanese man in his early 60s, short greying receding hair, thin-framed glasses, beige cardigan over a pale collared shirt, average build, an extreme close-up on his pale shocked face frozen in dread, wide fearful eyes contrasting with his confident business-owner bearing, a warm traditional Japanese living room, tatami mat flooring, wooden sliding shoji doors, low wooden table, warm-toned lighting, family photos and small plants on a shelf, softly blurred background, cold desaturated dramatic lighting, 16:9 landscape thumbnail composition, subject large and prominent in frame, dramatic close-up framing optimized for small preview size, manga anime style, cel shading, crisp clean linework, controlled color palette, absolutely no text, no letters, no words, no speech bubbles, no sound effects, no captions, no watermarks, no signatures, no UI elements in the image

### 段階2（GPT Image 2.0／文字入れ）—対話的運用

**タイトルコピー**：「金融庁登録業者の確認方法、「自分は騙されない」という過信バイアスへの警鐘を知らずに払った代償——SNS型投資詐欺・退職金一括投資」（from metadata_draft.json title_candidates）

段階1で生成された画像に対し、以下の方針でGPT Image 2.0に文字入れを指示する。初回は生成結果を見てから対話的に修正を繰り返す：

- **フック語句**：「自分は騙されない」という過信バイアス を最大サイズで最も目立つ位置に配置（顔・表情と重ならないよう注意）
- **補足情報**：残りのテキストは小さめで、画面下部または脇に添える（全文記載は不要、「〜の警鐘」など短縮可）
- **配置調整**：背景・被写体の表情が見えることを優先。生成された画像を見て、実際に文字が入る余地がある場所を選ぶ
- **視認性**：白または黄色文字＋濃い黒枠取りまたはドロップシャドウで、背景に関わらず視認性を確保する
- **修正フロー**：初回生成後、「ここの配置を調整してほしい」など具体的な指示で対話的に修正。背景・被写体の構図は変えず、文字配置のみ調整する

---

## 案2：スマホの残高画面（伸び続ける数字）の下に差す暗い影——3パターン構成

案2は、metadata_final.json の confirmed_title 「元経営者だから大丈夫」——60代の老後資金が狙われるSNS投資詐欺の落とし穴 をベースに、
段階1で3つの異なる構図・演出パターンを用意し、段階2（文字入れ）は全パターン共通で運用する。

### パターン2-v2-1：スマホの残高画面＋暗い影（対比構図）

#### 段階1（nanobanana／文字なし）

**参照画像**：P1_fujita_kenichi.png を必ず参照画像として添付すること（トレイトロックの一貫性を保つため）

a Japanese man in his early 60s, short greying receding hair, thin-framed glasses, beige cardigan over a pale collared shirt, average build, his hand holding a smartphone glowing with a rising balance graph with no legible content, a dark ominous shadow creeping up from beneath the phone across his face, a warm traditional Japanese living room, tatami mat flooring, wooden sliding shoji doors, low wooden table, warm-toned lighting, family photos and small plants on a shelf, softly blurred background, cold heavily desaturated low-key dramatic lighting, 16:9 landscape thumbnail composition, subject large and prominent in frame, dramatic close-up framing optimized for small preview size, manga anime style, cel shading, crisp clean linework, controlled color palette, absolutely no text, no letters, no words, no speech bubbles, no sound effects, no captions, no watermarks, no signatures, no UI elements in the image

#### 段階2（GPT Image 2.0／文字入れ）—対話的運用

**タイトルコピー**：「元経営者だから大丈夫」——60代の老後資金が狙われるSNS投資詐欺の落とし穴（from metadata_final.json confirmed_title）

段階1で生成された画像に対し、以下の方針でGPT Image 2.0に文字入れを指示する。初回は生成結果を見てから対話的に修正を繰り返す：

- **フック語句**：「元経営者だから大丈夫」 を最大サイズで最も目立つ位置に配置（顔・スマートフォン画面と重ならないよう注意）
- **補足情報**：「60代の老後資金が狙われる」または「SNS投資詐欺の罠」を小さめで、フック語句の下または脇に添える（省略可）
- **配置調整**：背景の質感、被写体の表情、スマートフォン画面など見せ場になる要素が見えることを優先。生成された画像を見て実際に文字が入る余地がある場所を選ぶ
- **視認性**：白または黄色文字＋濃い黒枠取りまたはドロップシャドウで、背景に関わらず視認性を確保する
- **修正フロー**：初回生成後、「ここの配置を調整してほしい」など具体的な指示で対話的に修正。背景・被写体の構図は変えず、文字配置のみ調整する

---

### パターン2-v2-2：ビフォーアフター型（左右対比）

#### 段階1（nanobanana／文字なし）

**参照画像**：P1_fujita_kenichi.png を必ず参照画像として添付すること（トレイトロックの一貫性を保つため）

split-screen composition with dramatic left-right contrast: 

LEFT SIDE (self-assured before): a Japanese man in his early 60s, short greying receding hair, thin-framed glasses, beige cardigan over a pale collared shirt, average build, viewed from a slightly upward angle emphasizing strength and confidence, with a proud, smug, self-assured expression and bright direct gaze, bathed in warm golden-orange lighting, standing in a bright, prosperous-looking warm traditional Japanese living room with tatami mat flooring, wooden sliding shoji doors, low wooden table, warm-toned mood lighting, family photos on shelf, and background details including framed company founder certificates, a formal letter envelope (retirement lump sum notification), and a piggy bank or safe, softly blurred warm background;

RIGHT SIDE (devastated after): the same man viewed from a slightly downward camera angle emphasizing weakness and defeat, with a pale, ashen, shell-shocked, devastated expression, eyes hollow and wide with dread and realization of loss, bathed in cold blue-cyan harsh lighting, in the same room now rendered in cold desaturated tones, ominous deep shadows creeping across his face and body, with background elements now darkened and sinister including the glow of a smartphone screen casting eerie light on his features, and the room itself appearing claustrophobic and trap-like, softly blurred cold background;

both sides clearly delineated by a sharp vertical dividing line or dramatic lighting gradient transition at center, emphasizing the psychological rupture between before and after, 16:9 landscape thumbnail composition, subjects large and prominent in frame, dramatic close-up framing optimized for small preview size, manga anime style, cel shading, crisp clean linework with exaggerated emotional contrast, absolutely no text, no letters, no words, no speech bubbles, no sound effects, no captions, no watermarks, no signatures, no UI elements in the image

#### 段階2（GPT Image 2.0／文字入れ）—対話的運用

**タイトルコピー**：「元経営者だから大丈夫」——60代の老後資金が狙われるSNS投資詐欺の落とし穴（from metadata_final.json confirmed_title）

段階1で生成された左右対比画像に対し、以下の方針でGPT Image 2.0に文字入れを指示する。初回は生成結果を見てから対話的に修正を繰り返す：

- **フック語句**：「元経営者だから大丈夫」 を最大サイズで配置。左右の顔・表情が見える位置（中央または上部）に配置することで、ビフォーアフターの対比構図を活かす
- **補足情報**：「60代の老後資金が狙われる」または「SNS投資詐欺の罠」を小さめで添える（省略可）
- **配置調整**：左右の表情（自信vs絶望）が見えることを最優先。生成された画像を見て、実際に文字が入る余地がある場所を選ぶ
- **視認性**：白または黄色文字＋濃い黒枠取りまたはドロップシャドウで視認性を確保する
- **修正フロー**：初回生成後、「ここの配置を調整してほしい」など具体的な指示で対話的に修正。背景・被写体の構図は変えず、文字配置のみ調整する

---

### パターン2-v2-3：視線誘導型（手のクローズアップ）

#### 段階1（nanobanana／文字なし）

**参照画像**：P1_fujita_kenichi.png を必ず参照画像として添付すること（トレイトロックの一貫性を保つため）

close-up focus on a Japanese man's hand in his early 60s holding a smartphone, the phone screen glowing brightly with a rising balance graph with no legible content, the smartphone dominating the lower-middle portion of the frame, soft warm lighting on the hand and device, while in the softly blurred background above and behind the phone, the same man's face is visible but out of focus, showing an anxious, worried, uncertain expression with furrowed brow and pursed lips contrasting with the bright promise of the glowing screen, a warm traditional Japanese living room setting visible but unfocused, cold desaturated dramatic lighting in the background, 16:9 landscape thumbnail composition, layered depth from sharp phone in foreground to soft face in background, framing optimized for small preview size, manga anime style, cel shading, crisp clean linework, controlled color palette, absolutely no text, no letters, no words, no speech bubbles, no sound effects, no captions, no watermarks, no signatures, no UI elements in the image

#### 段階2（GPT Image 2.0／文字入れ）—対話的運用

**タイトルコピー**：「元経営者だから大丈夫」——60代の老後資金が狙われるSNS投資詐欺の落とし穴（from metadata_final.json confirmed_title）

段階1で生成された手のクローズアップ画像に対し、以下の方針でGPT Image 2.0に文字入れを指示する。初回は生成結果を見てから対話的に修正を繰り返す：

- **フック語句**：「元経営者だから大丈夫」 を最大サイズで配置。スマートフォン画面と背景の不安げな表情が見える位置（上部または左上）を選ぶ
- **補足情報**：「60代の老後資金が狙われる」または「SNS投資詐欺の罠」を小さめで添える（省略可）
- **配置調整**：スマートフォン画面の光と背景の不安げな顔の両方が見えることを優先。生成された画像を見て実際に文字が入る余地がある場所を選ぶ
- **視認性**：白または黄色文字＋濃い黒枠取りまたはドロップシャドウで視認性を確保する
- **修正フロー**：初回生成後、「ここの配置を調整してほしい」など具体的な指示で対話的に修正。背景・被写体の構図は変えず、文字配置のみ調整する

---

## 案3：なりすまし広告のスクショ風ビジュアル＋「その広告、あなたも見た」

### 段階1（nanobanana／文字なし）

**参照画像**：P1_fujita_kenichi.png を必ず参照画像として添付すること（トレイトロックの一貫性を保つため）

a mock investment advertisement screenshot-style graphic featuring a smiling celebrity investor portrait and a fake verified checkmark badge, with rows of plain placeholder bars instead of readable text, a Japanese man in his early 60s, short greying receding hair, thin-framed glasses, beige cardigan over a pale collared shirt, average build, softly out of focus in the background holding a smartphone displaying the advertisement, a warm traditional Japanese living room, tatami mat flooring, wooden sliding shoji doors, low wooden table, warm-toned lighting, family photos and small plants on a shelf, softly blurred background, slightly cool dramatic lighting, 16:9 landscape thumbnail composition, subject large and prominent in frame, dramatic close-up framing optimized for small preview size, manga anime style, cel shading, crisp clean linework, controlled color palette, absolutely no text, no letters, no words, no speech bubbles, no sound effects, no captions, no watermarks, no signatures, no UI elements in the image

### 段階2（GPT Image 2.0／文字入れ）—対話的運用

**タイトルコピー**：「【実録シミュレーション】SNS型投資詐欺・退職金一括投資の末路」（from metadata_draft.json title_candidates）

段階1で生成された広告グラフィック画像に対し、以下の方針でGPT Image 2.0に文字入れを指示する。初回は生成結果を見てから対話的に修正を繰り返す：

- **ラベル表示**：【実録シミュレーション】 を小さめのバッジ風で配置（左上が目安だが、実画像を見て最適位置を選ぶ）
- **フック語句**：SNS型投資詐欺・退職金一括投資の末路 を最大サイズで配置。広告グラフィックと人物の両方が見える位置を選ぶ
- **配置調整**：なりすまし広告のビジュアルと背景の人物が見えることを優先。生成された画像を見て実際に文字が入る余地がある場所を選ぶ
- **視認性**：白または黄色文字＋濃い黒枠取りまたはドロップシャドウで視認性を確保する
- **修正フロー**：初回生成後、「ここの配置を調整してほしい」など具体的な指示で対話的に修正。背景・被写体の構図は変えず、文字配置のみ調整する

---

## 自己チェック

### 段階1：意図せず文字を入れる余地のある記述が無いか
- 案1：フェイシャルクローズアップと部屋の描写のみ。看板・画面表示・ラベル等の要素なし
- 案2：スマホ画面に言及しているが `"with no legible content"` を明示し、可読文字が
  乗らないよう限定している
- 案3：広告スクリーンショット風という最もリスクが高い方向性のため、
  `"rows of plain placeholder bars instead of readable text"` を明示し、
  実際の広告文言・アカウント名等が生成されないよう縛りを入れている
- 3案ともプロンプト末尾に `text_exclusion_guard`（`absolutely no text, no letters, no words,
  no speech bubbles, no sound effects, no captions, no watermarks, no signatures,
  no UI elements in the image`）を含めている

### 段階2：タイトルコピーがmetadata_final.jsonと矛盾しないか
- B-6確定後、案2のタイトルコピーは `metadata_final.json` の `confirmed_title`
  「元経営者だから大丈夫」——60代の老後資金が狙われるSNS投資詐欺の落とし穴に更新済み
- サムネ瞬間認識のため、「元経営者だから大丈夫」をフックの大サイズテキストとして
  採用し、「60代の老後資金が狙われる」または「SNS投資詐欺の罠」を小さく添える
  レイアウトに調整。これは確定タイトルの意味を保ちつつ、サムネ可読性のための
  運用判断であり、コピー自体を改変したわけではない

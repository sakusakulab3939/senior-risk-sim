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

**文字入れスペース確保**：段階2で下部と右側に「自分は騙されない」という過信バイアスのテキストが配置される予定のため、顔・目元は画面の上部2/3に収め、下部1/3は背景の質感は保ちつつ、顔や手など細部の重要な要素が掛からないようにする。

a Japanese man in his early 60s, short greying receding hair, thin-framed glasses, beige cardigan over a pale collared shirt, average build, an extreme close-up on his pale shocked face frozen in dread, wide fearful eyes contrasting with his confident business-owner bearing, positioned in the upper-to-middle portion of frame, a warm traditional Japanese living room, tatami mat flooring, wooden sliding shoji doors, low wooden table, warm-toned lighting, family photos and small plants on a shelf, softly blurred background in the lower portion maintaining atmospheric depth without character elements, cold desaturated dramatic lighting, 16:9 landscape thumbnail composition, subject large and prominent but with intentional lower-third spacing for text overlay, dramatic close-up framing optimized for small preview size, manga anime style, cel shading, crisp clean linework, controlled color palette, absolutely no text, no letters, no words, no speech bubbles, no sound effects, no captions, no watermarks, no signatures, no UI elements in the image

### 段階2（GPT Image 2.0／文字入れ）

Using the image generated in Step 1 as the base, add Japanese thumbnail title text.
Title copy source (from metadata_draft.json title_candidates): 「金融庁登録業者の確認方法、「自分は騙されない」という過信バイアスへの警鐘を知らずに払った代償——SNS型投資詐欺・退職金一括投資」。
This candidate is long, so for thumbnail legibility: display the short hook phrase
「自分は騙されない」という過信バイアス in large, bold, high-contrast Japanese sans-serif
text across the upper third of the frame, positioned so it does not cover the subject's
face. Place the remainder of the title copy in smaller supporting text along the bottom
edge, preserving the full candidate text somewhere in frame. Add a strong dark outline or
drop shadow for legibility against the background at small preview sizes. Do not alter the
underlying image, character appearance, or background — add text only.

---

## 案2：スマホの残高画面（伸び続ける数字）の下に差す暗い影——3パターン構成

案2は、metadata_final.json の confirmed_title 「元経営者だから大丈夫」——60代の老後資金が狙われるSNS投資詐欺の落とし穴 をベースに、
段階1で3つの異なる構図・演出パターンを用意し、段階2（文字入れ）は全パターン共通で運用する。

### パターン2-v2-1：スマホの残高画面＋暗い影（対比構図）

#### 段階1（nanobanana／文字なし）

**参照画像**：P1_fujita_kenichi.png を必ず参照画像として添付すること（トレイトロックの一貫性を保つため）

**文字入れスペース確保**：段階2で右側中央に「元経営者だから大丈夫」が大きく配置され、下部にサブテキストが入る予定のため、顔は画面左側と上部に配置し、右側と下部1/3は背景の質感は保ちつつ、顔や目元が掛からないようにする。

a Japanese man in his early 60s, short greying receding hair, thin-framed glasses, beige cardigan over a pale collared shirt, average build, his hand holding a smartphone positioned in the left-center area of frame, the phone screen glowing brightly with a rising balance graph with no legible content, a dark ominous shadow creeping up from beneath the phone across his face positioned in the upper-left quadrant, his face occupying the left and upper portion of frame while maintaining clear space on the right side and lower third for text overlay, a warm traditional Japanese living room, tatami mat flooring, wooden sliding shoji doors, low wooden table, warm-toned lighting, family photos and small plants on a shelf, softly blurred background in the right and lower portions maintaining atmospheric depth without character details, cold heavily desaturated low-key dramatic lighting, 16:9 landscape thumbnail composition, subject large and prominent with intentional right-side and lower-third spacing for text, dramatic close-up framing optimized for small preview size, manga anime style, cel shading, crisp clean linework, controlled color palette, absolutely no text, no letters, no words, no speech bubbles, no sound effects, no captions, no watermarks, no signatures, no UI elements in the image

#### 段階2（GPT Image 2.0／文字入れ）—全パターン共通

Using the generated image as the base, add Japanese thumbnail title text.
Title copy (from metadata_final.json confirmed_title): 「元経営者だから大丈夫」——60代の老後資金が狙われるSNS投資詐欺の落とし穴。
For thumbnail legibility: display the hook phrase 「元経営者だから大丈夫」 in very large,
bold, high-contrast white or yellow Japanese sans-serif text as the dominant visual element,
positioned along the center-right of the frame. Beneath or beside it in smaller supporting
text, add 「60代の老後資金が狙われる」 or simply 「SNS投資詐欺の罠」 to anchor the context
while keeping the main message about overconfidence prominent. Ensure key visual elements
(smartphone, subject's face) remain clearly visible. Add a strong dark outline or drop shadow
around the text for legibility against background at small preview sizes. Do not alter the
underlying image, character appearance, or background — add text only.

---

### パターン2-v2-2：ビフォーアフター型（左右対比）

#### 段階1（nanobanana／文字なし）

**参照画像**：P1_fujita_kenichi.png を必ず参照画像として添付すること（トレイトロックの一貫性を保つため）

**文字入れスペース確保**：段階2で中央帯に「元経営者だから大丈夫」という大きなテキストが配置される予定のため、左右の顔は中央の縦帯からやや離して配置し、中央帯（特に顔の高さ帯）は背景の質感は保ちつつ、目元や細部が掛からないようにする。顔は左側と右側の外側に配置することで、中央の文字スペースを確保する。

split-screen composition with dramatic left-right contrast and center text spacing: 

LEFT SIDE (self-assured before): a Japanese man in his early 60s, short greying receding hair, thin-framed glasses, beige cardigan over a pale collared shirt, average build, viewed from a slightly upward angle emphasizing strength and confidence, positioned toward the outer left edge of frame, with a proud, smug, self-assured expression and bright direct gaze, bathed in warm golden-orange lighting, standing in a bright, prosperous-looking warm traditional Japanese living room with tatami mat flooring, wooden sliding shoji doors, low wooden table, warm-toned mood lighting, family photos on shelf, and background details including framed company founder certificates, a formal letter envelope (retirement lump sum notification), and a piggy bank or safe, softly blurred warm background;

RIGHT SIDE (devastated after): the same man viewed from a slightly downward camera angle emphasizing weakness and defeat, positioned toward the outer right edge of frame, with a pale, ashen, shell-shocked, devastated expression, eyes hollow and wide with dread and realization of loss, bathed in cold blue-cyan harsh lighting, in the same room now rendered in cold desaturated tones, ominous deep shadows creeping across his face and body, with background elements now darkened and sinister including the glow of a smartphone screen casting eerie light on his features, and the room itself appearing claustrophobic and trap-like, softly blurred cold background;

center vertical band maintains atmospheric background texture but is clear of character facial details, allowing for text overlay of hook phrase; both sides clearly delineated by a sharp vertical dividing line or dramatic lighting gradient transition at center, emphasizing the psychological rupture between before and after, 16:9 landscape thumbnail composition, subjects positioned toward outer edges with intentional center spacing for text, dramatic close-up framing optimized for small preview size, manga anime style, cel shading, crisp clean linework with exaggerated emotional contrast, absolutely no text, no letters, no words, no speech bubbles, no sound effects, no captions, no watermarks, no signatures, no UI elements in the image

#### 段階2（GPT Image 2.0／文字入れ）—全パターン共通

（上記と同じ）

---

### パターン2-v2-3：視線誘導型（手のクローズアップ）

#### 段階1（nanobanana／文字なし）

**参照画像**：P1_fujita_kenichi.png を必ず参照画像として添付すること（トレイトロックの一貫性を保つため）

**文字入れスペース確保**：段階2で上部または左上にテキストが配置される予定のため、スマートフォンと手は下部・中央に保ち、背景となる顔のぼやけた要素は背景上部に配置する。上部1/3と左側は背景の質感は保ちつつ、顔の重要な細部（目元など）が掛からないようにして、テキスト配置スペースを確保する。

close-up focus on a Japanese man's hand in his early 60s holding a smartphone, the phone screen glowing brightly with a rising balance graph with no legible content, the smartphone dominating the lower-middle to lower-right portion of the frame, soft warm lighting on the hand and device, while in the softly blurred background above and behind the phone, the same man's face is visible but out of focus in the upper background, showing an anxious, worried, uncertain expression with furrowed brow and pursed lips contrasting with the bright promise of the glowing screen, positioned in upper portion to avoid covering upper-third text space, a warm traditional Japanese living room setting visible but unfocused in the upper and left portions maintaining atmospheric depth, cold desaturated dramatic lighting in the background, 16:9 landscape thumbnail composition, layered depth from sharp phone in lower-middle foreground to soft face in upper background, with intentional upper-third and left-side spacing for text overlay, framing optimized for small preview size, manga anime style, cel shading, crisp clean linework, controlled color palette, absolutely no text, no letters, no words, no speech bubbles, no sound effects, no captions, no watermarks, no signatures, no UI elements in the image

#### 段階2（GPT Image 2.0／文字入れ）—全パターン共通

（上記と同じ）

---

## 案3：なりすまし広告のスクショ風ビジュアル＋「その広告、あなたも見た」

### 段階1（nanobanana／文字なし）

**参照画像**：P1_fujita_kenichi.png を必ず参照画像として添付すること（トレイトロックの一貫性を保つため）

**文字入れスペース確保**：段階2で左上に【実録シミュレーション】のバッジが配置され、下部1/3に本文テキストが入る予定のため、広告グラフィックは画面の上部・中央に配置し、人物は背景に小さくぼやかし、左上と下部1/3は背景の質感は保ちつつ、人物の顔や細部が掛からないようにしてテキストスペースを確保する。

a mock investment advertisement screenshot-style graphic featuring a smiling celebrity investor portrait and a fake verified checkmark badge, positioned in the center-upper to center portion of the frame, with rows of plain placeholder bars instead of readable text, a Japanese man in his early 60s, short greying receding hair, thin-framed glasses, beige cardigan over a pale collared shirt, average build, softly out of focus in the background holding a smartphone displaying the advertisement, positioned behind and below the mock ad graphic to avoid blocking the upper-left and lower-third text spaces, a warm traditional Japanese living room, tatami mat flooring, wooden sliding shoji doors, low wooden table, warm-toned lighting, family photos and small plants on a shelf, softly blurred background in the upper-left and lower portions maintaining atmospheric depth without character facial details, slightly cool dramatic lighting, 16:9 landscape thumbnail composition, advertisement graphic prominent with character in supporting background, with intentional upper-left and lower-third spacing for text overlay, dramatic close-up framing optimized for small preview size, manga anime style, cel shading, crisp clean linework, controlled color palette, absolutely no text, no letters, no words, no speech bubbles, no sound effects, no captions, no watermarks, no signatures, no UI elements in the image

### 段階2（GPT Image 2.0／文字入れ）

Using the image generated in Step 1 as the base, add Japanese thumbnail title text.
Title copy (from metadata_draft.json title_candidates): 「【実録シミュレーション】SNS型投資詐欺・退職金一括投資の末路」。
Display 【実録シミュレーション】 as a smaller badge-style label in the upper-left corner,
and SNS型投資詐欺・退職金一括投資の末路 in large, bold, high-contrast Japanese sans-serif
text along the bottom third of the frame, positioned to avoid covering the fake
advertisement graphic. Add a strong dark outline or drop shadow for legibility against the
background at small preview sizes. Do not alter the underlying image, character appearance,
or background — add text only.

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

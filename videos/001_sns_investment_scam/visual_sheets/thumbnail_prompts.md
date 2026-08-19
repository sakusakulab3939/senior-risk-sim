# サムネイル生成プロンプト（001_sns_investment_scam）

`blueprint.json` の `thumbnail_direction`（3案）を、実際の2段階生成ワークフロー
（段階1：nanobananaで文字なしの画像を生成 → 段階2：GPT Image 2.0でタイトルコピーを合成）
向けのプロンプトに展開したもの。

タイトルコピーは `metadata_final.json` の `confirmed_title`（案2のみ）および
`output/metadata_draft.json` の `title_candidates`（案1・案3）から、各方向性に
最も合うものを1つずつ、3案とも別の候補を割り当てている。

> **注記**：案2は `metadata_final.json` の確定タイトルに更新済み。案1・案3は
> 引き続きmetadata_draft.jsonの候補から参照（B-6後の見直しは案2のみ実施）。

---

## 案1：「元経営者だから大丈夫」という慢心を煽るコピー＋青ざめた表情

### 段階1（nanobanana／文字なし）

a Japanese man in his early 60s, short greying receding hair, thin-framed glasses, beige cardigan over a pale collared shirt, average build, an extreme close-up on his pale shocked face frozen in dread, wide fearful eyes contrasting with his confident business-owner bearing, a warm traditional Japanese living room, tatami mat flooring, wooden sliding shoji doors, low wooden table, warm-toned lighting, family photos and small plants on a shelf, softly blurred background, cold desaturated dramatic lighting, 16:9 landscape thumbnail composition, subject large and prominent in frame, dramatic close-up framing optimized for small preview size, manga anime style, cel shading, crisp clean linework, controlled color palette, absolutely no text, no letters, no words, no speech bubbles, no sound effects, no captions, no watermarks, no signatures, no UI elements in the image

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

a Japanese man in his early 60s, short greying receding hair, thin-framed glasses, beige cardigan over a pale collared shirt, average build, his hand holding a smartphone glowing with a rising balance graph with no legible content, a dark ominous shadow creeping up from beneath the phone across his face, a warm traditional Japanese living room, tatami mat flooring, wooden sliding shoji doors, low wooden table, warm-toned lighting, family photos and small plants on a shelf, softly blurred background, cold heavily desaturated low-key dramatic lighting, 16:9 landscape thumbnail composition, subject large and prominent in frame, dramatic close-up framing optimized for small preview size, manga anime style, cel shading, crisp clean linework, controlled color palette, absolutely no text, no letters, no words, no speech bubbles, no sound effects, no captions, no watermarks, no signatures, no UI elements in the image

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

split-screen composition: left side shows a Japanese man in his early 60s, short greying receding hair, thin-framed glasses, beige cardigan over a pale collared shirt, average build, with a confident, self-assured smug expression and bright direct gaze, standing in a warm traditional Japanese living room with tatami mat flooring, wooden sliding shoji doors, low wooden table, warm-toned lighting; right side shows the same man with a pale, shell-shocked, devastated expression, eyes wide with dread and realization, in the same setting with cold desaturated dramatic lighting and ominous shadows; both sides clearly delineated by a subtle vertical dividing line or gradient transition, softly blurred background, 16:9 landscape thumbnail composition, subjects large and prominent in frame, dramatic close-up framing optimized for small preview size, manga anime style, cel shading, crisp clean linework, controlled color palette, absolutely no text, no letters, no words, no speech bubbles, no sound effects, no captions, no watermarks, no signatures, no UI elements in the image

#### 段階2（GPT Image 2.0／文字入れ）—全パターン共通

（上記と同じ）

---

### パターン2-v2-3：視線誘導型（手のクローズアップ）

#### 段階1（nanobanana／文字なし）

close-up focus on a Japanese man's hand in his early 60s holding a smartphone, the phone screen glowing brightly with a rising balance graph with no legible content, the smartphone dominating the lower-middle portion of the frame, soft warm lighting on the hand and device, while in the softly blurred background above and behind the phone, the same man's face is visible but out of focus, showing an anxious, worried, uncertain expression with furrowed brow and pursed lips contrasting with the bright promise of the glowing screen, a warm traditional Japanese living room setting visible but unfocused, cold desaturated dramatic lighting in the background, 16:9 landscape thumbnail composition, layered depth from sharp phone in foreground to soft face in background, framing optimized for small preview size, manga anime style, cel shading, crisp clean linework, controlled color palette, absolutely no text, no letters, no words, no speech bubbles, no sound effects, no captions, no watermarks, no signatures, no UI elements in the image

#### 段階2（GPT Image 2.0／文字入れ）—全パターン共通

（上記と同じ）

---

## 案3：なりすまし広告のスクショ風ビジュアル＋「その広告、あなたも見た」

### 段階1（nanobanana／文字なし）

a mock investment advertisement screenshot-style graphic featuring a smiling celebrity investor portrait and a fake verified checkmark badge, with rows of plain placeholder bars instead of readable text, a Japanese man in his early 60s, short greying receding hair, thin-framed glasses, beige cardigan over a pale collared shirt, average build, softly out of focus in the background holding a smartphone displaying the advertisement, a warm traditional Japanese living room, tatami mat flooring, wooden sliding shoji doors, low wooden table, warm-toned lighting, family photos and small plants on a shelf, softly blurred background, slightly cool dramatic lighting, 16:9 landscape thumbnail composition, subject large and prominent in frame, dramatic close-up framing optimized for small preview size, manga anime style, cel shading, crisp clean linework, controlled color palette, absolutely no text, no letters, no words, no speech bubbles, no sound effects, no captions, no watermarks, no signatures, no UI elements in the image

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

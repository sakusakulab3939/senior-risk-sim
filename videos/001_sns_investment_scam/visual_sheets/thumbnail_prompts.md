# サムネイル生成プロンプト（001_sns_investment_scam）

`blueprint.json` の `thumbnail_direction`（3案）を、実際の2段階生成ワークフロー
（段階1：nanobananaで文字なしの画像を生成 → 段階2：GPT Image 2.0でタイトルコピーを合成）
向けのプロンプトに展開したもの。

タイトルコピーは `output/metadata_draft.json` の `title_candidates` から、各方向性に
最も合うものを1つずつ、3案とも別の候補を割り当てている。

> **注記**：タイトルコピーはmetadata_draft.jsonの叩き台をそのまま使用しているため、
> B-6（メタデータ磨き）実施後に見直しが必要。

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

## 案2：スマホの残高画面（伸び続ける数字）の下に差す暗い影

### 段階1（nanobanana／文字なし）

a Japanese man in his early 60s, short greying receding hair, thin-framed glasses, beige cardigan over a pale collared shirt, average build, his hand holding a smartphone glowing with a rising balance graph with no legible content, a dark ominous shadow creeping up from beneath the phone across his face, a warm traditional Japanese living room, tatami mat flooring, wooden sliding shoji doors, low wooden table, warm-toned lighting, family photos and small plants on a shelf, softly blurred background, cold heavily desaturated low-key dramatic lighting, 16:9 landscape thumbnail composition, subject large and prominent in frame, dramatic close-up framing optimized for small preview size, manga anime style, cel shading, crisp clean linework, controlled color palette, absolutely no text, no letters, no words, no speech bubbles, no sound effects, no captions, no watermarks, no signatures, no UI elements in the image

### 段階2（GPT Image 2.0／文字入れ）

Using the image generated in Step 1 as the base, add Japanese thumbnail title text.
Title copy (from metadata_draft.json title_candidates): 「SNS型投資詐欺・退職金一括投資で人生が狂った話」。
Display in large, bold, high-contrast Japanese sans-serif text, split across two or three
lines along the right side of the frame, leaving the smartphone and the man's face clearly
visible on the left. Add a strong dark outline or drop shadow for legibility against the
living room background at small preview sizes. Do not alter the underlying image, character
appearance, or background — add text only.

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

### 段階2：タイトルコピーがmetadata_draft.jsonと矛盾しないか
- 案1→title_candidates[2]（過信バイアスへの代償）、案2→title_candidates[0]（人生が狂った話）、
  案3→title_candidates[1]（実録シミュレーション・末路）と3案とも別候補を割り当て、
  いずれも `metadata_draft.json` に実在する文字列をそのまま使用している（新規のコピーは作成していない）
- 案1のみ、割り当てた候補（title_candidates[2]）が文字数超過のためサムネ上では
  「フック部分を大きく強調＋全文は小さく添える」構成にしている。これは表示レイアウト上の
  調整であり、コピー自体を書き換えたわけではない（矛盾ではなく可読性のための運用判断として
  段階2プロンプト内に明記済み）

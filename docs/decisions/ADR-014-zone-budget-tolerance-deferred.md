# ADR-014: explanation_layoutごとの許容誤差調整の保留

## 背景
`validate_zone_char_budgets`（`production_extractor.py`）は、全ゾーンに一律±15%の
許容誤差でNARRATION文字数を検査している。しかし`prompts/write_full_script.md`の
「5. explanationゾーン：explanation_layoutによる配置切り替え」では、distributed/
compressedレイアウトの場合、explanationゾーンの実際の文字数を意図的に通常計算値の
6〜7割・6割程度に圧縮する設計になっている（該当箇所に「DRAFT値・根拠なし」と
明記済み）。

この設計と、±15%固定の検証ロジックは前提が矛盾しており、distributed/compressedを
使う動画では毎回explanationゾーンで警告が発生する。002（explanation_layout:
distributed）の実行で実際にこの警告が発生することを確認した。

## 決定
今回は許容誤差ロジックを修正しない。次回作以降、複数動画のdistributed/compressed
実測データが溜まってから、閾値をexplanation_layoutごとに調整する（例：
trailing_blockは±15%のまま、distributed/compressedは±40%程度に緩める、または
6〜7割・6割の目標値を基準にした専用チェックに置き換える）。

## 捨てた選択肢と理由
- **今回すぐに閾値を可変にする**：判断根拠となる実測データが002の1本しかなく、
  適切な閾値を決める材料が不十分なため見送った。根拠のない数値をまた1つ増やす
  だけになる

## 結果
（未記入。次回作以降、distributed/compressedの実測データが複数溜まった時点で
閾値見直しを検討する）

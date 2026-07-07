# ADR-001: ADRテンプレとmetrics.csvの初期化（Phase 0-7）

## 背景
risk_sim.jsonの結末パターン（ending_pattern）と解説レイアウト（explanation_layout）は、
比率をJSON側に固定せず、blueprint.json側で動画ごとに人間が指定する設計にした
（Opusレビューで確定）。この選択を検証するには、公開後の維持率データと
突合できる記録の仕組みが必要だった。

## 決定
metrics.csvにvideo_id, ending_pattern, explanation_layoutなどの列を持たせ、
1本ごとに手動記録する方式にした。

## 捨てた選択肢と理由
risk_sim.json側に結末パターンの比率を実装する案も検討したが、根拠のない
初期仮説が「守るべき設計」として固定化されるリスクがあるため採用しなかった。

## 結果
（まだ未記入。10本回した後に維持率データが溜まってから追記する）

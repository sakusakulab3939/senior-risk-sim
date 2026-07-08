# ADR-002: Analysis Baseline / Restart Modesの導入見送り

## 背景
旧パイプライン（senior_story_workflow）には、競合収集・transcript・構成分析の結果を
baselineとして保存し、再利用する仕組みがあった。

## 決定
risk_sim初期フェーズ（検証段階の10本）では導入しない。

## 捨てた選択肢と理由
Phase A（研究自動化）自体をまだ構築していない段階で、再利用の仕組みだけ先に
作る必要がないため。

## 再検討のタイミング
Phase A（月次リサーチバッチ）に着手する時。

## 結果
（未記入）

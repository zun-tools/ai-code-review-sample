# ai-code-review-sample

AI時代のコードレビューを扱った動画のサンプルです。
変更の場所によって、マージに必要な人の承認が変わる設定を置いています。使いかたは下のとおりです。

- `.github/CODEOWNERS` — 必ず人が見る場所と、見る人（チーム）
- `.github/workflows/ci.yml` — テスト（マージに必須の検査）
- `.github/workflows/open-pr.yml` — エージェントが PR を開く代わりに、GitHub Actions のボットが PR を開いて自動マージを予約する

設定の時点: 2026年10月（GitHub の仕様は変わることがあります）

License: MIT

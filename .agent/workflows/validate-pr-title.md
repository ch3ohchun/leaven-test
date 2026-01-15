---
description: 在 Pull Request (PR) 提交時自動檢查標題是否符合文件中的 Prefix 規範 (feat/、fix/、docs/ 等)，若不符則發出警告或拒絕。
---
1. 取得 PR 標題。
2. 檢查標題是否以指定 Prefix 開頭 (`feat`, `fix`, `docs`, `refactor`, `test`, `chore`)。
   - 格式範例：`feat: add login page` 或 `feat/add login page` (視專案習慣而定，但需統一)。
3. 如果不符合，在 PR 留言提示正確格式或設定 CI 狀態為失敗。

---
description: 根據 PR 變更的檔案內容與類型，自動生成 What’s this PR about? 欄位的摘要內容，輔助開發者填寫 PR Template。
---
1. 讀取 PR 的 diff 內容 (變更的檔案與程式碼)。
2. 分析變更類型 (新增功能、修復 bug、重構等)。
3. 自動生成摘要文字，填入 PR Template 的 `What’s this PR about?` 欄位。
4. 提醒使用者檢查並補充細節。

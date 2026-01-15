---
description: 根據現有的 test-frontend 和 test-backend 流程，進一步要求 Agent 讀取特定函式或類別，自動生成基礎的單元測試腳本，加速測試覆蓋率。
---
1. 接收使用者指定的檔案或函式/類別名稱。
2. 分析該程式碼的邏輯。
3. 根據是前端還是後端，生成對應的測試代碼：
   - 前端：使用 Jest/RTL。
   - 後端：使用 pytest。
4. 將測試代碼寫入對應的測試檔案 (例如 `frontend/src/components/__tests__` 或 `backend/test`)。

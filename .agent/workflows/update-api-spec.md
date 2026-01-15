---
description: 根據後端新增或修改的 API 路徑，自動更新內部 API 文件或型別定義檔，確保前後端溝通一致。
---
1. 掃描 `backend` 目錄下的 API 定義 (例如 FastAPI route 或其他框架路由)。
2. 提取 API 路徑、HTTP 方法、請求與回應結構。
3. 更新前端的 API 定義檔 (例如 `frontend/src/api/schema.ts` 或 Swagger 文件)。
4. 確保符合後端/前端資料傳輸規範。

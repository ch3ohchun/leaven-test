---
description: 根據輸入的組件名稱與用途，自動生成基礎的 React 組件檔案 (.jsx)、Styling 檔案 (.module.css 或直接使用 Tailwind CSS class)，並遵循前端的大駝峰式命名法。
---
1. 詢問使用者組件名稱 (例如 `UserProfile`) 和用途。
2. 檢查 `frontend/src/components` 下是否已存在該組件。
3. 產生組件檔案 `frontend/src/components/[ComponentName].jsx`：
   - 使用大駝峰式命名 (PascalCase)。
   - 使用 React functional component 和 shadcn/ui (如果適用)。
   - 使用 Tailwind CSS 進行樣式設定。
4. (選用) 如果需要個別 CSS module，產生 `frontend/src/components/[component-name].module.css` (kebab-case)。

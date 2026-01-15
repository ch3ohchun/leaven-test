---
description: 根據功能主題，在 backend/services/ 下建立新的模組資料夾與對應的主服務類別檔案，並遵循後端的大駝峰式命名法。
---
1. 詢問使用者功能模組名稱 (例如 `auth` 或 `report`)。
2. 在 `backend/services/` 下建立模組資料夾 `backend/services/[module_name]/` (snake_case)。
3. 在該資料夾下建立 `__init__.py`。
4. 建立主服務類別檔案 `backend/services/[module_name]/[module_name]_service.py` (或其他適當名稱)。
5. 在檔案中定義 class，名稱使用大駝峰式命名 (PascalCase)，並實作主接口方法。

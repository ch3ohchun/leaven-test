---
description: 監控 requirements.txt 或 package.json 中的套件是否有新的主要或次要版本更新，並建立一個包含更新日誌摘要的 chore PR。
---
1. 讀取 `backend/config/requirements.txt` 或 `pyproject.toml`。
2. 讀取 `frontend/package.json`。
3. 檢查是否有可用更新 (使用 `npm outdated` 或 `pip list --outdated`)。
4. 如果有更新，建立一個新分支 `chore/update-dependencies`。
5. 更新鎖定檔 (lock file)。
6. 提交 PR，並附上更新日誌連結。

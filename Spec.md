## 開發流程

.agent/workflows裡的東西  
1\. 程式碼生成與標準化 (Code Generation & Standardization)

| Workflow 名稱 | 描述 (用途) | 相關規範與技術 |
| ----- | ----- | ----- |
| **build-empty-project** | 自動生成專案的基礎資料夾架構 (backend/ 和 frontend/)、設定檔及必要的啟動檔案。 | 專案架構 (Project Structure) |
| **create-ui-component** | 根據輸入的組件名稱與用途，自動生成基礎的 React 組件檔案 (.jsx)、Styling 檔案 (.module.css 或直接使用 Tailwind CSS class)，並遵循前端的**大駝峰式命名法**。 | React, Tailwind CSS, shadcn/ui, 前端命名習慣 |
| **new-module** | 根據功能主題，在 `backend/services/` 下建立新的模組資料夾與對應的主服務類別檔案，並遵循後端的**大駝峰式命名法**。 | Python 3.11, 後端命名習慣 (Module, Class), 專案架構 (backend/services/) |
| **generate-service-class** | 根據輸入的後端功能主題，自動生成一個帶有主入口方法的 Python 服務類別檔案，並遵循後端的**大駝峰式命名法**。 | Python 3.11, 後端命名習慣 (Class) |
| **update-api-spec** | 根據後端新增或修改的 API 路徑，自動更新內部 API 文件或型別定義檔，確保前後端溝通一致。 | 後端/前端資料傳輸規範 (API Data Transfer Specifications) |

2\. 品質保證與審查 (QA & Review Automation)

| Workflow 名稱 | 描述 (用途) | 相關規範與技術 |
| ----- | ----- | ----- |
| **test-frontend** | 執行前端 React 應用程式的單元測試，確保 UI 組件和邏輯的正確性。 | RTL, React Testing Library |
| **test-backend** | 執行後端 Python 服務的單元測試，確保 API 邏輯和業務邏輯的正確性。 | Python 3.11, pytest |
| **generate-unit-test** | 根據現有的 test-frontend 和 test-backend 流程，進一步要求 Agent 讀取特定函式或類別，自動生成基礎的單元測試腳本，加速測試覆蓋率。 | RTL, pytest, test/translation tests |
| **validate-pr-title** | 在 Pull Request (PR) 提交時自動檢查標題是否符合文件中的 **Prefix 規範** (feat/、fix/、docs/ 等)，若不符則發出警告或拒絕。 | PR 規範 (Prefix) |
| **generate-pr-summary** | 根據 PR 變更的檔案內容與類型，自動生成 **What’s this PR about?** 欄位的摘要內容，輔助開發者填寫 PR Template。 | PR Template 填寫指南 |

3\. 環境與部署 (Environment & Deployment)

| Workflow 名稱 | 描述 (用途) | 相關規範與技術 |
| ----- | ----- | ----- |
| **check-dependency-updates** | 監控 requirements.txt 或 package.json 中的套件是否有新的主要或次要版本更新，並建立一個包含更新日誌摘要的 chore PR。 | Python 3.11, uv, 前端/後端依賴管理 |
| **deployment-rollback** | 提供一個快速觸發前一次穩定版本部署的能力，以應對緊急生產環境問題。 | GitHub Actions CI/CD, Azure/GCP 部署流程 |

[GEMINI.md](http://GEMINI.md) : global rules

## 專案架構

/  
├── backend/                  \# 後端服務（Python）  
│   ├── services/             \# 核心服務程式碼 (以 Module 為單位)  
│   ├── test/                    \# 單元測試程式碼  
│   ├── config/                \# 環境設定、Prompt.yaml 及其他程式碼相關設定檔(yml)  
│   ├── data/                  \# 後端 API 需要讀取的參考資料或靜態檔案  
│   └── [main.py](http://main.py)             \# 後端api主要啟動程式  
│  
└── frontend/                 \# 前端應用程式 (React)  
    ├── public/                \# 靜態檔案（如 index.html, favicon 等）  
    └── src/                    \# 應用程式原始碼  
        ├── components/       \# 可重複使用的 UI 組件  
        ├── pages/            \# 頁面級別的組件/視圖  
        ├── assets/           \# 圖片、字體等靜態資源  
        └── utils/              \# 通用工具函式

## 技術選擇

| 類別 | 技術/工具 | 備註 |
| ----- | ----- | ----- |
| **前端** | React | 單元測試：[RTL](https://nissentech.org/react-testing-library/) (React Testing Library) |
|  | [Tailwind CSS](https://tailwindcss.com/) |  |
|  | [shadcn/ui](https://ui.shadcn.com/) |  |
| **後端** | [Python 3.11](https://www.python.org/downloads/release/python-3110/) | \- 使用 [uv](https://docs.astral.sh/uv/getting-started/features/) 建立虛擬環境與套件版本管理。 \- 單元測試：[pytest](https://ithelp.ithome.com.tw/articles/10364892) |
| **資料庫** | [SQLite](https://www.navicat.com/cht/company/aboutus/blog/2398-sqlite-%E5%85%A5%E9%96%80.html) |  |
| **環境變數** | [.env](https://israynotarray.com/other/20230218/3618693250/) 檔案儲存 |  |
| **版本控制** | [Git](https://hackmd.io/@sysprog/gnu-linux-dev/https%3A%2F%2Fhackmd.io%2F%40sysprog%2Fgit-with-github) | 每次開發前需開新分支，合併到 main 前請發 Pull Request (PR)。 |

### 

## 後端（Python）命名習慣

1. **Module (模組)**  
   * 每個模組對應一個功能主題。  
   * 每個模組僅定義一個同名 `class` 作為主接口。  
2. **Class (類別)**  
   * 名稱使用大駝峰式命名法（PascalCase），例如：`GloassaryLoader`。  
   * 提供一個清晰的對外方法作為主入口。  
   * 其他方法都為私有或保護（以底線開頭）。  
3. **Function (函式)**  
   * 名稱使用蛇形命名法（snake\_case）。  
   * **對外函式**：例如：`extract_term_mapping`。  
   * **對內函式**：例如：`_filter_terms_by_original_sentence`。  
   * 每個函式僅負責一個單一明確任務，避免過多邏輯分支，必要時拆成子函式。

## 前端（React）命名習慣

1. **Component (組件)**  
   * **名稱**：使用大駝峰式命名法（PascalCase），例如：`UserProfile`、`HeaderBar`。  
   * **檔案名**：組件檔案名應與組件名稱一致，例如：`UserProfile.jsx`。  
2. **Hooks (自定義 Hook) 與 Function (函式)**  
   * **名稱**：使用小駝峰式命名法（camelCase）。  
   * **Hooks**：名稱必須以 `use` 開頭，例如：`useUserData`、`useFormValidation`。  
   * **函式/變數**：例如：`handleClick`、`isLoggedIn`。  
3. **CSS/SCSS 檔案 (模組化)**  
   * **名稱**：使用連字號命名法（kebab-case），例如：`user-profile.module.css`。  
4. **Utility (工具) 檔案**  
   * **名稱**：使用小駝峰式命名法（camelCase），例如：`dateUtils.js` 。

### 

## 後端/前端資料傳輸規範 (API Data Transfer Specifications)

為了確保前後端溝通的一致性與錯誤處理的明確性，所有後端 API 的回傳格式將遵循以下標準化結構。後端 API 回應格式 (Backend API Response Schema)

* 後端回傳的 JSON 物件應包含三個標準欄位：`status`、`message` 和 `data`。  
    
  {  
    "status": "SUCCESS" | "ERROR",  
    "message": "string",  
    "data": "any" | null  
  }

| 欄位 | 型別 | 說明 | 範例值 |
| ----- | ----- | ----- | ----- |
| **status** | String | API 呼叫的狀態。**`SUCCESS`** 表示成功，**`ERROR`** 表示失敗。 | `"SUCCESS"` / `"ERROR"` |
| **message** | String | 狀態訊息。成功時可為空字串或描述成功操作，失敗時傳回錯誤訊息。 | `"使用者資料已成功儲存。"` / `"驗證失敗：密碼錯誤。"` |
| **data** | Any / Null | 實際回傳的業務資料。成功時傳回，失敗時應為 `null` 或省略。 | `{"userId": "U001", "name": "Leaven"}` / `null` |

* 前端處理邏輯 (Frontend Handling Logic)

前端應用程式應根據 API 回傳的 `status` 欄位進行處理：

1. **成功 (Status: `SUCCESS`)**  
   * **邏輯**：前端應檢查 `status` 是否為 `"SUCCESS"`。  
   * **資料**：從 `data` 欄位取得並使用所需的業務資料。  
   * **提示**：可選擇性地顯示 `message` 欄位作為成功的提示訊息（例如：彈出通知）。  
2. **錯誤 (Status: `ERROR`)**  
   * **邏輯**：前端應檢查 `status` 是否為 `"ERROR"`。  
   * **錯誤訊息**：從 `message` 欄位取得錯誤的詳細描述，並將其顯示給使用者（例如：警示框、表單錯誤提示）。  
   * **資料**：忽略 `data` 欄位。

## PR 規範

請使用以下 **Prefix** 開頭，幫助大家快速知道 PR 的類型：

| Prefix | 類型 | 範例 |
| ----- | :---: | :---: |
| **feat** | 新功能 | `feat/add file-based translation in app.py` |
| **fix** | 修 bug | `fix/python docx api null` |
| **docs** | 文件變更 | `docs/add new requirements.txt` |
| **refactor** | 重構（不影響功能） | `refactor/moved evan PatentTranslate` |
| **test** | 加/改測試 | `test/translation tests` |
| **chore** | 雜項設定 | `chore/clean .gitignore rules` |

PR Template 填寫指南

| 欄位 | 怎麼寫 | 範例 |
| ----- | ----- | ----- |
| **What’s this PR about?** | 簡單列出改了什麼、為了解決什麼。 | \- 新增檔案翻譯功能 \- 修正 docx API 錯誤處理 \- 抽離翻譯邏輯到 utils |
| **How was it tested?** | 寫出怎麼驗證你的改動是 OK 的（包含單元測試或手動測試步驟）。 | \- 單元測試：`test_translation.py` \- 手動測試：上傳 `.docx` 檔案測試翻譯流程 \- 告訴 reviewer 怎麼測試- Expected result |
| **UI Changes** | 改到 UI 就放截圖或 GIF；沒有就刪掉這區。 | `![before](url)` / `![after](url)` |
| **Related Issues** | 如果有對應的 issue 或 ticket，要記得加上。 | `Closes #42` / `Related to #77` |
| **Notes for Reviewers** | 有任何潛在踩雷點、需要特別注意的設定，都寫在這裡。 | \- 新增的翻譯功能會使用 OpenAI API，請確認 API key 已設定- CI config 有更新，請注意 runner 的版本差異 |

### 

## 部署

* 使用 **GitHub Actions CI/CD** 部署到 **Azure**。  
* **前端**：部署至 Static Web Apps。  
* **後端**：部署至 App Services。  
* GCP 的 Firebase Hosting \+ Cloud Run


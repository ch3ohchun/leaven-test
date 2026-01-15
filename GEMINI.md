# GEMINI.md - Project Rules & Guidelines

## 1. Project Structure

```
/  
├── backend/                  # Python 3.11 Backend Services
│   ├── services/             # Core service logic (Modularized)
│   ├── test/                 # Unit tests (pytest)
│   ├── config/               # Configuration files (env, prompts, etc.)
│   ├── data/                 # Static data/resources for API
│   └── main.py               # API Entry point
│  
└── frontend/                 # React Frontend Application
    ├── public/               # Static assets (index.html, favicon)
    └── src/                  # Source code
        ├── components/       # Reusable UI Components
        ├── pages/            # Page-level Views
        ├── assets/           # Images, Fonts
        └── utils/            # Utility functions
```

## 2. Technology Stack

### Frontend
- **Framework**: React
- **Styling**: [Tailwind CSS](https://tailwindcss.com/)
- **UI Library**: [shadcn/ui](https://ui.shadcn.com/)
- **Testing**: [RTL (React Testing Library)](https://nissentech.org/react-testing-library/)

### Backend
- **Language**: [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- **Package Manager**: [uv](https://docs.astral.sh/uv/getting-started/features/)
- **Testing**: [pytest](https://ithelp.ithome.com.tw/articles/10364892)
- **Database**: [SQLite](https://www.navicat.com/cht/company/aboutus/blog/2398-sqlite-%E5%85%A5%E9%96%80.html)
- **Environment**: `.env` file for secrets/config

### Version Control
- **Git**: Branch-based workflow. PRs required for `main`.

## 3. Naming Conventions

### Backend (Python)
- **Modules**: Snake case (e.g., `my_module`). One module per feature.
- **Classes**: PascalCase (e.g., `GlossaryLoader`). One main class per module.
- **Functions**: snake_case.
    - Public: `extract_term_mapping`
    - Private: `_filter_terms_by_original_sentence`
- **Design**: Each function should have a single responsibility.

### Frontend (React)
- **Components**: PascalCase (e.g., `UserProfile`). Filename matches component name (`UserProfile.jsx`).
- **Hooks**: camelCase, start with `use` (e.g., `useUserData`).
- **Functions/Variables**: camelCase (e.g., `handleClick`, `isLoggedIn`).
- **CSS Modules**: kebab-case (e.g., `user-profile.module.css`).
- **Utilities**: camelCase (e.g., `dateUtils.js`).

## 4. API Standards

### Response Schema
All backend APIs must return JSON with the following structure:

```json
{
  "status": "SUCCESS" | "ERROR",
  "message": "string",
  "data": "any" | null
}
```

- **status**: `SUCCESS` or `ERROR`.
- **message**: Description of result or error details.
- **data**: Payload if success, `null` or omitted if error.

### Frontend Handling
1. **SUCCESS**: Use `data`. Optionally show `message`.
2. **ERROR**: Show `message` to user (alert/toast). Ignore `data`.

## 5. PR Guidelines

### Title Prefix
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `refactor`: Code restructuring
- `test`: Tests
- `chore`: Maintenance/Config

### PR Template Sections
- **What’s this PR about?**: Summary of changes.
- **How was it tested?**: Verification steps.
- **UI Changes**: Screenshots/GIFs (if applicable).
- **Related Issues**: e.g., `Closes #42`.
- **Notes for Reviewers**: Special instructions/warnings.

## 6. Deployment
- **Platform**: Azure (via GitHub Actions CI/CD)
    - Frontend: Static Web Apps
    - Backend: App Services
- **Alternative**: GCP (Firebase Hosting + Cloud Run)

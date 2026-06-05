# llm-pipeline-starter

# 🤖 LLM Pipeline Starter

> Automated CI/CD pipeline that processes text through multiple Large Language Models (Claude + OpenAI) using GitHub Actions.

[![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org)
[![Anthropic](https://img.shields.io/badge/LLM-Claude-D4A27F)](https://www.anthropic.com)
[![OpenAI](https://img.shields.io/badge/LLM-OpenAI-412991?logo=openai&logoColor=white)](https://openai.com)

---

## 🎯 What this project demonstrates

This is a working example of integrating **LLM API calls into a CI/CD pipeline** — exactly the kind of automation modern AI-driven teams need.

- **Trigger-based execution** — pipeline runs automatically on push to `inputs/`
- **Multi-provider LLM support** — abstracted Claude + OpenAI calls behind a single CLI
- **Secrets management** — API keys stored as encrypted GitHub Actions secrets
- **GitOps output flow** — generated summaries auto-committed back to the repo
- **Cost-conscious by design** — uses Haiku (10× cheaper than Opus) for production workflow

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   1. PUSH to inputs/*.txt                                   │
│             │                                               │
│             ▼                                               │
│   2. GitHub Actions trigger                                 │
│             │                                               │
│             ▼                                               │
│   3. Ubuntu runner spins up                                 │
│        ├─ Python 3.11 setup                                 │
│        ├─ pip install -r requirements.txt                   │
│        └─ Load API secrets                                  │
│             │                                               │
│             ▼                                               │
│   4. run_llm.py                                             │
│        ├─→ Anthropic API (Claude Haiku 4.5)                 │
│        └─→ OpenAI API   (gpt-4o-mini)  [optional]           │
│             │                                               │
│             ▼                                               │
│   5. Output saved to outputs/summary_<provider>_<ts>.txt    │
│             │                                               │
│             ▼                                               │
│   6. Bot commits outputs back to main                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick start

### 1. Fork or clone this repo

```bash
git clone https://github.com/thinkAkili/llm-pipeline-starter.git
cd llm-pipeline-starter
```

### 2. Add your API keys as GitHub secrets

Navigate to **`Settings → Secrets and variables → Actions`** and add:

| Secret name | Source |
|---|---|
| `ANTHROPIC_API_KEY` | [console.anthropic.com](https://console.anthropic.com) |
| `OPENAI_API_KEY` | [platform.openai.com](https://platform.openai.com) *(optional)* |

### 3. Enable write permissions for the workflow

`Settings → Actions → General → Workflow permissions → Read and write permissions`

### 4. Trigger the pipeline

Edit any file under `inputs/` and push — or run manually from the **Actions** tab.

---

## 🧪 Local development

```bash
# Set up a virtual environment
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template and add your keys
cp .env.example .env
# Edit .env with your real keys

# Run with Claude only
python scripts/run_llm.py --provider claude

# Run with both providers
python scripts/run_llm.py --provider both
```

---

## 📁 Project structure

```
llm-pipeline-starter/
├── .github/workflows/
│   └── llm_summary.yml      # GitHub Actions pipeline
├── inputs/
│   └── sample.txt           # Text to be summarized
├── outputs/                 # Generated summaries (auto-committed)
├── scripts/
│   └── run_llm.py           # Dual LLM client
├── .env.example             # Template for local secrets
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech stack

| Layer | Tool |
|---|---|
| **CI/CD** | GitHub Actions |
| **Language** | Python 3.11 |
| **LLM Providers** | Anthropic (Claude Haiku 4.5), OpenAI (GPT-4o-mini) |
| **Secrets** | GitHub Actions encrypted secrets |
| **GitOps** | Auto-commit via `github-actions[bot]` |

---

## 💡 Design decisions

**Why dual-provider support?**
Production AI systems rarely commit to a single LLM vendor. Abstracting the provider behind a CLI flag means the same code can switch between Claude and OpenAI without changes — useful for cost optimization, A/B testing, or fallback strategies.

**Why Haiku in CI, not Opus?**
Haiku 4.5 is ~10× cheaper than Opus for comparable summarization quality. In a pipeline that may run on every push, this matters. Production AI is as much about cost engineering as model quality.

**Why auto-commit outputs?**
A GitOps pattern — outputs become part of the audit trail, reviewable in PRs, and reproducible from history. Better than ephemeral artifacts that disappear after a run.

---

## 🇫🇷 À propos / About

Ce projet a été construit comme démonstration concrète de l'intégration LLM dans un pipeline CI/CD moderne — une compétence centrale pour les rôles AI DevOps / MLOps. Il combine de l'automatisation classique (GitHub Actions, Python, secrets management) avec l'écosystème LLM actuel.

This project was built as a hands-on demonstration of integrating LLMs into a modern CI/CD pipeline — a core skill for AI DevOps / MLOps roles. It combines classic automation (GitHub Actions, Python, secrets management) with the current LLM ecosystem.

---

## 👤 Author

**Ashanty** — Automation Developer transitioning into AI DevOps
[GitHub](https://github.com/thinkAkili) · Montreal, Canada · Bilingual FR/EN

---

## 📄 License

MIT
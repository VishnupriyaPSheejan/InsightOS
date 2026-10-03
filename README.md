# InsightOS — Local Business Intelligence Demo

A runnable portfolio project: explore bundled synthetic sales data, filter it, inspect charts, ask simple natural-language questions, and export a filtered CSV. No API key, database, cloud account, or external dataset is required.

> **Data note:** `data/sales.csv` is synthetic and generated deterministically. It is not real company/customer data. Answers are descriptive and do not claim causal explanations.

## Run in VS Code (Python)
1. Install Python 3.11+.
2. Open this folder in VS Code.
3. Create a terminal and run:

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
4. Open the local URL shown in the terminal (usually http://localhost:8501).

## Run with Docker
```bash
docker compose up --build
```
Open http://localhost:8501. Stop with `Ctrl+C`; optionally run `docker compose down`.

## Tests
```bash
pytest -q
```

## Regenerate data
```bash
python scripts/generate_data.py
```
The checked-in CSV is already included, so regeneration is optional.

## GitHub Actions
`.github/workflows/ci.yml` runs pytest and builds the Docker image on pushes and pull requests. To publish/deploy, add a deployment workflow for your chosen host (e.g. Streamlit Community Cloud, Render, Azure, or a container registry). Keep credentials in GitHub Actions Secrets; never commit tokens.

## Architecture
```text
Bundled CSV → Pandas filtering/aggregation → Streamlit UI
                                  ├─ Plotly charts
                                  ├─ deterministic question router
                                  └─ CSV export
GitHub push/PR → Actions tests → Docker build
```

## Current scope and limitations
- The Q&A component is a transparent rule-based analyst, not an LLM or autonomous agent.
- “Why did revenue change?” reports a time comparison; it cannot establish causality.
- This starter is designed for local reproducibility. A production version could add SQL generation with read-only validation, an LLM provider, evaluation datasets, auth, and deployment.

## Suggested blog title
**“From CSV to Business Intelligence: Building a Reproducible Analytics App with Streamlit, Docker, and GitHub Actions”**

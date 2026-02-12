# Market Research Crew

Multi-agent market research powered by crewAI. Given a company domain (e.g., `salesforce.com`), the crew performs web research and produces a structured Markdown report including Executive Summary, SWOT Analysis, and Strategic Recommendations.

## Overview

- **Agents:**
	- Researcher uses a web search tool to gather company data.
	- Reporting Analyst synthesizes findings into a strategic report.
- **LLM:** Google Gemini 2.5 Flash via crewAI `LLM`.
- **Process:** Sequential tasks, research → reporting.
- **Outputs:** Markdown report saved to the `output` folder as `{company_domain}_report.md`.

Key files:
- [src/market_research/crew.py](src/market_research/crew.py) — agents, tasks, process, LLM setup
- [src/market_research/main.py](src/market_research/main.py) — run/train/replay/test entry points
- [src/market_research/config/agents.yaml](src/market_research/config/agents.yaml) — agent roles/goals/backstories
- [src/market_research/config/tasks.yaml](src/market_research/config/tasks.yaml) — task descriptions/expected outputs
- [src/market_research/tools/custom_tool.py](src/market_research/tools/custom_tool.py) — example custom tool (not used by default)

## Requirements

- Python `>=3.10,<3.14`
- [uv](https://docs.astral.sh/uv/) for dependency management
- API keys (set as environment variables):
	- `GOOGLE_API_KEY` for Gemini
	- `SERPER_API_KEY` for Serper web search

Set environment variables (PowerShell on Windows):

```powershell
$env:GOOGLE_API_KEY="your_google_api_key"
$env:SERPER_API_KEY="your_serper_api_key"
```

## Install

1) Install uv:

    ```bash
    pip install uv
    ```

2) Create a virtual environment and install project dependencies from `pyproject.toml`:

    ```bash
    uv sync
    ```

## Run

Interactive run (prompts for `company_domain`):

```bash
uv run run_crew
```

After completion, the report is written to `output/{company_domain}_report.md` (e.g., `output/IBM.com_report.md`).


## Configuration

- Update agents in [src/market_research/config/agents.yaml](src/market_research/config/agents.yaml)
- Update tasks in [src/market_research/config/tasks.yaml](src/market_research/config/tasks.yaml)
- Adjust LLM settings, tools, and output path in [src/market_research/crew.py](src/market_research/crew.py)
- Optional knowledge base at [knowledge/user_preference.txt](knowledge/user_preference.txt)

## Notes & Troubleshooting

- Ensure `GOOGLE_API_KEY` and `SERPER_API_KEY` are set before running; the researcher relies on Serper search and the crew uses Gemini.
- The LLM is rate-limited via `requests_per_minute` in [src/market_research/crew.py](src/market_research/crew.py) to improve stability.
- If console scripts aren’t found, reinstall with `uv pip install -e .` and ensure you run commands via `uv run`.

## License & Support

- Built with [crewAI](https://crewai.com). See crewAI docs: https://docs.crewai.com
- Community: https://discord.com/invite/X4JWnZnxPb
- Issues and examples: https://github.com/joaomdmoura/crewai

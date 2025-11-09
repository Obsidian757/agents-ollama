# agents-ollama — 12th House AI
![Banner](../BRAND/banner.png)

## Overview
Placeholder for **Ollama agent** development. Pre-scaffolded for future builds.

## Features
- `.env.example` stub for configuration  
- Ready for integration with Ollama models  

## Setup
1. Clone repo
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your Anthropic API key

## Running the Example

To run the Anthropic SDK example:

```bash
# Make sure your API key is set in .env or export it:
export ANTHROPIC_API_KEY='your-api-key-here'

# Run the Python script:
python3 example_anthropic.py
```

**Important**: Python code must be run in a Python interpreter or script file, not directly in the terminal shell.

## Structure
- `.env.example` – Environment variable template
- `requirements.txt` – Python dependencies
- `example_anthropic.py` – Example Anthropic SDK usage
- `README.md` – Project overview

## Roadmap
- Next: Add Ollama model orchestration + API

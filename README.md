# Code Review LLM

This repository implements a large language model (LLM) for code review assistance, covering data preparation, model training (SFT & DPO), evaluation, sandboxed inference, and serving via FastAPI.

## Project Structure
```
code-review-llm/
├── configs/          # Experiment configurations
├── data/             # Raw & processed data
├── src/              # Core source code
│   ├── data/         # Data pipelines
│   ├── models/       # Model loading & tokenization
│   ├── train/        # Training scripts
│   ├── preference/   # DPO preference data generation
│   ├── evaluation/   # Evaluation utilities
│   ├── sandbox/      # Secure execution sandbox
│   └── serving/      # FastAPI serving layer
├── scripts/          # Convenience command‑line scripts
├── tests/            # Automated test suite
├── checkpoints/      # Model checkpoints
├── logs/             # Training logs
├── reports/          # Experiment reports
├── README.md
├── pyproject.toml
├── environment.yml
├── .gitignore
└── LICENSE
```

## Getting Started
```bash
# Create a virtual environment and install dependencies
conda env create -f environment.yml
conda activate code-review-llm

# Install the package in editable mode
pip install -e .
```

See the `scripts/` directory for typical workflows.

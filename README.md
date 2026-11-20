# CodeReview-LLM

A Qwen-based LLM fine-tuning project for Python code review,
bug localization, automated code repair, and test-based validation.

## 1. Project Overview

CodeReview-LLM aims to build a specialized Python code review
and automated bug-fixing model based on Qwen2.5-Coder-7B-Instruct.

The project explores a complete LLM post-training pipeline:

- Python bug-fixing dataset construction
- Supervised Fine-Tuning (SFT)
- LoRA / QLoRA fine-tuning
- Direct Preference Optimization (DPO)
- Automated code repair evaluation
- Sandboxed Python test execution
- FastAPI inference service
- ResearchOps Agent integration

## 2. Development Status

Current stage: Phase 1 - Project Initialization.

Completed:
- Project directory structure
- Git repository initialization
- GitHub remote configuration
- Python package structure
- Editable package installation
- Conda environment preparation
- MS-SWIFT dependency compatibility inspection
- Basic pytest tests
- Ruff code quality checks

Not yet implemented:
- Bug-fixing dataset pipeline
- Base model baseline evaluation
- SFT training
- DPO training
- Automated repair benchmark
- Production inference API

No training results or model improvements are claimed at this stage.

## 3. Base Model

Model: Qwen2.5-Coder-7B-Instruct

Current server model location:

\`\`\`text
/usst906disk/lrx/models/Qwen2.5-Coder-7B-Instruct
\`\`\`

The model is stored outside this Git repository.
Model weights are not committed to GitHub.

## 4. Technology Stack

| Component | Version |
|---|---|
| Python | 3.12.16 |
| PyTorch | 2.11.0+cu130 |
| CUDA Runtime | 13.0 |
| MS-SWIFT | 4.6.1 |
| Transformers | 5.22.2 |
| PEFT | 0.20.0 |
| TRL | 0.29.1 |
| Datasets | 4.8.4 |
| Accelerate | 1.16.0 |
| FastAPI | 0.165.0 |
| Pytest | 9.2.0 |

Hardware: NVIDIA RTX PRO 6000 Blackwell Workstation Edition.

## 5. Project Structure

\`\`\`text
code-review-llm/
├── configs/
│   ├── data.yaml
│   ├── sft.yaml
│   ├── dpo.yaml
│   ├── evaluation.yaml
│   └── serving.yaml
│
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   ├── manifests/
│   ├── splits/
│   ├── sft/
│   └── dpo/
│
├── requirements/
│   ├── base.txt
│   ├── torch-cu130.txt
│   ├── training.txt
│   ├── serving.txt
│   └── development.txt
│
├── src/
│   └── code_review_llm/
│       ├── data/
│       ├── models/
│       ├── train/
│       ├── preference/
│       ├── evaluation/
│       ├── sandbox/
│       └── serving/
│
├── tests/
├── scripts/
├── checkpoints/
├── logs/
├── reports/
│
├── environment.yml
├── pyproject.toml
├── README.md
├── LICENSE
└── .gitignore
\`\`\`

## 6. Environment Setup

### Create Conda Environment

\`\`\`bash
conda env create -f environment.yml
conda activate llm
\`\`\`

### Install Project Dependencies

\`\`\`bash
pip install -r requirements/development.txt
\`\`\`

### Install Project Package

\`\`\`bash
pip install -e .
\`\`\`

Note: The existing development environment has already been
prepared and validated. Avoid reinstalling PyTorch unnecessarily.

## 7. Development Checks

Run automated tests:

\`\`\`bash
pytest -v
\`\`\`

Run code quality checks:

\`\`\`bash
ruff check src tests
\`\`\`

Check Python dependencies:

\`\`\`bash
python -m pip check
\`\`\`

## 8. Experiment Management

Each experiment should record:

- Model and tokenizer versions
- Dataset version and split
- Training configuration
- Random seed
- Training and validation loss
- Evaluation metrics
- Checkpoint path
- Experiment logs

All reported performance improvements must be supported
by actual evaluation results.

## 9. Git Workflow

- main: stable project versions
- dev: active development

Feature development and experiments should be performed
on development branches before merging into main.

Large model weights, datasets, checkpoints, and training
logs should not be committed to Git.

## 10. Project Roadmap

1. Project initialization and environment validation
2. Python bug-fixing dataset construction
3. Base model baseline evaluation
4. SFT with LoRA
5. DPO preference optimization
6. Automated code repair evaluation
7. FastAPI inference deployment
8. ResearchOps Agent integration


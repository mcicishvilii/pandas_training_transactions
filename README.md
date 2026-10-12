# Automated Risk Analysis & Financial Pipeline

An enterprise-grade, modular Python pipeline built with **Pandas** and **NumPy** designed to ingest multi-source financial data, perform robust feature engineering, execute vectorized conditional risk scoring, and export executive-ready reports.

---

## Architectural Overview

This project transitions messy prototype notebooks into a structured, production-ready software architecture:
- **Modular Design**: Clear separation of concerns utilizing dedicated modules for configuration constants, data ingestion/schema cleanup (`schema_cleanup`), feature engineering & sliding-window metrics (`windowing_and_feature_engineering`), and risk evaluation.
- **Robust Imputation**: Implements a cascading fallback ladder (Dual-Group median $\rightarrow$ Global median) to handle missing income values in niche demographic segments without data loss.
- **Vectorized Performance**: Leverages NumPy and Pandas vectorized operations for high-speed conditional risk classification across tens of thousands of transaction records.

---

## Project Structure

```text
pandas_training/
│
├── constants/
│   └── constants.py          # Centralized path configurations and global variables
├── features/
│   ├── open_file.py          # Universal data loading and normalization utilities
│   ├── schema_cleanup.py     # Applicant deduplication and fallback-ladder income imputation
│   └── windowing_and_feature_engineering.py # Sliding rearview window metrics & transaction features
│   └── risk_scoring.py       # Left-join assembly and vectorized risk tier classification
│
├── data/                     # Raw datasets (Applications, Bureau Scores, Transaction Ledger)
├── main.py                   # Orchestration entry point
└── requirements.txt          # Project dependencies
```

---

## Getting Started & Installation

Follow these steps to clone and run the pipeline locally on your machine.

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Set Up a Virtual Environment
It is recommended to run the pipeline inside an isolated virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows PowerShell)
.\venv\Scripts\Activate

# Activate virtual environment (Mac/Linux)
source venv/bin/activate
```

### 3. Install Dependencies
Install the required packages (`pandas`, `numpy`, `openpyxl`, etc.):
```bash
pip install -r requirements.txt
```

---

## Running the Pipeline

Execute the orchestrator script from the root directory to run ingestion, feature engineering, joining, and risk modeling:

```bash
python main.py
```

---

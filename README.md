# Sustainability_SLMs_Study

This repository contains the full replication package for the empirical study:

**“An Empirical Study of Sustainability in Prompt-driven Test Script Generation using Small Language Models (SLMs)”**

The study evaluates sustainability–performance trade-offs in unit test script generation using Small Language Models (2B–8B), under structured prompt variants (APV0–APV3), with energy and carbon tracking using CodeCarbon.

---

# Study Overview

We evaluate:

• 5 Small Language Models (SLMs)  
• 4 Prompt Variants (APV0–APV3)  
• Multiple runs per prompt  
• 8-bit baseline + 4-bit + Full precision comparisons  
• Energy, Carbon Emission, Runtime, Coverage  
• Sustainability metrics (SCI, SCI_NORM, Time_NORM, SBI/ECO, SVI)

Benchmark:
HumanEval dataset (164 Python programming tasks)

Official HumanEval repository:
https://github.com/openai/human-eval

---
Sustainability_SLMs_Study/
│
├── Code_File/
│ └── Llama_model.ipynb
│
├── Generated results emission and test scripts/
│ ├── Llama/
│ ├── Mistral/
│ ├── Phi/
│ ├── Qwen/
│ └── Deepseek/
│
├── HumanEval_Code_Test_Dataset/
│ ├── HumanEval_0_code.py
│ ├── HumanEval_0_test.py
│ ├── ...
│
├── Prompts/
│ ├── APV0.pdf
│ ├── APV1.pdf
│ ├── APV2.pdf
│ └── APV3.pdf
│
├── Test Coverage/
│ ├── Deepseek 8bit/
│ ├── Llama 8bit/
│ ├── Mistral 8bit/
│ ├── Phi 8bit/
│ ├── Qwen 8bit/
│ ├── coverage_report_*.txt
│
├── Master_Sheet_For_All_Metrics_Calculation.xlsx
│
├── Anthropic_Prompt_Structure_Image.png
│
└── README.md


---

# 🤖 Models Evaluated

- deepseek-coder-7b-instruct-v1.5
- Meta-Llama-3-8B-Instruct
- Mistral-7B-Instruct
- Phi-3.5-mini
- Qwen2.5-1.5B-Instruct

All experiments use 8-bit quantization as baseline unless explicitly changed.

---

# 🧠 Prompt Variants

Located in `/Prompts/`:

- APV0 – Minimal instruction
- APV1 – Structured instruction
- APV2 – More constrained version
- APV3 – Fully structured with rules and examples

Prompt design follows Anthropic structured prompting principles.

---

# 🧪 How to Run the Experiments

All experiments are controlled via: Code_File/Llama_model.ipynb


This notebook implements the complete experimental pipeline for:

- Loading Small Language Models (SLMs)
- Applying Prompt Variants (APV0–APV3)
- Generating unit test scripts for HumanEval
- Tracking energy and carbon emissions using CodeCarbon
- Recording runtime and setup cost
- Saving generated tests and emissions logs

---

## 🔁 Experimental Workflow

Each execution of the notebook performs the following steps:

1. Install required dependencies
2. Mount Google Drive (if using Colab)
3. Load HumanEval dataset modules
4. Authenticate HuggingFace (for gated models)
5. Load selected SLM model
6. Apply selected prompt variant (APV0–APV3)
7. Generate unit test scripts (batch-wise)
8. Track:
   - Energy (kWh)
   - Carbon emissions (gCO₂eq)
   - Runtime (seconds)
   - Setup cost (model loading)
9. Save results in structured folders

---

## ⚙ Model Selection

To switch models, only modify:

```python
MODEL_ID  = "model-name"
MODEL_TAG = "ModelLabel"

**No other change in the pipeline is required.**

Supported models:

deepseek-coder-7b-instruct-v1.5

Meta-Llama-3-8B-Instruct

Mistral-7B-Instruct

Phi-3.5-mini

Qwen2.5-1.5B-Instruct


# 📂 Repository Structure
🧠 Prompt Selection

Each prompt block defines:

PROMPT_NAME = "APV0"

Available prompt variants:

APV0

APV1

APV2

APV3

Prompt PDFs are stored in:

Prompts/
🔁 Run Configuration

Current setup:

APV0 → RUNS = 3

APV1 → RUNS = 1

APV2 → RUNS = 1

APV3 → RUNS = 1

This can be modified by updating:

RUNS = X
⚡ Quantization Settings
Default (8-bit Baseline)
load_in_8bit=True
Switch to 4-bit

Replace with:

load_in_4bit=True
bnb_4bit_quant_type="nf4"
bnb_4bit_use_double_quant=True
Full Precision (No Quantization)

Remove quantization configuration entirely:

AutoModelForCausalLM.from_pretrained(MODEL_ID)
📊 Output Directory Structure

Results are saved as:

Generated results emission and test scripts/
   └── ModelName/
        └── APVx/
             └── run_k/
                  ├── tests/
                  ├── emissions_csv/
                  ├── runtime_csv/
                  ├── setup_cost_csv/
                  └── summary/

Each run folder contains:

Generated unit tests

CodeCarbon emission logs

Runtime tracking

Setup cost logs

🧪 Dataset

HumanEval benchmark (164 tasks):

Official source:
https://github.com/openai/human-eval

Runnable Python modules included in:

HumanEval_Code_Test_Dataset/

Each problem includes:

HumanEval_i_code.py

HumanEval_i_test.py


---

# 🔹Master Excel Sheet Explanation 

```markdown
# 📊 Master Excel Sheet Explanation

All sustainability metrics used in the paper are computed in:


This Excel file ensures full transparency and reproducibility of metric calculations.

It contains structured sheets as described below.

---

# 📄 Sheet 1 — Master Sheet

This is the main computation sheet.

It aggregates raw and averaged values for:

- Carbon Emission (gCO₂eq)
- Energy Consumption (kWh)
- Coverage (%) — used as quality metric
- Time Duration (seconds)

From these raw metrics, the following are calculated:

### 1️⃣ SCI (Software Carbon Intensity)
Carbon emission adjusted for grid intensity.

### 2️⃣ SCI_NORM
Min–max normalization of SCI across runs.

### 3️⃣ Time_NORM
Min–max normalization of runtime.

### 4️⃣ SBI_ECO
Eco-efficiency score combining normalized SCI and coverage.

### 5️⃣ SVI
Sustainability metric combining:
- SCI_NORM
- Time_NORM

All normalization and composite metrics are computed directly within this sheet.

---

# 📄 Sheet 2 — SCI (Region-Sensitive Analysis)

This sheet includes:

- country_iso_code (region of execution)
- Grid carbon intensity
- Per-run SCI values
- Region-dependent sustainability comparison

Since Google Colab may migrate execution to different data centers, grid intensity varies.

This sheet ensures:

- Region-aware transparency
- Fair sustainability comparison
- Reproducibility of carbon intensity adjustments

---

# 📄 Sheet 3 — Coverage Comparison

This sheet provides:

- Coverage comparison across models
- Coverage comparison across APV0–APV3
- Quantization comparison (8bit vs 4bit vs noQuant)

This allows direct evaluation of:

- Quality retention
- Prompt effectiveness
- Quantization impact on coverage

---

# 📄 Sheet 4 — Grid Intensity Reference

Contains:

- Region names
- Grid power intensity values
- Used for SCI computation

This ensures that carbon intensity values are explicitly documented.

---

# 🔎 Why This Excel Sheet Is Important

All sustainability conclusions in the paper are derived from:

- Raw CodeCarbon outputs
- Coverage results
- Runtime logs

The Excel sheet:

- Aggregates all runs
- Performs normalization
- Computes composite sustainability metrics
- Enables transparent verification

Anyone can recompute SCI, SCI_NORM, SBI_ECO, and SVI using the provided values.


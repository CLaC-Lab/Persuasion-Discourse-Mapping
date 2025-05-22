# Persuasion-Discourse Mapping

## 1. Introduction

This repository accompanies the paper *"On the Influence of Rhetorical Relations in Persuasive Texts"*. It provides a complete framework for analyzing the relationship between persuasion techniques (PTs) and discourse relations (DRs) using large language models (LLMs). This includes tools for classifying, evaluating, and performing statistical analysis. PT annotations are masked to preserve dataset integrity.
## 2. Overview of the Repository

### 2.1 Repository Structure

```
Persuasion-Discourse-Mapping/
├── dataset/                     # Masked PT dataset and DR test set extracted from the PDTB v3 manual
├── results/                     # DR predictions, evaluations, and visualizations
│   ├── stage1_eval_initial_DR_prompts_126instances/      # Evaluation results for classifiers; used to identify top 9 classifiers for ensemble methods
│   ├── stage2_DR_parsing_of_PT_annotated_semeval_datasets/ # DR-annotated PT datasets; includes 5 silver datasets under '03_pooled_datasets'
│   └── stage3_statistical_analysis/                       # Statistical results including significant PT–DR pairs using Fisher's test and OR
├── src/
│   ├── prompts/                 # Prompt templates
│   ├── utils/                   # Helper functions
│   ├── statistics_module/       # Analysis tools
│   └── config.py                # Configuration
├── requirements.txt
└── README.md
```

### 2.2 Argument Flags

```python
--preprocess             # Converts the DR test set CSV into a JSON format to prepare it for parsing
--parseDR                # Runs LLM-based DR classification on the PDTB test dataset using the selected model and prompt
--evaluateDRParsers      # Evaluates DR predictions: reports macro F1, prediction consistency across runs, and hallucination rate
--parsePTForDR           # Uses the selected classifier in config.py to annotate the dataset located at dataset/02_processed_data/persuasion_techniques/PT_dataset_A.json
--poolDatasets           # Applies majority voting (from 5 to 9 classifiers) to produce silver datasets based on agreement levels
--performStatistics      # Conducts statistical analysis using Fisher’s exact test, odds ratio, and computes PPMI across silver datasets
```

### 2.3 Models Supported

| ID | Model Name        | Prompt Handler          |
|----|-------------------|-------------------------|
| 1  | GPT-4o            | `gpt_prompt_handler`    |
| 2  | Gemini (1.5/2.0)  | `gemini_prompt_handler` |
| 3  | Claude 3.5 Sonnet | `claude_prompt_handler` |

### 2.4 Configuration File

All behavior is driven by `src/config.py`, including:

- API keys for LLMs
- Prompt name (`PROMPT_KEY`)
- Parser ID (1, 2, or 3)
- PT dataset name
- Batch size and delays for API calls

### 2.5 Prompt Templates

Prompts are stored in `src/prompts/` as `.txt` files. The prompt name in the config should match the filename (without `.txt`).

### 2.6 Results Folder

- `stage1_eval_initial_DR_prompts_126instances/`: DR evaluation results and predictions
- `stage2_DR_parsing_of_PT_annotated_semeval_datasets/`: DR-annotated PT datasets
- `stage3_statistical_analysis/`: Statistical summaries and visualizations (PPMI, Fisher, etc.)

## 3. User Workflows

### 3.1 Evaluate New Prompts

1. Add your `.txt` prompt to `src/prompts/`. It is recommended that you follow naming consistency (e.g., if the last file was `promptN10.txt`, use `promptN11.txt`).
2. In `config.py`, set:
   ```python
   PROMPT_KEY = 'promptN11'
   PARSER_ID = 1 #choose 1, 2 or 3 based on the desired LLM
   # Then choose the desired model version under 'Model Name'
   ```
3. Run the parser:
   ```bash
   python src/main.py --parseDR
   ```
4. Re-run the parser with a second trial. To do so, go to `src/DR_parsers/PDTB_DR_parser_with_LMM.py` and change line 16 from `t1` to `t2`.
5. Run evaluation:
   ```bash
   python src/main.py --evaluateDRParsers
   ```
   Results will be saved under:
   `results/stage1_eval_initial_DR_prompts_126instances/json_DR_level2_predictions/`, with filenames like:
   `promptN11_gemini-1.5-pro-t1.json`

**Note:** If an error occurs, it may be due to hallucinated outputs. You should manually examine the 126 predictions and remove or fix any malformed entries.

### 3.2 Annotate Dataset with DRs

1. Add your JSON dataset to:
   ```
   dataset/02_processed_data/persuasion_techniques/
   ```
2. Update `config.py`:
   ```python
   PT_DATASET = 'your_dataset_name'
   PROMPT_KEY = 'your_prompt_key'
   PARSER_ID = 1 | 2 | 3
   BATCH_SIZE = 40
   API_CALL_DELAY_SEC = 3
   RUN_DELAY_SEC = 50
   ```
3. Run the parser:
   ```bash
   python src/main.py --parsePTForDR
   ```
   Output will be saved in:
   `results/stage2_DR_parsing_of_PT_annotated_semeval_datasets/01_with_hallucination/`

## 4. Citation

> Turk, N., Kaspar, S., & Kosseim, L. (2025). *On the Influence of Rhetorical Relations in Persuasive Texts*. Canadian AI 2025. [Link to paper (to be added)]

import os
import json
from collections import Counter
import pandas as pd

def save_pt_and_dr_pivot_tables():
    """
    Generate and save pivot tables for Persuasion Techniques (PT) and Discourse Relations (DR).

    - Loads JSON datasets from a predefined directory.
    - Counts occurrences of each PT and DR.
    - Creates pivot tables summarizing these counts.
    - Saves the pivot tables as Excel files in the same directory.

    No input arguments required.
    """

    print('run save_pt_and_dr_pivot_tables')
    """
    Iterate through all datasets, compute counts for PTs and DRs,
    and save them as separate pivoted Excel files.
    """
    base_path = "../results/stage2_DR_parsing_of_PT_annotated_semeval_datasets/03_pooled_datasets"
    pt_output_path = os.path.join(base_path, 'PT_Pivot_Table.xlsx')
    dr_output_path = os.path.join(base_path, 'DR_Pivot_Table.xlsx')

    pooled_files = [file for file in os.listdir(base_path) if file.endswith('.json')]
    if not pooled_files:
        print(f"No JSON files found in {base_path}. Exiting.")
        return

    summary_data = []

    for pooled_file in pooled_files:
        file_path = os.path.join(base_path, pooled_file)
        with open(file_path, 'r', encoding='utf-8') as f:
            dataset = json.load(f)

        PT_count = Counter(item["PT"] for item in dataset.values())
        DR_count = Counter(item["DR"] for item in dataset.values())

        for pt, pt_count in PT_count.items():
            summary_data.append({'file_name': pooled_file, 'type': 'PT', 'label': pt, 'count': pt_count})
        for dr, dr_count in DR_count.items():
            summary_data.append({'file_name': pooled_file, 'type': 'DR', 'label': dr, 'count': dr_count})

    df = pd.DataFrame(summary_data)

    pt_pivot = df[df['type'] == 'PT'].pivot_table(
        index='label', columns='file_name', values='count', aggfunc='sum', fill_value=0
    )
    dr_pivot = df[df['type'] == 'DR'].pivot_table(
        index='label', columns='file_name', values='count', aggfunc='sum', fill_value=0
    )

    pt_pivot.to_excel(pt_output_path)
    dr_pivot.to_excel(dr_output_path)

    print(f"PT pivot table saved to {pt_output_path}")
    print(f"DR pivot table saved to {dr_output_path}")

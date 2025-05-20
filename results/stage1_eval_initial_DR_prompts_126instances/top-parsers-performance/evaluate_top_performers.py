import json
import os
from collections import defaultdict
from sklearn.metrics import f1_score

# Create f1_results directory if it doesn't exist
f1_results_dir = 'f1_results'
os.makedirs(f1_results_dir, exist_ok=True)

# Dictionaries to store both summaries
summary_1 = {}  # Basic F1 summary
summary_2 = {}  # Extended summary with relation stats

# Process each trial
for trial in [1, 2]:
    # Get list of pooled dataset files for this trial
    pooled_files = [f for f in os.listdir('pooled_results') 
                    if f.startswith('pooled_agreement') and f.endswith(f't{trial}.json')]

    print(f"\nProcessing trial {trial} files:", pooled_files)

    # Process each agreement level file
    for file_path in sorted(pooled_files):
        # Load the JSON data
        with open(os.path.join('pooled_results', file_path), 'r') as f:
            data = json.load(f)
        
        # Extract agreement level from filename
        agreement_level = int(file_path.split('_')[2])
        
        # Initialize in both summaries if not exists
        if agreement_level not in summary_1:
            summary_1[agreement_level] = {
                'agreement_level': agreement_level,
                'trial1_f1': None,
                'trial1_size': None,
                'trial2_f1': None,
                'trial2_size': None,
                'average_f1': None
            }
            
        if agreement_level not in summary_2:
            summary_2[agreement_level] = {
                'agreement_level': agreement_level,
                'trial1_f1': None,
                'trial1_size': None,
                'trial2_f1': None,
                'trial2_size': None,
                'average_f1': None,
                'trial1': [],
                'trial2': []
            }
        
        # Calculate F1 score
        y_true = []
        y_pred = []
        for instance in data:
            y_true.append(instance['actual_DR_level2'])
            y_pred.append(instance['ensemble_prediction'])
        f1 = f1_score(y_true, y_pred, average='macro')
        
        # Update F1 and size in both summaries
        for summary in [summary_1, summary_2]:
            summary[agreement_level][f'trial{trial}_f1'] = round(f1, 3)
            summary[agreement_level][f'trial{trial}_size'] = len(data)
        
        # For summary 2, add relation stats
        relation_stats = defaultdict(lambda: {'count': 0, 'correct': 0})
        
        for instance in data:
            actual_dr = instance['actual_DR_level2']
            predicted_dr = instance['ensemble_prediction']
            
            relation_stats[actual_dr]['count'] += 1
            if actual_dr == predicted_dr:
                relation_stats[actual_dr]['correct'] += 1
        
        # Create list of tuples for sorting
        relation_data = []
        for sense, stats in relation_stats.items():
            accuracy = f"{int(round((stats['correct'] / stats['count'] * 100), 0))}%" if stats['count'] > 0 else "0%"
            relation_data.append((sense, accuracy, stats['count']))
        
        # Sort by count
        relation_data.sort(key=lambda x: x[2], reverse=True)
        
        # Convert to formatted strings after sorting
        relation_strings = [f"{sense}-{acc}-{count}" for sense, acc, count in relation_data]
                
        # Update summary 2 with relation stats
        summary_2[agreement_level][f'trial{trial}'] = relation_strings

# Calculate average F1 for each agreement level in both summaries
for agreement_level in summary_1:
    for summary in [summary_1, summary_2]:
        t1_f1 = summary[agreement_level]['trial1_f1']
        t2_f1 = summary[agreement_level]['trial2_f1']
        if t1_f1 is not None and t2_f1 is not None:
            summary[agreement_level]['average_f1'] = round((t1_f1 + t2_f1) / 2, 3)

# Save both summaries
with open(os.path.join(f1_results_dir, 'summary_agreement_f1.json'), 'w') as f:
    json.dump(summary_1, f, indent=2)

with open(os.path.join(f1_results_dir, 'summary_2.json'), 'w') as f:
    json.dump(summary_2, f, indent=2)

print("\nBoth summaries created!")
print("Summary 1 (basic F1):", os.path.join(f1_results_dir, 'summary_agreement_f1.json'))
print("Summary 2 (with relation stats):", os.path.join(f1_results_dir, 'summary_2.json'))
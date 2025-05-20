import json
import os
import pandas as pd
from collections import Counter

# Directory containing the prediction files
directory = "./"  # Change this to your directory path

# Get all t1 files
t1_files = []
for filename in os.listdir(directory):
    if filename.endswith('t2.json'):
        t1_files.append(filename)

# Dictionary to store all predictions
all_instances = {}

# Load all t1 files and collect predictions
for filename in t1_files:
    model_name = filename.split('.')[0]  # Get model name without extension
    filepath = os.path.join(directory, filename)
    
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            
            # Process each instance in the file
            for instance_id, instance_data in data.items():
                if instance_id not in all_instances:
                    all_instances[instance_id] = {
                        "text": instance_data.get("text", ""),
                        "actual_DR_level1": instance_data.get("actual_DR_level1", ""),
                        "actual_DR_level2": instance_data.get("actual_DR_level2", ""),
                        "predictions": {}
                    }
                
                # Add this model's prediction to the instance
                all_instances[instance_id]["predictions"][model_name] = instance_data.get("predicted_DR_level2", "")
    except Exception as e:
        print(f"Error loading {filename}: {e}")

# Create ensemble datasets with different agreement thresholds
for agreement_threshold in range(5, 10):  # 5 to 9 agreement levels
    ensemble_dataset = []
    
    for instance_id, instance_data in all_instances.items():
        predictions = instance_data["predictions"].values()
        prediction_counts = Counter(predictions)
        
        # Only proceed if we have predictions
        if prediction_counts:
            # Get most common prediction and its count
            most_common_pred, most_common_count = prediction_counts.most_common(1)[0]
            
            # Check if it meets the threshold
            if most_common_count >= agreement_threshold:
                entry = {
                    "instance_id": instance_id,
                    "text": instance_data["text"],
                    "actual_DR_level1": instance_data["actual_DR_level1"],
                    "actual_DR_level2": instance_data["actual_DR_level2"],
                    "ensemble_prediction": most_common_pred,
                    "agreement_count": most_common_count,
                    "total_models": len(instance_data["predictions"])
                }
                ensemble_dataset.append(entry)
    
    # Save this ensemble dataset
    output_file = f"pooled_results/pooled_agreement_{agreement_threshold}_t2.json"
    with open(output_file, 'w') as f:
        json.dump(ensemble_dataset, f, indent=2)
    
    print(f"Silver-{agreement_threshold} dataset: {len(ensemble_dataset)} instances")

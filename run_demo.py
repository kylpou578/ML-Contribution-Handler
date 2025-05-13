import json
from validate_model import load_metrics, compare_metrics

# Simulated current vs previous metrics
current_metrics = {"accuracy": 0.89, "precision": 0.85, "recall": 0.88, "f1": 0.86}
previous_metrics = load_metrics("metrics/previous_metrics.json")

print("Evaluating model update...")
if compare_metrics(current_metrics, previous_metrics):
    print("✅ Update accepted: performance improved or maintained.")
else:
    print("❌ Update rejected: performance regression detected.")
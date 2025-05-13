import json

def load_metrics(path):
    with open(path, 'r') as f:
        return json.load(f)

def compare_metrics(current, previous):
    for key in current:
        if current[key] < previous.get(key, 0):
            return False
    return True

# For manual testing
if __name__ == '__main__':
    cur = load_metrics('metrics/current_metrics.json')
    prev = load_metrics('metrics/previous_metrics.json')
    print("Metrics valid:", compare_metrics(cur, prev))
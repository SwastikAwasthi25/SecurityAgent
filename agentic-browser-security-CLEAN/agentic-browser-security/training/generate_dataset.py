import json
import random
from pathlib import Path

# Output paths
BASE_DIR = Path(__file__).parent
DATASET_DIR = BASE_DIR / "dataset"
DATASET_DIR.mkdir(exist_ok=True)

TRAIN_FILE = DATASET_DIR / "guardian_train.jsonl"
VAL_FILE = DATASET_DIR / "guardian_val.jsonl"

# Simple synthetic samples based on your existing logic
SAMPLES = [
    {
        "input": "Hidden text saying ignore previous instructions detected in DOM.",
        "label": "BLOCK",
        "reason": "Hidden prompt injection"
    },
    {
        "input": "JavaScript dynamically injects new DOM nodes after page load.",
        "label": "WARN",
        "reason": "Dynamic DOM injection"
    },
    {
        "input": "Login form asking for credentials on unknown domain.",
        "label": "BLOCK",
        "reason": "Phishing attempt"
    },
    {
        "input": "Static informational page with no forms or scripts.",
        "label": "ALLOW",
        "reason": "No malicious signals"
    },
    {
        "input": "Multiple iframes and obfuscated scripts detected.",
        "label": "WARN",
        "reason": "Suspicious embedded content"
    }
]

def generate(n=200):
    data = []
    for _ in range(n):
        s = random.choice(SAMPLES)
        data.append({
            "prompt": s["input"],
            "response": f"Decision: {s['label']} | Reason: {s['reason']}"
        })
    return data

def write_files():
    data = generate()
    split = int(0.8 * len(data))
    train, val = data[:split], data[split:]

    with open(TRAIN_FILE, "w", encoding="utf-8") as f:
        for x in train:
            f.write(json.dumps(x) + "\n")

    with open(VAL_FILE, "w", encoding="utf-8") as f:
        for x in val:
            f.write(json.dumps(x) + "\n")

    print(f"[OK] Generated {len(train)} training samples")
    print(f"[OK] Generated {len(val)} validation samples")

if __name__ == "__main__":
    write_files()

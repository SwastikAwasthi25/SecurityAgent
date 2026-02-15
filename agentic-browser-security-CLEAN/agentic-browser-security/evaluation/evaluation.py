import os
from browser.controller import get_page
from sec_layer.dom_analyzer import (
    detect_hidden_text,
    detect_dynamic_dom_injection,
    detect_phishing_forms
)
from sec_layer.risk_engine import compute_risk


DATASET = {
    "benign": [
        "attacks/safe_page.html",
    ],
    "malicious": [
        "attacks/hidden_prompt.html",
        "attacks/dynamic_injection.html",
    ]
}


TP = FP = TN = FN = 0


def evaluate_page(file_path, label):
    global TP, FP, TN, FN

    url = "file:///" + os.path.abspath(file_path)
    page, browser, p = get_page(url)

    hidden = detect_hidden_text(page)
    dynamic = detect_dynamic_dom_injection(page)
    phishing = detect_phishing_forms(page)

    risk, _ = compute_risk(hidden, dynamic, phishing)
    detected = 1 if risk >= 40 else 0

    if detected == 1 and label == 1:
        TP += 1
    elif detected == 1 and label == 0:
        FP += 1
    elif detected == 0 and label == 0:
        TN += 1
    else:
        FN += 1

    browser.close()
    p.stop()


if __name__ == "__main__":
    for page in DATASET["benign"]:
        evaluate_page(page, label=0)

    for page in DATASET["malicious"]:
        evaluate_page(page, label=1)

    precision = TP / (TP + FP + 1e-6)
    recall = TP / (TP + FN + 1e-6)
    f1 = 2 * precision * recall / (precision + recall + 1e-6)

    print("\n=== EVALUATION RESULTS ===")
    print("TP:", TP, "FP:", FP, "TN:", TN, "FN:", FN)
    print("Precision:", round(precision, 2))
    print("Recall:", round(recall, 2))
    print("F1-score:", round(f1, 2))

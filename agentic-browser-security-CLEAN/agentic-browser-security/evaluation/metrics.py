from sklearn.metrics import classification_report, confusion_matrix
import json

def evaluate_model(model, dataset_path):
    y_true = []
    y_pred = []

    with open(dataset_path, "r") as f:
        for line in f:
            sample = json.loads(line)

            prompt = sample["prompt"]
            true_label = sample["response"].split(":")[1].strip().split("|")[0]

            output = model.generate(prompt)

            if "MALICIOUS" in output:
                pred = "MALICIOUS"
            else:
                pred = "BENIGN"

            y_true.append(true_label)
            y_pred.append(pred)

    print("\nClassification Report:\n")
    print(classification_report(y_true, y_pred))

    print("\nConfusion Matrix:\n")
    print(confusion_matrix(y_true, y_pred))

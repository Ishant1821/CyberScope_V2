import numpy as np
import time
import json
import os
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from sklearn.neighbors import LocalOutlierFactor
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

print("Generating 7D extreme stealth anomalies (Hard Mode)...")

# 7D Normal data
normal_data = np.random.normal(
    loc=[30.0, 3.3, 20.0, 240.0, 0.2, 0.0, 30.0], 
    scale=[1.5, 0.1, 5.0, 15.0, 0.1, 0.01, 10.0], 
    size=(10000, 7)
)
# 7D Threat payload data
anomaly_data = np.random.normal(
    loc=[33.5, 3.5, 85.0, 40.0, 25.0, 8.0, 600.0], 
    scale=[1.0, 0.1, 2.0, 5.0, 5.0, 1.0, 50.0], 
    size=(500, 7)
)

X_test = np.vstack([normal_data, anomaly_data])
y_true = np.append(np.ones(10000), np.full(500, -1))

models = {
    "Isolation Forest": IsolationForest(contamination=0.04, random_state=42),
    "One-Class SVM": OneClassSVM(nu=0.03, kernel="rbf", gamma=0.1),
    "Local Outlier Factor": LocalOutlierFactor(novelty=True, contamination=0.05)
}

results = {}
for name, clf in models.items():
    start_time = time.time()
    clf.fit(normal_data)
    y_pred = clf.predict(X_test)
    end_time = time.time()
    
    prec = precision_score(y_true, y_pred, pos_label=-1, zero_division=0)
    rec = recall_score(y_true, y_pred, pos_label=-1, zero_division=0)
    f1 = f1_score(y_true, y_pred, pos_label=-1, zero_division=0)
    acc = accuracy_score(y_true, y_pred)
    
    total_time = round(end_time - start_time, 4)
    latency_per_sample = round(((end_time - start_time) / len(X_test)) * 1000, 5)
    false_positives = int(np.sum((y_pred == -1) & (y_true == 1)))
    detection_rate = round(rec * 100, 2)
    
    results[name] = {
        "detection_rate": detection_rate,
        "precision": round(prec * 100, 2),
        "recall": round(rec * 100, 2),
        "f1_score": round(f1 * 100, 2),
        "accuracy": round(acc * 100, 2),
        "false_positives": false_positives,
        "time_taken": total_time,
        "latency_ms": latency_per_sample
    }
    
    print(f"[{name}] Recall: {results[name]['recall']}% | Precision: {results[name]['precision']}% | F1: {results[name]['f1_score']}% | Latency: {latency_per_sample} ms/sample")

with open("benchmark_results.json", "w") as f:
    json.dump(results, f, indent=4)

print("\nBenchmark complete! 7D metrics written to benchmark_results.json.")
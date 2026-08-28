import joblib
import os
import numpy as np
from sklearn.ensemble import IsolationForest

os.makedirs('models', exist_ok=True)

# Generate 7D normal operational bounds
# Columns: Temp, Volt, CPU, Heap, Drop, Faults, Traffic
normal_data = np.random.normal(
    loc=[30.0, 3.3, 20.0, 240.0, 0.2, 0.0, 30.0], 
    scale=[3.0, 0.15, 5.0, 15.0, 0.1, 0.01, 10.0], 
    size=(500, 7)
)

clf = IsolationForest(contamination=0.05, random_state=42)
clf.fit(normal_data)

joblib.dump(clf, 'models/anomaly_model.pkl')
print("7-Dimensional Model retrained successfully for your current environment!")
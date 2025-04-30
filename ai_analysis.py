import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

print("🤖 AI Analysis starting...")

# Load data
df = pd.read_csv('system_data.csv')
df['Time Index'] = np.arange(len(df))

# Train model
X = df[['Time Index']]
y = df['CPU Usage (%)']
model = LinearRegression()
model.fit(X, y)

# Predict next 10 seconds
future_idx = np.arange(len(df), len(df)+10).reshape(-1, 1)
predictions = model.predict(future_idx)

print("\n📈 Predicted CPU Usage for next 10 seconds:")
for i, p in enumerate(predictions):
    print(f"Time +{i+1}s: {p:.2f}%")

# Optionally save predictions
pd.DataFrame({'Time+sec': np.arange(1,11), 'Predicted CPU Usage (%)': predictions}).to_csv("cpu_predictions.csv", index=False)

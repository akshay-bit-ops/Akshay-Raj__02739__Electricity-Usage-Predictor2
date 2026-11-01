import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load dataset
data = pd.read_csv("usage.csv")

# 2. Validate dataset
if not {"Month", "Units"}.issubset(data.columns):
    raise ValueError("CSV must contain Month and Units columns.")

data["Month"] = pd.to_numeric(data["Month"], errors="coerce")
data["Units"] = pd.to_numeric(data["Units"], errors="coerce")

data = data.dropna(subset=["Month", "Units"])

if len(data) < 2:
    raise ValueError("At least 2 months of data are required for prediction.")

x = data["Month"].to_numpy()
y = data["Units"].to_numpy()

if len(np.unique(x)) < 2:
    raise ValueError("At least 2 different months are required.")

# 3. Linear Regression
slope, intercept = np.polyfit(x, y, 1)

# 4. Calculate R-squared
predicted_y = slope * x + intercept
ss_res = np.sum((y - predicted_y) ** 2)
ss_tot = np.sum((y - np.mean(y)) ** 2)

r2 = 1 - (ss_res / ss_tot) if ss_tot != 0 else 1.0

print("\n--- Electricity Usage Predictor ---")
print(f"Slope: {slope:.2f}")
print(f"Intercept: {intercept:.2f}")
print(f"R2: {r2:.2f}")

# 5. Future prediction
try:
    month = int(input("\nEnter future month number: "))

    if month <= np.max(x):
        raise ValueError("Enter a month after the available data.")

    units = slope * month + intercept
    bill = units * 6

    print(f"Predicted Units: {units:.2f}")
    print(f"Estimated Bill: Rs. {bill:.2f}")

    # 6. Plot graph
    x_line = np.linspace(min(x), month, 100)
    y_line = slope * x_line + intercept

    plt.scatter(x, y, label="Actual Usage")
    plt.plot(x_line, y_line, color="red", label="Regression Line")
    plt.scatter(month, units, color="green", label="Future Prediction")

    plt.title("Electricity Usage Predictor")
    plt.xlabel("Month")
    plt.ylabel("Units Consumed")
    plt.legend()
    plt.grid(True)
    plt.show()

except ValueError as error:
    print("Error:", error)
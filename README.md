# Akshay-Raj__02739__Electricity-Usage-Predictor

⚡ Electricity Usage Predictor

Project No.: 62

A Python-based machine learning project that predicts future electricity consumption using Simple Linear Regression.

📌 About the Project

The Electricity Usage Predictor analyses historical monthly electricity consumption data and predicts electricity usage for a future month.

It also estimates the electricity bill using a fixed rate of ₹6 per unit and visualises the results through a graph.

✨ Key Features

- Reads electricity consumption data from a CSV file.
- Uses Pandas to load and process data.
- Uses NumPy for Simple Linear Regression.
- Predicts electricity consumption for a future month.
- Calculates the Slope and Intercept.
- Calculates the R² score to evaluate the model.
- Estimates the electricity bill at ₹6 per unit.
- Displays a graph of actual usage, regression line, and future prediction.
- Handles invalid and insufficient input data.

🛠️ Technologies Used

Technology| Purpose
Python| Main programming language
Pandas| CSV data handling
NumPy| Mathematical calculations and regression
Matplotlib| Data visualisation

📂 Project Structure

Electricity-Usage-Predictor2/
│
├── predictor.py
├── usage.csv
└── README.md

📊 Dataset

The project uses a CSV file named "usage.csv".

Sample dataset:

Month| Units
1| 100
2| 120
3| 150
4| 170

⚙️ Installation

First, install Python on your computer.

Install the required libraries using:

python -m pip install pandas numpy matplotlib

🚀 How to Run the Project

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

python predictor.py

5. Enter the future month number when prompted.
6. View the predicted electricity units, estimated bill, and graph.

🧮 Working Principle

The project uses Simple Linear Regression.

The mathematical equation is:

Y = mX + c

Where:

- Y = Predicted electricity units
- X = Month number
- m = Slope
- c = Intercept

The model calculates the best-fit straight line using NumPy's "polyfit()" function.

Electricity Bill Calculation

Estimated Bill = Predicted Units × ₹6

Model Evaluation

The R² score measures how well the regression line fits the historical data.

🧪 Assignment Test Cases

The project is designed to handle:

1. Normal input – Predict electricity usage using multiple months of data.
2. Minimum input – Handle the minimum requirement of two months.
3. Invalid input – Display an error when insufficient data is available.
4. Different valid data – Calculate regression values and future predictions.

⚠️ Limitations

- Predictions are based on historical electricity consumption.
- The model uses Simple Linear Regression.
- The electricity rate is fixed at ₹6 per unit for this assignment.
- Actual electricity bills may differ due to additional charges and tariff rules.

👨‍💻 Author

Akshay Raj

B.Tech – Computer Science and Engineering

Project No.: 62

---

⭐ If you find this project useful, feel free to explore the source code.

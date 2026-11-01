

# ⚡ Electricity Usage Predictor

### Python Programming Project

**Project Name:** Electricity Usage Predictor  
**Project ID:** 02739  
**Developed By:** Akshay Raj  
**Technology:** Python 3

---

## 📌 About the Project

Electricity Usage Predictor is a Python-based application designed to predict future electricity consumption using historical electricity usage data.

The project uses Linear Regression to analyze previous electricity consumption and estimate future electricity usage. It also calculates the estimated electricity bill based on predicted units.

The main purpose of this project is to demonstrate the practical application of Python, data analysis, mathematical calculations, and Machine Learning concepts.

## 🎯 Project Objectives

- Analyze historical electricity consumption.
- Predict future electricity usage.
- Implement Linear Regression.
- Calculate estimated electricity bills.
- Visualize electricity consumption patterns.
- Develop practical problem-solving skills using Python.

## ✨ Key Features

- CSV data loading and processing.
- Electricity consumption analysis.
- Linear Regression-based prediction.
- Automatic electricity bill estimation.
- Data visualization using graphs.
- Input validation and error handling.
- Console-based execution.
- Web application support using Flask.

## 🛠️ Technologies Used

| Technology | Application |
|---|---|
| Python 3 | Core programming |
| Pandas | Data processing |
| NumPy | Mathematical calculations |
| Matplotlib | Graph visualization |
| Flask | Web application |
| HTML | Web interface |

## ⚡ Electricity Bill Calculation

The project uses an assumed electricity rate of ₹6 per unit.

**Formula:**

Estimated Bill = Predicted Electricity Units × Rate Per Unit

Example:

- Predicted Units = 280
- Rate = ₹6 per unit
- Estimated Bill = ₹1,680

## 🧠 Machine Learning Concept

The project uses Linear Regression to predict electricity consumption.

The mathematical equation is:

```text
Y = mX + C
```

Where:

- Y = Predicted electricity usage
- X = Month number
- m = Slope
- C = Intercept

The model uses historical data to estimate future electricity consumption.

## 📂 Project Files

```text
Electricity-Usage-Predictor/
│
├── app.py
├── electricity_predictor.py
├── usage.csv
├── Demo.csv
├── Output.csv
├── requirements.txt
├── render.yaml
└── README.md
```

## 🚀 Installation and Execution

**1. Clone the repository**

```bash
git clone https://github.com/akshay-bit-ops/Akshay-Raj__02739__Electricity-Usage-Predictor2.git
```

**2. Open the project folder**

```bash
cd Akshay-Raj__02739__Electricity-Usage-Predictor2
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the Python program**

```bash
python electricity_predictor.py
```

**5. Run the Flask application**

```bash
python app.py
```

Open the local address displayed in the terminal to access the web application.

## 📚 Learning Outcomes

By developing this project, the following concepts can be understood:

1. Python programming.
2. Data analysis using Pandas.
3. Numerical operations using NumPy.
4. Linear Regression.
5. Data visualization.
6. CSV file handling.
7. Flask web development.
8. Problem-solving and logical thinking.

## ⚠️ Project Limitations

- Prediction accuracy depends on historical data.
- Sudden changes in electricity usage may affect predictions.
- The electricity rate is an assumed value and may differ from actual tariffs.
- Linear Regression may not capture every consumption pattern.

## 🏁 Conclusion

The Electricity Usage Predictor demonstrates how Python programming and Machine Learning concepts can be used to solve a real-world problem.

It provides an approach to analyzing electricity consumption, predicting future usage, and estimating electricity bills.

This project demonstrates the practical implementation of data analysis, mathematical calculations, and predictive modeling.

---

### Project Credits

**Project Title:** Electricity Usage Predictor  
**Project ID:** 02739  
**Developer:** Akshay Raj  
**GitHub:** akshay-bit-ops

⭐ If you find this project useful, feel free to explore the repository.

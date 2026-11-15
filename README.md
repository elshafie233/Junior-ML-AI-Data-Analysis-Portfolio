<div align="center">

# Junior ML , AI & Data Analysis Portfolio

### Python · Data Analysis · Machine Learning Fundamentals · Data Visualization

A growing collection of hands-on Python projects exploring real-world-style datasets, predictive modeling, statistical analysis, and data-driven visualizations.

[Explore Projects](#-projects) · [Tech Stack](#-tech-stack) · [Getting Started](#-getting-started) · [Roadmap](#-roadmap)

</div>

---

## 👋 About This Repository

This repository documents my practical learning journey in **data science and machine learning**. Rather than relying exclusively on prebuilt modeling APIs, some projects implement core algorithms directly with NumPy, while others focus on preparing, analyzing, and visualizing data with Pandas and Matplotlib.

The current portfolio contains **five Python projects**, ranging from sales analysis and anomaly detection to stock analytics and regression. It is a learning portfolio, not a collection of production-ready applications.

## 📂 Projects

| Project | What it does | Key concepts |
| --- | --- | --- |
| 🏠 **[Housing Price Prediction](./Hosuing%20Price%20Prediction/)** | Generates synthetic housing data and trains regression and classification models from scratch. | Feature engineering, normalization, gradient descent, linear regression, logistic regression, L2 regularization |
| 🛒 **[E-Commerce Market Analysis](./E-commerce%20market%20Analysis/)** | Combines sales and product data, calculates transaction revenue, labels high-value orders, and charts revenue by category. | Data cleaning, joins, NumPy, Pandas `groupby`, bar charts |
| 🚀 **[Interplanetary Delivery Analysis](./Solar%20Planet%20distances/)** | Simulates deliveries between fictional planets and analyzes costs, delivery times, and on-time performance. | Python OOP, synthetic data, aggregation, multi-panel visualization |
| 📈 **[Stock Market Analysis](./Stock%20Market%20Analyser/)** | Downloads historical stock prices and examines daily returns, volatility, and cumulative returns. | `yfinance`, time-series processing, financial statistics, charts |
| 🌡️ **[Weather Anomaly Analysis](./Weather%20Anomalies%20Analysis/)** | Simulates daily temperatures, flags extreme values using a three-standard-deviation threshold, and visualizes the results. | Synthetic time series, standard deviation, outlier detection, line/scatter plots |

### Project Highlights

#### 🏠 Housing Price Prediction

- Generates **200 simulated housing records** with features such as area, number of bedrooms, building age, and distance.
- Engineers additional features including squared size, size per bedroom, and squared age.
- Implements **linear regression and gradient descent from scratch** using NumPy.
- Implements **logistic regression** for a binary classification task: whether a property's simulated price is at least **350,000**.
- Includes an **L2-regularized linear regression** routine and a two-feature decision-boundary calculation.
- Saves a **gradient descent learning-curve** chart.

**Note:** The models use synthetic data; the script does not currently include a train/test split or out-of-sample evaluation.

#### 🛒 E-Commerce Market Analysis

- Reads sales and product CSV datasets and merges them using `Product_ID`.
- Computes transaction revenue as `Quantity × Price_Per_Unit`.
- Labels orders **High Value** when revenue exceeds **100**, otherwise **Normal Value**.
- Aggregates revenue by product category and saves a labeled bar chart to `total_revenue_by_category.png`.

**Note:** The provided script references absolute CSV paths from its original development workspace; adjust these paths to match your local checkout.

#### 🚀 Interplanetary Delivery Analysis

- Creates **200 simulated deliveries** using an object-oriented `delivery` class.
- Uses fictional planets, generated pilot names, distances, shipment weights, and simulated delivery outcomes.
- Computes a base delivery cost from distance and weight, then adds random noise.
- Summarizes routes and origin planets, and calculates the overall on-time delivery rate.
- Saves a four-panel visualization to `delivery_analysis.png`.

**Note:** This is a fictional logistics simulation, not an astronomy dataset or an operational delivery system.

#### 📈 Stock Market Analysis

- Fetches historical prices for **AAPL, MSFT, GOOG, and 005930.KS** using `yfinance`.
- Analyzes a date range from **January 1, 2025, to August 18, 2026** (the API end date is exclusive).
- Calculates **daily percentage returns**, **standard deviation of daily returns**, and **compounded total returns** for each ticker.
- Plots individual daily-return series and a volatility comparison.

**Note:** The script labels `total return / daily standard deviation` as a “Sharpe Ratio.” This is **not the conventional Sharpe ratio**, which uses return and risk-free rate over consistent periods. The script reports **per-asset statistics**, not an allocated or optimized portfolio.

#### 🌡️ Weather Anomaly Analysis

- Generates **1,000 days** of synthetic temperature observations beginning January 1, 2023.
- Adds seasonal variation, random noise, and a few deliberately extreme readings.
- Flags anomalies outside `mean ± 3 × standard deviation`.
- Saves the generated dataset as `Real_Weather.csv` and the visualization as `Weather_Anomalies_Dashboard.png`.

**Note:** Despite the CSV filename, these are **simulated**, not measured, weather observations.

## 🛠️ Tech Stack

| Area | Tools / methods |
| --- | --- |
| Programming | Python |
| Data manipulation | Pandas, NumPy |
| Visualization | Matplotlib |
| Financial data retrieval | yfinance |
| Machine learning fundamentals | Linear regression, logistic regression, gradient descent, regularization |
| Statistics | Mean, standard deviation, returns, outlier thresholds |
| Software fundamentals | Functions, classes, object-oriented programming |

> The regression implementations in this repository use **NumPy**, not scikit-learn, TensorFlow, or PyTorch. Those tools may be part of future projects but are not required by the five scripts currently documented here.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/elshafie233/Junior-ML-AI-Portfolio.git
cd Junior-ML-AI-Portfolio
```

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv .venv
```

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install numpy pandas matplotlib yfinance
```

### 4. Run a project

Open the relevant project folder and run its Python script:

```bash
python "your_script_name.py"
```

Some projects generate their own datasets; the **E-Commerce Market Analysis** project requires its sales and product CSV files. The **Stock Market Analysis** project needs an internet connection to fetch market prices. Some scripts open Matplotlib windows and save image files in the current working directory.

## 🧠 Skills Demonstrated

- **Data preparation:** missing-value handling, merging tables, feature transformation, and filtering.
- **Exploratory analysis:** grouping, aggregation, descriptive statistics, and comparisons.
- **Mathematical implementation:** writing loss, gradient, optimization, and prediction functions with NumPy.
- **Visualization:** time-series plots, scatter plots, distributions, and categorical comparisons.
- **Problem solving:** turning simple analytical questions into executable Python workflows.

## 🗺️ Roadmap

These are potential next steps, **not features currently implemented**:

- [ ] Add unit tests and reproducible environment files.
- [ ] Replace hard-coded file paths with portable relative paths.
- [ ] Add train/test splits and evaluation metrics for predictive models.
- [ ] Compare from-scratch models with scikit-learn implementations.
- [ ] Expand financial analysis with a correctly calculated Sharpe ratio and portfolio weights.
- [ ] Add more real datasets, model validation, and end-to-end ML projects.

## 📄 License

Licensed under the **MIT License**. See [LICENSE](./LICENSE).

## 🔗 Connect

**GitHub:** [@elshafie233](https://github.com/elshafie233)

---

<div align="center">

*Learning by building — one Python project at a time.*

</div>

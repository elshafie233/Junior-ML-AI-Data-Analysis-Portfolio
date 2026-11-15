# Weather Analyzer: Temperature Anomaly Detection

A Python data-analysis project that generates a **synthetic daily temperature dataset**, detects unusually high or low temperatures using the **three-sigma rule**, and visualizes the results in a time-series chart.

> **Note:** Although the script saves the dataset as `Real_Weather.csv`, the data is simulated rather than sourced from real weather observations.

## Features

- Creates 1,000 consecutive daily observations starting on January 1, 2023.
- Models seasonal temperature changes using a sine wave with added random noise.
- Inserts three deliberately extreme temperature values to test anomaly detection.
- Calculates the mean and standard deviation of all temperatures.
- Flags observations outside **mean ± 3 standard deviations** as anomalies.
- Plots daily temperatures and highlights detected anomalies in red.
- Exports both the generated CSV dataset and a high-resolution PNG chart.

## Tech Stack

- **Python**
- **Pandas** — date ranges, tabular data, and CSV I/O
- **NumPy** — synthetic data generation and statistical calculations
- **Matplotlib** — visualization and chart export

## Project Structure

```text
weather-analyzer/
├── Weather Analyzer.py
├── README.md
├── Real_Weather.csv                 # Generated when the script runs
└── Weather_Anomalies_Dashboard.png  # Generated when the script runs
```

## Installation

Make sure Python 3 is installed, then install the dependencies:

```bash
python -m pip install numpy pandas matplotlib
```

## Run the Project

From the project directory, run:

```bash
python "Weather Analyzer.py"
```

The script prints the number of anomalies detected, saves `Real_Weather.csv` and `Weather_Anomalies_Dashboard.png` in the current working directory, and displays the chart in a window (if graphical display is available).

## How It Works

### 1. Generate synthetic weather data

The script generates 1,000 dates and simulates temperatures with seasonal variation:

```python
temps = 24 + 10 * np.sin(np.arange(1000) * (2 * np.pi / 365)) + np.random.normal(0, 3, 1000)
```

- **24°C** is the baseline temperature.
- **10°C** is the seasonal oscillation amplitude.
- **365 days** is the assumed seasonal cycle.
- Random noise has a standard deviation of **3°C**.

The random seed is set to `10` for reproducibility. Three temperatures are explicitly overwritten with `47.8°C`, `-2.5°C`, and `49.1°C` at positions `150`, `450`, and `750`.

### 2. Compute anomaly thresholds

The script uses a standard-deviation-based rule:

\[
\text{Upper limit} = \mu + 3\sigma
\]

\[
\text{Lower limit} = \mu - 3\sigma
\]

Here, **μ** is the mean temperature and **σ** is the population standard deviation calculated by `np.std`.

A reading is marked as an anomaly when it falls **strictly above** the upper limit or **strictly below** the lower limit.

```python
anomalies = df[(df['Temp'] > upper_limit) | (df['Temp'] < lower_limit)]
```

### 3. Visualize results

The chart includes:

- A blue line showing daily temperatures over time.
- Red points marking detected anomalies.
- Axis labels, a legend, and a grid.

The plot is saved as `Weather_Anomalies_Dashboard.png` at **300 DPI**.

## Output Files

| File | Description |
| --- | --- |
| `Real_Weather.csv` | Generated dataset with `Date` and `Temp` columns. |
| `Weather_Anomalies_Dashboard.png` | Temperature time-series plot with detected outliers highlighted. |

## Limitations

- The dataset is **synthetic**, not a real weather feed.
- A global three-sigma threshold does not adjust for seasons or long-term trends.
- The three injected extreme values are test cases; whether each is flagged depends on the calculated thresholds.
- The script does not train a machine-learning model or forecast future temperatures.

## Possible Improvements

- Analyze real observations from a weather data source.
- Use rolling or seasonal anomaly thresholds.
- Report anomaly dates, values, and threshold limits in a CSV file.
- Add a command-line interface for input and output paths.
- Add automated tests and a requirements file.

## License

No license has been specified for this project.

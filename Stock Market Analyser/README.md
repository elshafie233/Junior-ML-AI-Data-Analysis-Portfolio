# Stock Market Portfolio Risk Analysis 📈

A Python project that downloads historical stock prices and explores **daily returns, volatility, and cumulative returns** for four major technology companies. It uses `yfinance` for market data, `pandas` for return calculations, and `matplotlib` to visualize the results.

> **Scope:** Despite the project title, the current script analyzes **individual stocks** rather than a weighted investment portfolio. It does not yet calculate portfolio-level volatility, diversification, or an industry-standard Sharpe ratio.

## Features

- Fetches historical closing prices directly from Yahoo Finance.
- Aligns available prices and forward-fills missing observations.
- Computes **daily percentage returns** for each stock.
- Estimates **daily-return volatility** using standard deviation.
- Calculates the **compounded return** over the observed data.
- Prints a return-to-volatility ratio (labeled `Sharpe Ratio` in the script; see note below).
- Plots daily returns for each selected ticker.
- Creates a bar chart comparing daily-return standard deviations.

## Stocks Analyzed

| Ticker | Company | Exchange / market |
| --- | --- | --- |
| `AAPL` | Apple | U.S. |
| `MSFT` | Microsoft | U.S. |
| `GOOG` | Alphabet (Class C) | U.S. |
| `005930.KS` | Samsung Electronics | South Korea |

**Date range requested:** January 1, 2025 through August 18, 2026 (`yfinance` treats the `end` date as exclusive). The exact returned observations depend on available market data, trading calendars, and download behavior.

## Tech Stack

- **Python 3**
- **yfinance** — stock market data retrieval
- **pandas** — data preparation and return calculations
- **NumPy** — imported by the script
- **Matplotlib** — visualization

## Installation

1. Clone or download the repository.
2. Install the required packages:

   ```bash
   pip install yfinance pandas numpy matplotlib
   ```

3. Run the script from your project directory:

   ```bash
   python "Stock Market Portfolio Risk.py"
   ```

An internet connection is required to download price data. If you rename the Python file, update the command accordingly.

## How It Works

### 1. Retrieve and prepare price data

```python
tickers = ['AAPL', 'MSFT', 'GOOG', '005930.KS']
raw_data = yf.download(tickers, start='2025-01-01', end='2026-08-18')
df = raw_data['Close']
df = df.ffill().dropna()
df = df.pct_change()
```

The script selects the downloaded closing-price series, fills missing values forward, drops rows that still contain missing prices, and converts prices to daily returns.

**Note:** Different stock exchanges have different trading holidays. Forward filling may produce a zero return on dates when a particular market was closed. The first row of `pct_change()` is also `NaN` because no earlier price is available.

### 2. Calculate daily returns

For stock price \(P_t\) on day \(t\):

\[
r_t = \frac{P_t - P_{t-1}}{P_{t-1}}
\]

`df.pct_change()` performs this calculation for each stock.

### 3. Measure volatility

```python
standard_deviation = df.std()
```

The standard deviation of daily returns measures how widely returns fluctuate. **Higher volatility** generally indicates larger day-to-day price swings; it does not by itself capture every kind of investment risk.

### 4. Calculate compounded total return

```python
Total_Return = (df + 1).prod() - 1
```

The calculation compounds observed daily returns:

\[
R_{\mathrm{total}} = \prod_{t=1}^{T} (1+r_t) - 1
\]

### 5. Calculate the script's return-to-volatility ratio

```python
sharp_ratio = Total_Return / standard_deviation
```

The original code prints this result as **`Sharpe Ratio`**, but **it is not a conventional Sharpe ratio**. It divides a *multi-period cumulative return* by a *daily standard deviation*, without subtracting a risk-free rate or matching measurement periods.

A conventional annualized Sharpe ratio is commonly estimated using a consistent return frequency:

\[
\mathrm{Sharpe} \approx \frac{\overline{r}_{\mathrm{daily}}-r_{f,\mathrm{daily}}}{\sigma_{\mathrm{daily}}}\sqrt{252}
\]

where \(r_f\) is the risk-free return at the same frequency and 252 is a commonly used approximation for annual U.S. trading days. Cross-market calendars require additional care.

## Visualizations

### Daily Returns of Selected Stocks

A line plot compares each ticker's daily return fluctuations throughout the period. The chart is displayed when the script runs.

### Standard Deviation of Daily Returns

A bar chart compares the daily-return standard deviations across the four tickers.

The script also calls:

```python
plt.savefig('standard_deviation.png')
```

**Important:** This call appears *after* `plt.show()`. Depending on the Matplotlib backend, the saved image may be blank or may not contain the intended chart. For a reliable export, move `plt.savefig(...)` to just **before** the second `plt.show()`.

## Project Structure

```text
Stock-Market-Portfolio-Risk/
├── Stock Market Portfolio Risk.py
├── README.md
└── standard_deviation.png    # Intended chart output; see savefig note
```

## Console Output

The script prints three per-stock series:

- `Standard Deviation of Daily Returns`
- `Total Return`
- `Sharpe Ratio` *(the script's unadjusted ratio, as noted above)*

Actual numerical values depend on the downloaded data and any data adjustments applied by the installed `yfinance` version.

## Current Limitations

- No portfolio weights or aggregate portfolio return/risk calculations.
- No covariance or correlation analysis for diversification.
- No train/test split or predictive model (this is descriptive analysis, not forecasting).
- No risk-free adjustment or properly matched frequency for the displayed `Sharpe Ratio`.
- No safeguards for failed downloads or changed upstream data formats.
- The bar chart export may not work reliably because `savefig()` follows `show()`.

## Possible Improvements

- Add configurable portfolio weights and portfolio-level returns.
- Estimate the covariance matrix and annualized portfolio volatility.
- Compute a correctly scaled Sharpe ratio using an appropriate risk-free rate.
- Add maximum drawdown and Value at Risk (VaR).
- Handle different stock-market calendars and currencies explicitly.
- Add correlation heatmaps and save plots before displaying them.
- Make tickers and dates configurable from the command line.

## Disclaimer

This project is for **educational and exploratory analysis only**. Its output is not investment advice, and past returns do not guarantee future performance.

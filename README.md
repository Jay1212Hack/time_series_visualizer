# 📈 Time Series Visualizer

This project is part of the freeCodeCamp Data Analysis with Python certification. The goal is to visualize time series data from the freeCodeCamp.org forum to observe patterns, trends, and seasonality in daily page views.

---

## 🗃 Dataset

The data is sourced from the `fcc-forum-pageviews.csv` file and contains daily page views from **2016-05-09** to **2019-12-03**.

### Columns:
| Column      | Description            |
|-------------|------------------------|
| `date`      | Date of the record     |
| `value`     | Number of page views   |

---

## 📊 Tasks & Visualizations

### ✅ Data Preparation
- Import data using Pandas and set `date` as the index.
- Clean the data by removing the top and bottom 2.5% of `value` data (outliers).

---

### 1. 📉 Line Plot
**Function:** `draw_line_plot()`

- Shows the daily page views over time.
- **Title:** `Daily freeCodeCamp Forum Page Views 5/2016-12/2019`
- **X-axis:** `Date`
- **Y-axis:** `Page Views`

---

### 2. 📊 Bar Plot
**Function:** `draw_bar_plot()`

- Displays average monthly page views grouped by year.
- **X-axis:** `Years`
- **Y-axis:** `Average Page Views`
- **Legend:** Months with a title `Months`

---

### 3. 📦 Box Plots
**Function:** `draw_box_plot()`

- Two box plots:
  - **Year-wise:** Distribution of views per year
  - **Month-wise:** Distribution of views per month across all years
- **Titles:**
  - `Year-wise Box Plot (Trend)`
  - `Month-wise Box Plot (Seasonality)`
- **X-axis:** Years or Months
- **Y-axis:** Page Views

---

## 🧑‍💻 Development

Work in the `time_series_visualizer.py` file. You can test your code using `main.py` which includes helper test and plot calls.

### Run the script
```bash
python main.py

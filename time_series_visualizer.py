import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# 1. Import the data
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# 2. Clean the data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

# Function 1: Draw Line Plot
def draw_line_plot():
    # Copy the data for the line plot
    df_copy = df.copy()

    # Create the figure and plot the line plot
    plt.figure(figsize=(12, 6))
    plt.plot(df_copy.index, df_copy['value'], color='tab:blue')

    # Set title and labels
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save and return the figure
    plt.tight_layout()
    plt.savefig('line_plot.png')
    return plt

# Function 2: Draw Bar Plot
def draw_bar_plot():
    # Create a new DataFrame for the bar plot
    df_copy = df.copy()

    # Extract year and month from the index
    df_copy['year'] = df_copy.index.year
    df_copy['month'] = df_copy.index.month

    # Group by year and month and get the mean of page views
    monthly_avg = df_copy.groupby(['year', 'month'])['value'].mean().unstack()

    # Create the figure and plot the bar plot
    plt.figure(figsize=(12, 6))
    monthly_avg.plot(kind='bar', ax=plt.gca(), width=0.8)

    # Set title and labels
    plt.title('Average Daily Page Views per Month (Grouped by Year)')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')

    # Save and return the figure
    plt.tight_layout()
    plt.savefig('bar_plot.png')
    return plt

# Function 3: Draw Box Plot
def draw_box_plot():
    # Create a new DataFrame for the box plot
    df_copy = df.copy()

    # Extract year and month from the index
    df_copy['year'] = df_copy.index.year
    df_copy['month'] = df_copy.index.month

    # Create the figure and axes for the box plots
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Year-wise Box Plot
    sns.boxplot(x='year', y='value', data=df_copy, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise Box Plot
    sns.boxplot(x='month', y='value', data=df_copy, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    # Save and return the figure
    plt.tight_layout()
    plt.savefig('box_plot.png')
    return plt
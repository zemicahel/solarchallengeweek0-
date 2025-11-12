import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(path):
    """Load cleaned CSV data."""
    df = pd.read_csv(path, parse_dates=["Timestamp"])
    return df

def boxplot_metric(df, metric):
    """Return a matplotlib figure of a boxplot for a metric."""
    fig, ax = plt.subplots(figsize=(8,5))
    sns.boxplot(x="Country", y=metric, data=df, ax=ax)
    ax.set_title(f"{metric} Comparison Across Countries")
    return fig

def summary_table(df, metrics=["GHI","DNI","DHI"]):
    """Return a summary table (mean, median, std) for selected metrics."""
    return df.groupby("Country")[metrics].agg(['mean','median','std'])

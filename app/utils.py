import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(path):
    """Load cleaned CSV data with timestamp parsing."""
    df = pd.read_csv(path, parse_dates=["Timestamp"])
    return df

def boxplot_metric(df, metric):
    """Return a matplotlib figure with a boxplot for a given metric."""
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x="Country", y=metric, data=df, ax=ax)
    ax.set_title(f"{metric} Comparison Across Countries", fontsize=14)
    ax.set_xlabel("Country")
    ax.set_ylabel(metric)
    plt.tight_layout()
    return fig

def summary_table(df, metrics=["GHI", "DNI", "DHI", "Tamb"]):
    """Return a summary table (mean, median, std) grouped by country."""
    return df.groupby("Country")[metrics].agg(["mean", "median", "std"]).round(2)

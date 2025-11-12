import streamlit as st
from utils import load_data, boxplot_metric, summary_table
import pandas as pd

st.set_page_config(page_title="Solar Dashboard", layout="wide")

st.title("🌞 Cross-Country Solar Farm Analysis")

selected_countries = st.multiselect(
    "Select countries to display",
    options=["Benin", "Sierra Leone", "Togo"],
    default=["Benin", "Sierra Leone", "Togo"]
)

dfs = []
for country in selected_countries:
    path = f"data/clean/{country.lower().replace(' ','_')}_clean.csv"
    df = load_data(path)
    df["Country"] = country
    dfs.append(df)
data = pd.concat(dfs, ignore_index=True)

metric = st.selectbox("Select metric to visualize", ["GHI","DNI","DHI","Tamb"])

st.subheader(f"Boxplot of {metric} across selected countries")
fig = boxplot_metric(data, metric)
st.pyplot(fig)

st.subheader("Summary statistics (mean, median, std)")
st.dataframe(summary_table(data))

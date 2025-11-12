import os
import streamlit as st
import pandas as pd
from utils import load_data, boxplot_metric, summary_table

st.set_page_config(page_title="Solar Dashboard", layout="wide")
st.title("🌞 Cross-Country Solar Farm Analysis")

selected_countries = st.multiselect(
    "Select countries to display",
    options=["Benin", "Sierra Leone", "Togo"],
    default=["Benin", "Sierra Leone", "Togo"]
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "../data/clean")

dfs = []
for country in selected_countries:
    if country == "Sierra Leone":
        file_name = "sierraleone_clean.csv"
    else:
        file_name = f"{country.lower().replace(' ', '_')}_clean.csv"

    path = os.path.join(DATA_DIR, file_name)

    if not os.path.exists(path):
        st.error(f"⚠️ File not found for {country}: expected {path}")
        continue

    df = load_data(path)
    df["Country"] = country
    dfs.append(df)

if dfs:
    data = pd.concat(dfs, ignore_index=True)
else:
    st.stop()

metric = st.selectbox("Select metric to visualize", ["GHI", "DNI", "DHI", "Tamb"])

st.subheader(f"📊 Boxplot of {metric} across selected countries")
fig = boxplot_metric(data, metric)
st.pyplot(fig)

st.subheader("📈 Summary statistics (mean, median, std)")
st.dataframe(summary_table(data))

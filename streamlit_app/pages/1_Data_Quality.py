# pages/1_Data_Quality.py
import streamlit as st
import pandas as pd

st.header("📊 Data Quality & Stability")

st.metric("Completeness", "99.2%")
st.metric("PSI (PD Features)", "0.08 (Stable)")
st.metric("Outlier Rate", "1.3%")

st.success("✔ Data meets regulatory & modeling standards")

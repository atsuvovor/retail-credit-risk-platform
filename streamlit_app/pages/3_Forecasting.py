#Forecasting & Capital Impact
# pages/3_Forecasting.py
import streamlit as st

st.header("📈 Forecasting & Stress Testing")

scenario = st.radio("Scenario", ["Baseline", "Mild Stress", "Severe Stress"])

st.metric("Expected Credit Loss", "$1.42B")
st.metric("RWA Impact", "+$6.3B")

st.warning("Stress scenario materially impacts capital ratios")

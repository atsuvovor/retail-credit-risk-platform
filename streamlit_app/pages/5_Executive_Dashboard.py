import streamlit as st
import pandas as pd

df = pd.read_csv("data/processed/bi_credit_risk_dataset.csv")

st.header("📊 Executive Credit Risk Dashboard")

st.metric("Total Expected Loss", f"${df.expected_loss.sum():,.0f}")
st.metric("Portfolio PD", f"{df.pd.mean():.2%}")

st.bar_chart(df.groupby("product")["expected_loss"].sum())

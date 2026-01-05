def forecast_losses(df):
    df["expected_loss"] = df["pd"] * df["lgd"] * df["ead"]
    return df.groupby("product")[["expected_loss"]].sum()

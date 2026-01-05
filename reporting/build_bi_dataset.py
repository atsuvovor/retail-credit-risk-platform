def build_bi_dataset(df):
    bi = df.copy()

    bi["expected_loss"] = bi["pd"] * bi["lgd"] * bi["ead"]

    return bi[[
        "customer_id",
        "product",
        "fico_score",
        "utilization",
        "pd",
        "lgd",
        "ead",
        "expected_loss",
        "default_flag"
    ]]

#bi_df.to_csv("data/processed/bi_credit_risk_dataset.csv", index=False)


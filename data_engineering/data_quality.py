def data_quality_report(df):
    report = {
        "rows": len(df),
        "missing_pct": df.isna().mean(),
        "outlier_fico_pct": (df["fico_score"] < 300).mean(),
        "default_rate": df["default_flag"].mean()
    }
    return report

def engineer_features(df):
    df = df.copy()

    df["fico_bucket"] = pd.cut(
        df["fico_score"],
        bins=[300, 600, 660, 720, 850],
        labels=[1, 2, 3, 4]
    )

    df["high_util_flag"] = (df["utilization"] > 0.8).astype(int)
    df["seasoned_flag"] = (df["months_on_book"] > 24).astype(int)

    return df

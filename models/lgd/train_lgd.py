from sklearn.linear_model import LinearRegression

def train_lgd(df):
    df_d = df[df["default_flag"] == 1]

    X = df_d[["fico_score", "utilization", "loan_balance"]]
    y = df_d["lgd"]

    model = LinearRegression()
    model.fit(X, y)

    return model

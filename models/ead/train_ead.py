from sklearn.linear_model import LinearRegression

def train_ead(df):
    X = df[["loan_balance", "utilization"]]
    y = df["ead"]

    model = LinearRegression()
    model.fit(X, y)

    return model

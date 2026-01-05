from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
import joblib

def train_pd(df):
    features = [
        "fico_score",
        "utilization",
        "months_on_book",
        "unemployment_rate"
    ]

    X = df[features]
    y = df["default_flag"]

    model = LogisticRegression(max_iter=500)
    model.fit(X, y)

    auc = roc_auc_score(y, model.predict_proba(X)[:,1])

    joblib.dump(model, "models/pd/pd_model.pkl")

    return auc

import numpy as np
import pandas as pd

np.random.seed(42)

N = 100_000

df = pd.DataFrame({
    "customer_id": range(N),
    "product": np.random.choice(
        ["Credit Card", "Mortgage", "Personal Loan", "SMB Loan"], N
    ),
    "fico_score": np.random.normal(680, 60, N).clip(300, 850),
    "utilization": np.random.beta(2, 5, N),
    "loan_balance": np.random.lognormal(10, 0.5, N),
    "interest_rate": np.random.uniform(0.03, 0.22, N),
    "months_on_book": np.random.randint(1, 180, N),
    "unemployment_rate": np.random.normal(6, 1.5, N).clip(3, 12),
    "gdp_growth": np.random.normal(1.5, 1.0, N)
})

# Default probability (latent)
logit_pd = (
    -5
    + 0.005 * (700 - df["fico_score"])
    + 2.0 * df["utilization"]
    + 0.15 * df["unemployment_rate"]
)

df["pd"] = 1 / (1 + np.exp(-logit_pd))
df["default_flag"] = np.random.binomial(1, df["pd"])

# LGD
df["lgd"] = np.where(
    df["default_flag"] == 1,
    np.random.beta(2, 5, N),
    0
)

# EAD
df["ead"] = df["loan_balance"] * (
    1 + 0.4 * df["utilization"]
)

df.to_csv("data/raw/retail_credit_data.csv", index=False)

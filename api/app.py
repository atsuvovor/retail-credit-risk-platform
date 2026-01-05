"""
Retail Credit Risk API
----------------------
Exposes data, models, and forecasts for:
- Streamlit dashboards
- Power BI / Tableau
- Internal model validation & governance

Author: Atsu Vovor
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd

from services.data_service import load_integrated_dataset
from services.model_service import (
    score_pd,
    score_lgd,
    score_ead,
    calculate_ecl
)
from services.forecast_service import forecast_ecl

# -------------------------------------------------------------------
# App Initialization
# -------------------------------------------------------------------
app = FastAPI(
    title="Retail Credit Risk API",
    description="End-to-End Credit Risk Modeling & BI Integration",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Lock down in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------------------------
# Schemas
# -------------------------------------------------------------------
class ScoringRequest(BaseModel):
    customer_id: str

class ForecastRequest(BaseModel):
    horizon_months: int = 12
    scenario: str = "baseline"  # baseline | adverse | severe

# -------------------------------------------------------------------
# Health Check
# -------------------------------------------------------------------
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "Retail Credit Risk API"
    }

# -------------------------------------------------------------------
# Integrated Dataset (BI Ready)
# -------------------------------------------------------------------
@app.get("/data/integrated")
def get_integrated_dataset():
    """
    Returns integrated dataset for BI tools
    """
    df = load_integrated_dataset()
    return df.to_dict(orient="records")

# -------------------------------------------------------------------
# Individual Risk Scoring
# -------------------------------------------------------------------
@app.post("/score/pd")
def get_pd_score(request: ScoringRequest):
    try:
        return {"PD": score_pd(request.customer_id)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/score/lgd")
def get_lgd_score(request: ScoringRequest):
    try:
        return {"LGD": score_lgd(request.customer_id)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/score/ead")
def get_ead_score(request: ScoringRequest):
    try:
        return {"EAD": score_ead(request.customer_id)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# -------------------------------------------------------------------
# Expected Credit Loss
# -------------------------------------------------------------------
@app.post("/score/ecl")
def get_ecl(request: ScoringRequest):
    try:
        ecl = calculate_ecl(request.customer_id)
        return {"ECL": ecl}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# -------------------------------------------------------------------
# Forecasting & Capital Impact
# -------------------------------------------------------------------
@app.post("/forecast/ecl")
def forecast_ecl_endpoint(request: ForecastRequest):
    try:
        forecast_df = forecast_ecl(
            horizon_months=request.horizon_months,
            scenario=request.scenario
        )
        return forecast_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# -------------------------------------------------------------------
# Portfolio Summary (Executive View)
# -------------------------------------------------------------------
@app.get("/portfolio/summary")
def portfolio_summary():
    df = load_integrated_dataset()

    summary = {
        "total_exposure": float(df["ead"].sum()),
        "avg_pd": float(df["pd"].mean()),
        "avg_lgd": float(df["lgd"].mean()),
        "total_ecl": float(df["ecl"].sum()),
        "ac


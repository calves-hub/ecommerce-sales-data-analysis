import pandas as pd
from sklearn.metrics import (
    roc_auc_score,
    precision_score,
    recall_score
)

# -------------------------
# Feature Engineering
# -------------------------

def add_total_amount(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]
    return df


def add_shipping_delay(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["ShippingDelay"] = (
        df["Ship Date"] - df["Order Date"]
    ).dt.days
    return df


def add_high_discount_flag(
    df: pd.DataFrame,
    threshold: float = 0.2
) -> pd.DataFrame:
    df = df.copy()
    df["HighDiscount"] = (df["Discount"] >= threshold).astype(int)
    return df


# -------------------------
# Aggregations
# -------------------------

def build_monthly_sales(
    df: pd.DataFrame,
    date_col: str = "OrderDate"
) -> pd.DataFrame:
    if date_col not in df.columns:
        raise KeyError(
            f"Expected column '{date_col}' not found. "
            f"Available columns: {list(df.columns)}"
        )

    monthly = (
        df.assign(
            YearMonth=df[date_col]
            .dt.to_period("M")
            .dt.to_timestamp()
        )
        .groupby("YearMonth", as_index=False)["TotalAmount"]
        .sum()
    )
    return monthly


# -------------------------
# Model Evaluation
# -------------------------

def evaluate_classifier(
    y_true,
    y_pred
) -> dict:
    """
    Returns evaluation metrics for binary classifiers.
    Handles edge cases explicitly.
    """
    return {
        "roc_auc": roc_auc_score(y_true, y_pred),
        "precision": precision_score(
            y_true, y_pred, zero_division=0
        ),
        "recall": recall_score(
            y_true, y_pred, zero_division=0
        )
    }

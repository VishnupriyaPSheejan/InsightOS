import pandas as pd

def analyze_sales(df: pd.DataFrame) -> dict:
    return {
        "revenue": float(df["revenue"].sum()),
        "units": int(df["units"].sum()),
        "orders": int(df["order_id"].nunique()),
    }

def answer_question(df: pd.DataFrame, question: str) -> str:
    q=question.lower()
    total=df["revenue"].sum()
    if "highest" in q and "region" in q:
        s=df.groupby("region").revenue.sum().sort_values(ascending=False)
        return f"{s.index[0]} has the highest revenue (${s.iloc[0]:,.0f}) in the selected data."
    if "category" in q:
        s=df.groupby("category").revenue.sum().sort_values(ascending=False)
        return f"{s.index[0]} leads by revenue (${s.iloc[0]:,.0f})."
    if "change" in q or "trend" in q:
        m=df.assign(month=df.date.dt.to_period("M")).groupby("month").revenue.sum()
        if len(m)<2: return "Select data spanning at least two months to inspect a trend."
        delta=float(m.iloc[-1]-m.iloc[0])
        pct=(delta/m.iloc[0]*100) if m.iloc[0] else 0
        direction="increased" if delta>=0 else "decreased"
        return f"Revenue {direction} by ${abs(delta):,.0f} ({abs(pct):.1f}%) from {m.index[0]} to {m.index[-1]}. This is a descriptive comparison, not a causal explanation."
    if "order" in q:
        return f"There are {df.order_id.nunique():,} unique orders in the selected data."
    return f"Selected data totals ${total:,.0f} revenue across {df.units.sum():,} units. Try asking about trend, highest region, category, or orders."

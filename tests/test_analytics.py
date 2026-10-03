import pandas as pd
from src.analytics import analyze_sales, answer_question

def sample():
    return pd.DataFrame({
        "order_id":[1,2,3], "date":pd.to_datetime(["2025-01-01","2025-02-01","2025-02-02"]),
        "region":["North","South","South"], "category":["Books","Home","Home"],
        "units":[2,1,3], "revenue":[20.,50.,150.]
    })

def test_summary():
    result=analyze_sales(sample())
    assert result["revenue"]==220
    assert result["units"]==6
    assert result["orders"]==3

def test_highest_region():
    assert "South" in answer_question(sample(),"Which region has highest revenue?")

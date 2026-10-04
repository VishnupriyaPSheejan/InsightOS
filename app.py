import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from src.analytics import analyze_sales, answer_question

st.set_page_config(page_title="InsightOS | Business Intelligence", page_icon="📊", layout="wide")
DATA = Path(__file__).parent / "data" / "sales.csv"
st.title("📊 InsightOS")
st.caption("A local-first AI-style business intelligence demo • synthetic data • no API key required")
df = pd.read_csv(DATA, parse_dates=["date"])
with st.sidebar:
    st.header("Explore")
    regions = st.multiselect("Regions", sorted(df.region.unique()), default=sorted(df.region.unique()))
    categories = st.multiselect("Categories", sorted(df.category.unique()), default=sorted(df.category.unique()))
    st.caption("All data is synthetic and bundled with this project.")
filtered = df[df.region.isin(regions) & df.category.isin(categories)]
if filtered.empty:
    st.warning("Choose at least one region and category.")
    st.stop()
summary = analyze_sales(filtered)
c1,c2,c3 = st.columns(3)
c1.metric("Revenue", f"${summary['revenue']:,.0f}")
c2.metric("Units sold", f"{summary['units']:,}")
c3.metric("Orders", f"{summary['orders']:,}")
left,right=st.columns(2)
with left:
    st.subheader("Revenue over time")
    monthly=filtered.assign(month=filtered.date.dt.to_period("M").astype(str)).groupby("month",as_index=False).revenue.sum()
    st.plotly_chart(px.line(monthly,x="month",y="revenue",markers=True),use_container_width=True)
with right:
    st.subheader("Revenue by region")
    by_region=filtered.groupby("region",as_index=False).revenue.sum().sort_values("revenue",ascending=False)
    st.plotly_chart(px.bar(by_region,x="region",y="revenue",color="region"),use_container_width=True)
st.subheader("Ask the analyst")
question=st.text_input("Try: Why did revenue change? Which region has the highest revenue? What is total revenue?")
if question:
    st.info(answer_question(filtered, question))
with st.expander("View bundled dataset"):
    st.dataframe(filtered, use_container_width=True)
st.download_button("Download filtered CSV", filtered.to_csv(index=False), "insightos_filtered.csv", "text/csv")

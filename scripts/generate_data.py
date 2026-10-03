from pathlib import Path
import numpy as np
import pandas as pd

rng=np.random.default_rng(42)
dates=pd.date_range("2025-01-01","2025-12-31",freq="D")
regions=["North","South","East","West"]
categories=["Electronics","Home","Sports","Books"]
rows=[]
oid=10000
for day in dates:
    for _ in range(int(rng.integers(3,9))):
        region=str(rng.choice(regions)); category=str(rng.choice(categories))
        units=int(rng.integers(1,6))
        base={"Electronics":180,"Home":75,"Sports":55,"Books":25}[category]
        seasonal=1+0.18*np.sin(2*np.pi*(day.dayofyear/365))
        price=round(float(base*seasonal*rng.uniform(.8,1.2)),2)
        rows.append([oid,day.date(),region,category,units,price,round(units*price,2)])
        oid+=1
out=Path(__file__).resolve().parents[1]/"data"/"sales.csv"
pd.DataFrame(rows,columns=["order_id","date","region","category","units","unit_price","revenue"]).to_csv(out,index=False)
print(f"Wrote {len(rows)} synthetic rows to {out}")

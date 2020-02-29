import pandas as pd
dfVisitors = pd.read_excel("Int Monthly Visitor.xlsx", index_col=0, na_values=" na ").fillna(0)
dfVisitors.index = pd.to_datetime(dfVisitors.index)
dfVisitors.columns = dfVisitors.columns.str.strip()
dfAseans = dfVisitors.loc["2008":"2017","Brunei Durassalam":"Myanmar"]
AseansVisitors = dfAseans.sum()
print(AseansVisitors)

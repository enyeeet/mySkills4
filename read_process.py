import pandas as pd

file1 = pd.read_csv("data/daily_sales_data_0.csv")
file2 = pd.read_csv("data/daily_sales_data_1.csv")
file3 = pd.read_csv("data/daily_sales_data_2.csv")

df = pd.concat([file1,file2,file3])

df = df[df["product"] == "pink morsel"]
df["price"] = df["price"].replace(r'[\$,]', '', regex=True).astype(float)
df["Sales"] = df["price"] * df["quantity"]

output = df[["Sales", "date", "region"]]
output.columns = ["Sales", "Date", "Region"]
output.to_csv("formatted_output.csv", index=False)
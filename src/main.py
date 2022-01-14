import pandas as pd

# parquetをロード
df = pd.read_parquet("./parquet/original.parquet")
# print(loaded_df.info())

# CSVで出力
df.to_csv("./csv/converted.csv")

print("Proccessing Did Completed")
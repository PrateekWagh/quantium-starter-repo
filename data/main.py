import pandas as pd

csv_files = ["daily_sales_data_0.csv", "daily_sales_data_1.csv", "daily_sales_data_2.csv"]

def load_and_prepare(filepath):
    df = pd.read_csv(filepath).query("product == 'pink morsel'")
    df.price = df.price.str.replace("$", "", regex=False).astype(float)
    df["Sales"] = df["price"] * df["quantity"]
    return df

df_0 = load_and_prepare("daily_sales_data_0.csv")
df_1 = load_and_prepare("daily_sales_data_1.csv")
df_2 = load_and_prepare("daily_sales_data_2.csv")

df_files = [load_and_prepare(file) for file in csv_files]
final_df = pd.concat(df_files, ignore_index=True)
final_df.to_csv("Soul_Foods_Data.csv")
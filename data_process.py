import pandas as pd 

df1= pd.read_csv("data/daily_sales_data_0.csv")
df2=pd.read_csv("data/daily_sales_data_1.csv")
df3=pd.read_csv("data/daily_sales_data_2.csv")

combined_df= pd.concat([df1,df2,df3], ignore_index=True)

combined_df.to_csv("data/combined_data.csv", index=False)


df =pd.read_csv("data/combined_data.csv")
df= df[df["product"]=="pink morsel"]

df.to_csv("data/pink_morsel.csv",index=False)

df=pd.read_csv("data/pink_morsel.csv")
df["price"] = df["price"].str.replace('$', '').astype(float)
df["sales"] = df["quantity"].astype(int) * df["price"]
print(df)
df = df.drop(["product","price", "quantity"],axis=1)
print(df)
df.to_csv("data/final_data.csv",index=False)
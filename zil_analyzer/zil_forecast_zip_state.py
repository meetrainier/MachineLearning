import pandas as pd 
file_path="data\AllRegionsForePublic.csv"
df = pd.read_csv(file_path)
print(df.head())
print(df.columns)
#df[df['date'].astype(str).str.contains('07311954')]

#df_zip_state = df[df["Region"].astype(str).str.contains("Zip") and df["StateName"].astype(str).str.contains("AL")]
df_zip = df[df["Region"].astype(str).str.contains("Zip")]
print(df_zip.head())

df_zip_state = df_zip[df_zip["StateName"].astype(str).str.contains("AL")]
print(df_zip_state.head())
import pandas as pd 
file_path="data\AllRegionsForePublic.csv"
df = pd.read_csv(file_path)
print(df.head())
print(df.columns)

#df_zip_state = df[df["Region"].astype(str).str.contains("Zip") and df["StateName"].astype(str).str.contains("AL")]
df_zip = df[df["Region"].astype(str).str.contains("Zip")]
print(df_zip.head())

min_population=10000

#pop_file_path="data\UszipsShort.csv"
pop_file_path = "data\ZipsShort.csv"
zip_population_df = pd.read_csv(pop_file_path,sep=';')

med_price_file_path = "data\Sale_Prices_Zip.csv"
zip_price_df = pd.read_csv(med_price_file_path,usecols=['RegionName','2019-11'])
#zip_price_df = pd.read_csv(med_price_file_path,sep=';')
print("zip_price_df=",zip_price_df.head())

states = ['AL','AZ','CA','NV','OR','TX','WA']

for s in states:
	df_zip_state = df_zip[df_zip["StateName"].astype(str).str.contains(s)]
	#print(df_zip_state.head())

	df_zip_state.sort_values(by=['ForecastYoYPctChange'], inplace=True, ascending=False)
	#print(df_zip_state.head())

	'''
	print(zip_population_df.head())
	print("type=",type(zip_population_df.loc[zip_population_df.zip == 1001,'population']))
	print("Population=")
	print(zip_population_df.loc[zip_population_df.zip == 1001,'population'].iloc[0])
	'''
	count = 0
	zips=[]
	for x in df_zip_state['RegionName']:
		#print("Type of x =",type(x))
		#print("Type of zip_population_df.zip =",type(zip_population_df.zip))
		if zip_population_df.loc[zip_population_df.zip == int(x),'population'].size == 1:
			p = zip_population_df.loc[zip_population_df.zip == int(x),'population'].iloc[0]
			if p < min_population and count < 10: 
				#print('Qualified zip=',x)
				count=count+1
				zips.append(x)
	selected_rows=df_zip_state[df_zip_state.RegionName.isin(zips)]
	print("The selected rows are:",selected_rows.head())
#Next Plan: 	
##1. Write function to return zips
##2. Write function to modify zips based on min price
##3. Write function to modify zips based on max price
##5. Create df based on zip , include population , median price
##6. Save the data-frame a csv

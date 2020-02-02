import pandas as pd 
file_path="data\AllRegionsForePublic.csv"
df = pd.read_csv(file_path)
print(df.head())
print(df.columns)

#df_zip_state = df[df["Region"].astype(str).str.contains("Zip") and df["StateName"].astype(str).str.contains("AL")]
df_zip = df[df["Region"].astype(str).str.contains("Zip")]
print(df_zip.head())

states = ['AL','AZ','CA','NV','OR','TX','WA']
for s in states:
	df_zip_state = df_zip[df_zip["StateName"].astype(str).str.contains(s)]
	#print(df_zip_state.head())

	df_zip_state.sort_values(by=['ForecastYoYPctChange'], inplace=True, ascending=False)
	print(df_zip_state.head())

	min_population=10000

	#pop_file_path="data\UszipsShort.csv"
	pop_file_path = "data\ZipsShort.csv"
	zip_population_df = pd.read_csv(pop_file_path,sep=';')
	'''
	print(zip_population_df.head())
	print("type=",type(zip_population_df.loc[zip_population_df.zip == 1001,'population']))
	print("Population=")
	print(zip_population_df.loc[zip_population_df.zip == 1001,'population'].iloc[0])
	'''
	# def get_population(zip,df):
		# for x in df['zip']:
			# if x == zip:
				# return 
	count = 0
	for x in df_zip_state['RegionName']:
		#print("Type of x =",type(x))
		#print("Type of zip_population_df.zip =",type(zip_population_df.zip))
		if zip_population_df.loc[zip_population_df.zip == int(x),'population'].size == 1:
			p = zip_population_df.loc[zip_population_df.zip == int(x),'population'].iloc[0]
			if p < min_population and count < 10: 
				print('Qualified zip=',x)
				count=count+1
import pandas as pd
data=pd.read_csv("E:/python/weather/1. Weather Data.csv")

print(data.head())
print(data.shape)
print(data.index)
print(data.columns)
print(data.dtypes)
print(data['Weather'].unique())
print(data.nunique())
print(data.count())
print(data['Weather'].value_counts())
print(data.info())



#Find all the unique 'Wind Speed' values in the data.
print(data['Wind Speed_km/h'].unique())

#Find the number of times when the 'Weather is exactly Clear'

#view_counts()
print(data.Weather.value_counts())

#filtering
print(data[data.Weather=='Clear'])

#groupby

print(data.groupby('Weather').get_group('Clear'))


#Find the number of times when the 'Wind Speed was exactly 4 km/h'.
print(data[data['Wind Speed_km/h']==4])


#Find out all the Null Values in the data.
print(data[data.isnull()])

#Rename the column name 'Weather' of the dataframe to 'Weather Condition'.
print(data.rename(columns={'Weather':'Weather Condition'},inplace=True))

#What is the mean 'Visibility' ?
print(data.Visibility_km.mean())

#What is the Standard Deviation of 'Pressure'  in this data?
print(data.Press_kPa.std())

#What is the Variance of 'Relative Humidity' in this data ?
print(data['Rel Hum_%'].var())

#Find all instances when 'Snow' was recorded.
#value_counts()
print(data['Weather'].value_counts())

#filtering
print(data[data['Weather']=='Snow'])

#str.contains()
print(data[data['Weather'].str.contains('Snow')])

# What is the Mean value of each column against each 'Weather Condition ?
print(data.groupby('Weather').mean())

#What is the Minimum & Maximum value of each column against each 'Weather Condition
print(data.groupby('Weather').min())
print(data.groupby('Weather').max())


#Show all the Records where Weather Condition is Fog.
print(data[data['Weather']=='Fog'])

#Find all instances when 'Weather is Clear' or 'Visibility is above 40'.
print(data[(data['Weather']=='Clear') | (data['Visibility_km']>40)])

#Find all instances when :
#A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
#or
#B. 'Visibility is above 40'

print(data[  (data['Weather']=='Clear') & (data['Rel Hum_%']>50) | (data['Visibility_km']>40) ])
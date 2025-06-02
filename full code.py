import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weatherHistory.csv")

df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)
df.set_index('Formatted Date', inplace=True)
df.index = pd.to_datetime(df.index)

df.dropna(inplace=True)

print("Temperature (C):")
print("Mean:", df['Temperature (C)'].mean())
print("Median:", df['Temperature (C)'].median())
print("Max:", df['Temperature (C)'].max())
print("Min:", df['Temperature (C)'].min())

print("\nHumidity:")
print("Mean:", df['Humidity'].mean())
print("Median:", df['Humidity'].median())
print("Max:", df['Humidity'].max())
print("Min:", df['Humidity'].min())

print("\nWind Speed (km/h):")
print("Mean:", df['Wind Speed (km/h)'].mean())
print("Median:", df['Wind Speed (km/h)'].median())
print("Max:", df['Wind Speed (km/h)'].max())
print("Min:", df['Wind Speed (km/h)'].min())

print("\nWeather condition counts:")
print(df['Precip Type'].value_counts())

if 'Summary' in df.columns:
    summary_lower = df['Summary'].str.lower()
    sunny_days = summary_lower.str.contains("sun|clear").sum()
    cloudy_days = summary_lower.str.contains("cloud").sum()
    print("\nSunny days (from Summary):", sunny_days)
    print("Cloudy days (from Summary):", cloudy_days)
else:
    print("\nColumn 'Summary' not found, skipping sunny/cloudy counts.")

plt.hist(df['Temperature (C)'], bins=30, color='skyblue')
plt.title('Temperature Distribution')
plt.xlabel('Temperature (C)')
plt.ylabel('Frequency')
plt.show()

df['Precip Type'].value_counts().plot(kind='bar', title='Weather Conditions')
plt.xlabel('Condition')
plt.ylabel('Count')
plt.show()

monthly_avg_temp = df['Temperature (C)'].resample('ME').mean()
monthly_avg_temp.plot(title='Monthly Average Temperature')
plt.ylabel('Temperature (C)')
plt.show()

monthly_avg_humidity = df['Humidity'].resample('ME').mean()
monthly_avg_humidity.plot(title='Monthly Average Humidity', color='green')
plt.ylabel('Humidity')
plt.show()

monthly_rainy_days = df[df['Precip Type'] == 'rain']['Precip Type'].resample('ME').count()
monthly_rainy_days.plot(title='Monthly Count of Rainy Days', color='blue')
plt.ylabel('Number of Rainy Days')
plt.show()

plt.scatter(df['Temperature (C)'], df['Humidity'], alpha=0.5)
plt.title('Temperature vs Humidity')
plt.xlabel('Temperature (C)')
plt.ylabel('Humidity')
plt.show()

corr = df.corr(numeric_only=True)
fig, ax = plt.subplots(figsize=(8, 6))
cax = ax.matshow(corr, cmap='coolwarm')
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
fig.colorbar(cax)
plt.title('Correlation Matrix Heatmap')
plt.show()

df.boxplot(column='Temperature (C)', by='Precip Type')
plt.title('Temperature by Weather Type')
plt.suptitle('')
plt.xlabel('Weather Type')
plt.ylabel('Temperature (C)')
plt.show()

coldest = df['Temperature (C)'].idxmin()
hottest = df['Temperature (C)'].idxmax()
print("\nColdest Day:", coldest)
print("Hottest Day:", hottest)

rainy = df[df['Precip Type'] == 'rain']
non_rainy = df[df['Precip Type'] != 'rain']
print("\nAverage Temperature on Rainy Days:", rainy['Temperature (C)'].mean())
print("Average Temperature on Non-Rainy Days:", non_rainy['Temperature (C)'].mean())

print("\nAverage Wind Speed by Weather Type:")
print(df.groupby('Precip Type')['Wind Speed (km/h)'].mean())

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weatherHistory.csv")

# clean and prepare dates
df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)
df['Formatted Date'] = df['Formatted Date'].dt.tz_localize(None)
df['Date'] = pd.to_datetime(df['Formatted Date'].dt.date)
df['Hour'] = df['Formatted Date'].dt.hour
df = df.dropna(subset=['Precip Type'])

df.set_index('Date', inplace=True)

# show temp stats
print("--- Temperature Statistics ---")
print(df['Temperature (C)'].describe())

# show wind speed stats
print("\n--- Wind Speed Statistics ---")
print(df['Wind Speed (km/h)'].describe())

# show humidity stats
print("\n--- Humidity Statistics ---")
print(df['Humidity'].describe())

# show pressure stats
print("\n--- Pressure (millibars) Statistics ---")
print(df['Pressure (millibars)'].describe())

# show wind bearing stats
print("\n--- Wind Bearing (degrees) Statistics ---")
print(df['Wind Bearing (degrees)'].describe())

# show visibility stats
print("\n--- Visibility (km) Statistics ---")
print(df['Visibility (km)'].describe())

# show precip type counts
print("\n--- Precipitation Types ---")
print(df['Precip Type'].value_counts())

# show summary counts
print("\n--- Weather Summaries ---")
print(df['Summary'].value_counts())

# show daily summary counts
print("\n--- daily weather summaries ---")
print(df['Daily Summary'].value_counts())

# plot temp, humidity, wind speed dist.
plt.figure(figsize=(18, 4))

plt.subplot(1, 3, 1)
plt.hist(df['Temperature (C)'], bins=40, color='orange', edgecolor='black')
plt.title('Temperature Distribution')

plt.subplot(1, 3, 2)
plt.hist(df['Humidity'], bins=40, color='lightblue', edgecolor='black')
plt.title('Humidity Distribution')

plt.subplot(1, 3, 3)
plt.hist(df['Wind Speed (km/h)'], bins=40, color='green', edgecolor='black')
plt.title('Wind Speed Distribution')

plt.tight_layout()
plt.show()

# plot precip type counts
plt.figure(figsize=(10, 4))
df['Precip Type'].value_counts().plot(kind='bar', color='purple', edgecolor='black')
plt.title('Precipitation Type Frequency')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

# get the highest 10 in summaries
plt.figure(figsize=(10, 4))
df['Summary'].value_counts().head(10).plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Top 10 Weather Summaries')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# get summaries from 10 to 20
summary_counts = df['Summary'].value_counts()
selected_summaries = summary_counts.iloc[10:20]
plt.figure(figsize=(10, 4))
selected_summaries.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Weather Summaries from 10 to 20')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# get the lowest 5 in summaries
plt.figure(figsize=(10, 4))
df['Summary'].value_counts().tail(5).plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Bottom 5  Weather Summaries')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='x')
plt.tight_layout()
plt.show()

# get the highest 5 in daily summaries
plt.figure(figsize=(10, 4))
df['Daily Summary'].value_counts().head(5).plot(kind='bar', color='sandybrown', edgecolor='black')
plt.title('Top 5 Daily Weather Summaries')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# get the lowest 5 in daily summaries
plt.figure(figsize=(10, 4))
df['Daily Summary'].value_counts().tail(5).plot(kind='bar', color='sandybrown', edgecolor='black')
plt.title('Bottom 5 Daily Weather Summaries')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# daily avg temp
daily_avg = df['Temperature (C)'].resample('D').mean()
# monthly avg temp
monthly_avg = df['Temperature (C)'].resample('ME').mean()
# yearly avg temp
yearly_avg = df['Temperature (C)'].resample('YE').mean()

plt.figure(figsize=(14, 4))
plt.plot(daily_avg.index, daily_avg.values, color='red')
plt.title('Daily Average Temperature')
plt.ylabel('Temperature (C)')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(14, 4))
plt.plot(monthly_avg.index, monthly_avg.values, marker='o', linestyle='-', color='red')
plt.title('Monthly Average Temperature')
plt.ylabel('Temperature (C)')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(14, 4))
plt.plot(yearly_avg.index, yearly_avg.values, marker='o', linestyle='-', color='red')
plt.title('Yearly Average Temperature')
plt.ylabel('Temperature (C)')
plt.grid(True)
plt.tight_layout()
plt.show()

# daily avg pressure
pressure_daily = df['Pressure (millibars)'].resample('D').mean()
# monthly avg pressure
pressure_monthly = df['Pressure (millibars)'].resample('ME').mean()
# yearly avg pressure
pressure_yearly = df['Pressure (millibars)'].resample('YE').mean()

plt.figure(figsize=(14, 4))
plt.plot(pressure_daily.index, pressure_daily, color='mediumslateblue')
plt.title('Daily Average Pressure')
plt.ylabel('Pressure (millibars)')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(14, 4))
plt.plot(pressure_monthly.index, pressure_monthly, marker='o', color='mediumslateblue')
plt.title('Monthly Average Pressure')
plt.ylabel('Pressure (millibars)')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(14, 4))
plt.plot(pressure_yearly.index, pressure_yearly, marker='o', linestyle='-', color='mediumslateblue')
plt.title('Yearly Average Pressure')
plt.ylabel('Pressure (millibars)')
plt.grid(True)
plt.tight_layout()
plt.show()

# daily avg wind bearing
windbearing_daily = df['Wind Bearing (degrees)'].resample('D').mean()
# monthly avg wind bearing
windbearing_monthly = df['Wind Bearing (degrees)'].resample('ME').mean()
# yearly avg wind bearing
windbearing_yearly = df['Wind Bearing (degrees)'].resample('YE').mean()

plt.figure(figsize=(14, 4))
plt.plot(windbearing_daily.index, windbearing_daily, color='teal')
plt.title('Daily Average Wind Bearing')
plt.ylabel('Degrees')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(14, 4))
plt.plot(windbearing_monthly.index, windbearing_monthly, marker='o', color='teal')
plt.title('Monthly Average Wind Bearing')
plt.ylabel('Degrees')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(14, 4))
plt.plot(windbearing_yearly.index, windbearing_yearly, marker='o', linestyle='-', color='teal')
plt.title('Yearly Average Wind Bearing')
plt.ylabel('Degrees')
plt.grid(True)
plt.tight_layout()
plt.show()

# yearly avg visibility
yearly_visibility = df['Visibility (km)'].resample('YE').mean()
plt.figure(figsize=(14, 4))
plt.plot(yearly_visibility.index, yearly_visibility.values, marker='o', linestyle='-', color='mediumslateblue')
plt.title('Yearly Average Visibility')
plt.ylabel('Visibility (km)')
plt.grid(True)
plt.tight_layout()
plt.show()

# daily avg humidity and wind speed
daily_avg = df[['Humidity', 'Wind Speed (km/h)']].resample('D').mean()
# monthly avg humidity and wind speed
monthly_avg = df[['Humidity', 'Wind Speed (km/h)']].resample('ME').mean()
# yearly avg humidity and wind speed
yearly_avg = df[['Humidity', 'Wind Speed (km/h)']].resample('YE').mean()

plt.figure(figsize=(12, 4))
plt.plot(daily_avg.index, daily_avg['Humidity'], label='Humidity', color='darkblue')
plt.plot(daily_avg.index, daily_avg['Wind Speed (km/h)'], label='Wind Speed', color='forestgreen')
plt.title('Daily Humidity and Wind Speed')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(14, 4))
plt.plot(monthly_avg.index, monthly_avg['Humidity'], marker='o', color='darkblue', label='Humidity')
plt.plot(monthly_avg.index, monthly_avg['Wind Speed (km/h)'], marker='o', color='forestgreen', label='Wind Speed')
plt.title('Monthly Average Humidity and Wind Speed')
plt.ylabel('Values')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(14, 4))
plt.plot(yearly_avg.index, yearly_avg['Humidity'], marker='o', color='darkblue', label='Humidity')
plt.plot(yearly_avg.index, yearly_avg['Wind Speed (km/h)'], marker='o', color='forestgreen', label='Wind Speed')
plt.title('Yearly Average Humidity and Wind Speed')
plt.ylabel('Values')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# final weather insights
hottest = df.loc[df['Temperature (C)'].idxmax()]
coldest = df.loc[df['Temperature (C)'].idxmin()]
corr_temp_hum = df['Temperature (C)'].corr(df['Humidity'])
rainy_days = df[df['Precip Type'] == 'rain']
non_rainy_days = df[df['Precip Type'] != 'rain']

# handle duplicates safely
hottest = df.loc[df['Temperature (C)'].idxmax()]
if isinstance(hottest, pd.DataFrame):
    hottest = hottest.iloc[0]

coldest = df.loc[df['Temperature (C)'].idxmin()]
if isinstance(coldest, pd.DataFrame):
    coldest = coldest.iloc[0]

print("\n--- Weather Insights ---")
print("Hottest Day:", hottest['Formatted Date'].strftime('%Y-%m-%d'), f"| {hottest['Temperature (C)']:.2f} °C")
print("Coldest Day:", coldest['Formatted Date'].strftime('%Y-%m-%d'), f"| {coldest['Temperature (C)']:.2f} °C")
print("Temp–Humidity Correlation:", f"{corr_temp_hum:.2f}")
print("Avg Temp on Rainy Days:", f"{rainy_days['Temperature (C)'].mean():.2f} °C")
print("Avg Temp on Dry Days:", f"{non_rainy_days['Temperature (C)'].mean():.2f} °C")
print("\n--- Additional Weather Stats ---")
print(f"Average Visibility: {df['Visibility (km)'].mean():.2f} km")
print(f"Average Wind Speed: {df['Wind Speed (km/h)'].mean():.2f} km/h")
print(f"Average Wind Bearing: {df['Wind Bearing (degrees)'].mean():.2f}°")
print(f"Average Pressure: {df['Pressure (millibars)'].mean():.2f} millibars")
print(f"Average Humidity: {df['Humidity'].mean():.2f}")

print("\nAverage Wind Speed by Precipitation Type:")
print(df.groupby('Precip Type')['Wind Speed (km/h)'].mean())
print("\nAverage Visibility by Precipitation Type:")
print(df.groupby('Precip Type')['Visibility (km)'].mean())

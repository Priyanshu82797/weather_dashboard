import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Step 1: Replace with your actual API key
API_KEY = "8f24723790340654f45f0d90e4fcb8f0"
CITY = "New Delhi"  # You can change the city
UNITS = "metric"    # Use "imperial" for Fahrenheit

# Step 2: Build the API URL
url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units={UNITS}"

# Step 3: Send the request
response = requests.get(url)
data = response.json()

# Step 4: Prepare lists to store data
timestamps = []
temperatures = []
humidity = []
wind_speed = []

# Step 5: Extract 8 forecast data points (24 hours = 8 * 3-hour intervals)
for i in range(8):
    forecast = data['list'][i]
    time = datetime.fromtimestamp(forecast['dt']).strftime('%H:%M')
    temp = forecast['main']['temp']
    hum = forecast['main']['humidity']
    wind = forecast['wind']['speed']

    timestamps.append(time)
    temperatures.append(temp)
    humidity.append(hum)
    wind_speed.append(wind)

# Step 6: Create visualizations using seaborn
sns.set(style="whitegrid")
fig, axs = plt.subplots(3, 1, figsize=(10, 12))

# Temperature Plot
sns.lineplot(x=timestamps, y=temperatures, ax=axs[0], marker='o', color='red')
axs[0].set_title(f"Temperature Forecast in {CITY}")
axs[0].set_ylabel("Temperature (°C)")

# Humidity Plot
sns.barplot(x=timestamps, y=humidity, ax=axs[1], palette="Blues_d")
axs[1].set_title("Humidity Forecast (%)")
axs[1].set_ylabel("Humidity")

# Wind Speed Plot
sns.lineplot(x=timestamps, y=wind_speed, ax=axs[2], marker='o', color='green')
axs[2].set_title("Wind Speed Forecast (m/s)")
axs[2].set_ylabel("Wind Speed")

plt.tight_layout()
plt.show()

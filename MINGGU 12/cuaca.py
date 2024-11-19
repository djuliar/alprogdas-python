import requests
import json

# URL dan parameter API
city = "Bondowoso"
api_key = "012334c03083d398b22d99b805d58042"  # Gantilah dengan API key Anda dari penyedia layanan cuaca
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# Mengirim permintaan GET ke API
response = requests.get(url)

# Memeriksa status respons
if response.status_code == 200:
    data = response.json()  # Mengurai data JSON
    main = data['main']
    temperature = main['temp'] / 10 
    pressure = main['pressure']
    humidity = main['humidity']

    print(f"Cuaca di {city}:")
    print(f"Suhu: {temperature}K")
    print(f"Tekanan: {pressure} hPa")
    print(f"Kelembaban: {humidity}%")
else:
    print("Gagal mengambil data cuaca!")
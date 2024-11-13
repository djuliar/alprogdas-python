from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cuaca', methods=['POST'])
def cuaca():
    kota = request.form['kota']
    api_key = 'API_KEY_ANDA'  # Masukkan API Key yang valid dari layanan cuaca, misalnya OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={kota}&appid={api_key}"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        cuaca = {
            'kota': kota,
            'suhu': data['main']['temp'],
            'deskripsi': data['weather'][0]['description']
        }
        return render_template('hasil.html', cuaca=cuaca)
    else:
        return f"Kota {kota} tidak ditemukan."

if __name__ == '__main__':
    app.run(debug=True)

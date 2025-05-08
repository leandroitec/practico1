import requests

from flask import Flask, render_template, request

app = Flask(__name__)

ciudades = {
    "Buenos Aires": {"lat": -34.6037, "lon": -58.3816},
    "Cordoba": {"lat": -31.4201, "lon": -64.1888},
    "Madrid": {"lat": 40.4168, "lon": -3.7038},
    "Nueva York": {"lat": 40.7128, "lon": -74.0060},
    "Tokio": {"lat": 35.6895, "lon": 139.6917},
    "Paris": {"lat": 48.8566, "lon": 2.3522},
    "Londres": {"lat": 51.5074, "lon": -0.1278},
    "Sidney": {"lat": -33.8688, "lon": 151.2093},
    "Ciudad de Mexico": {"lat": 19.4326, "lon": -99.1332},
    "El Cairo": {"lat": 30.0444, "lon": 31.2357}
    }

@app.route("/")
def index():
    
    return render_template(
        "index.html",
        cities = ciudades,
        )


@app.route("/climas")
def climas():
    ciudad = request.args.get("ciudad")
    # /clima?ciudad=Nombre
    ciudad = request.args.get("ciudad",str)
    
    lat = ciudades[ciudad]["lat"]
    lon = ciudades[ciudad]["lon"]

    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")
    data = response.json()
    print(data)
    datos_ciudad = data["current_weather"]
    print("Status code from requests",response.status_code)
    
    return render_template(
        "clima.html",
        informacion = datos_ciudad,
        city = ciudad,
        )

# cosas que cambie: linea 25 cities = ciudades, linea 47 city = ciudad, linea 7 saque los tildes de las ciudades, 

# https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current_weather=true

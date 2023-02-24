import requests

def obtener_temperaturas(ciudad, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp_max = data["main"]["temp_max"]
        temp_min = data["main"]["temp_min"]
        return temp_max, temp_min
    else:
        print("Error al realizar la petición.")

ciudad = "Madrid"
api_key = "TU_CLAVE_DE_API"
temperatura_max, temperatura_min = obtener_temperaturas(ciudad, api_key)
print(f"Temperatura máxima en {ciudad}: {temperatura_max}K")
print(f"Temperatura mínima en {ciudad}: {temperatura_min}K")

import requests

def obtener_datos_api_externa():
    url = 'https://api.externa.com/datos'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

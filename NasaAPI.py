import requests


APOD_URI: str = "https://api.nasa.gov/planetary/apod"


def get_apod(api_key: str):
    print("Requesting NASA APOD data...")
    response = requests.get(url=APOD_URI, params={"api_key": api_key, "hd": False})
    response.raise_for_status()
    print("NASA APOD request succeeded.")
    return response.json()

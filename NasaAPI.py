import requests


APOD_URI: str = "https://api.nasa.gov/planetary/apod"


def get_apod(api_key: str):
    print("Requesting NASA APOD data...")
    response = requests.get(url=APOD_URI, params={"api_key": api_key, "hd": False})

    if response.status_code != 200:
        raise Exception(
            f"NASA RequestError: {response.status_code} - {response.reason}"
        )
    print("NASA APOD request succeeded.")
    return response.json()

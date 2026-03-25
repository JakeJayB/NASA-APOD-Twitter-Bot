from NasaAPI import get_apod
from UploadCareAPI import upload_img
from config import environment


def main():
    apod_data = get_apod(environment.NASA_APOD_KEY)
    
    if apod_data["media_type"] != "image":
        print("Today's APOD is a video. Skipping...")
        return

    url = upload_img(environment.UPLOADCARE_KEY, apod_data)
    print(url)


main()

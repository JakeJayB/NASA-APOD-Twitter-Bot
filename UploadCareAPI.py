import time
import requests

UC_UPLOAD_URI = "https://upload.uploadcare.com/" # for uploading data
UC_CDN_URI = "https://1c89zf2tb2.ucarecd.net/" # for getting data

def upload_img(key, apod_data):
    upload_uri = f"{UC_UPLOAD_URI}from_url/"
    status_uri = f"{upload_uri}status/"

    payload = {
        "pub_key": key,
        "source_url": apod_data['url'],
        "store": "0",
        "check_URL_duplicates": "1",
        "save_URL_duplicates": "1",
    }

    print("Uploading APOD image to UploadCare...")
    response = requests.post(upload_uri, data=payload)
    response.raise_for_status()
    
    data = response.json()
    if "uuid" in data:
        print("APOD image already exists.")
        return f"{UC_CDN_URI}{data['uuid']}/"
    else:

        base_delay = 1
        payload = {
            "token": data['token']
        }
        for attempt in range(5):         
            response = requests.get(status_uri, params=payload)
            response.raise_for_status()
            
            data = response.json()
            if data['status'] == "success" and data['is_ready']:
                print("APOD image sucessfully uploaded.")
                return f"{UC_CDN_URI}{data['uuid']}/"
            
            wait = base_delay * (2**attempt)
            print(f"Image not yet ready. Waiting {wait} seconds...")
            time.sleep(wait)
        raise Exception("UploadCare Timeout Error: Data not ready after max retries")

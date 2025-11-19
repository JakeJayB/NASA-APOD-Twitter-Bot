import requests


class Extract:
    def __init__(self):
        self.API_URL = "https://api.nasa.gov/planetary/apod"
         
    
    def GetAPOD(self, key: str):
        key = key.strip()
        data = requests.get(self.API_URL + f"?api_key={key}")
        
        if data.status_code != 200:
            print(f"RequestError: {data.status_code} - {data.reason}")
            return None
        
        data = data.json()
        print("Returned data from NASA-APOD API:") 
        print(f"\t{data['title']}") 
        print(f"\t{data['date']}") 
        print(f"\t{data['explanation']}") 
        print(f"\t{data['url']}") 
            
        return data

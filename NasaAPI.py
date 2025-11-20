import requests


class Extract:
    def __init__(self, key : str):
        self.API_URL = "https://api.nasa.gov/planetary/apod"
        self.key = key.strip()
         
    
    def GetAPOD(self):
        response = requests.get(self.API_URL + f"?api_key={self.key}")
        
        if response.status_code != 200:
            raise Exception(f"NASA RequestError: {response.status_code} - {response.reason}")
        
        data = response.json()
        print("Returned data from NASA-APOD API:") 
        print(f"\t{data['title']}") 
        print(f"\t{data['date']}") 
        print(f"\t{data['explanation']}") 
        print(f"\t{data['url']}") 
            
        return data
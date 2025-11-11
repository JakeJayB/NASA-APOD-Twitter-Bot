import requests


class Extract:
    def __init__(self):
        self.API_URL = "https://api.nasa.gov/planetary/apod"
         
    
    def GetAPOD(self, key: str):
        key = key.strip()
        data = requests.get(self.API_URL + f"?api_key={key}&count=2")
        print(data.status_code, data.json)
        
    def Get(self, params):
        pass
        
    
    
def main():
    e = Extract()
    e.GetAPOD("")

main()
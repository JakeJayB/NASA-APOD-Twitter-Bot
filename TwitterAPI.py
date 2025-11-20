from datetime import date
import requests

class Post:
    def __init__(self, key : str):
        self.API_URL = "https://api.x.com/2"
        self.key = key.strip()
        self.__SetUsername()
    
    
    def __SetUsername(self):
        url = self.API_URL + "/users/me"
        header = {"Authorization": f"Bearer {self.key}"}
        response = requests.get(url, headers=header)
        
        if response.status_code != 200:
            raise Exception(f"Twitter RequestError: {response.status_code} - {response.reason}")
        
        data = response.json()['data']
        self.username = data.get('username', None)
        self.userID = data.get('id', None)
        
        if not self.userID or not self.username:
            raise Exception("Could not find username/userID with given Twitter key")
        
        print("Found Twitter Username:")
        print(f"\tUsername: {self.username}")
        print(f"\tUserID: {self.userID}")
        
        
        

    def HasPostedToday(self):
        url = self.API_URL + "/tweets/counts/recent"
        
        header = {"Authorization": f"Bearer {self.key}"}
        params = {"start_time": f"{str(date.today())}00:00:00"}
        response = requests.get(url, headers=header)
        
    
    def Post(self):
        pass
    
    
def main():
    p = Post("")



main()
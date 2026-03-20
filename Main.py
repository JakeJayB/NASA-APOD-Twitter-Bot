from config import environment
import NasaAPI, TwitterAPI

def main():
    print(environment.model_dump())
    
    # n = NasaAPI.Extract(NASA_APOD_KEY)
    # apod_data = n.GetAPOD()
    
main()
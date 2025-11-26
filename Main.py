import os
from dotenv import load_dotenv, find_dotenv
import NasaAPI, TwitterAPI

def main():
    
    if find_dotenv() == "":
        raise Exception(".env file not found! See .env.example for further instructions.")
    
    load_dotenv()
    X_BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")
    X_API_KEY = os.getenv("X_API_KEY")
    X_API_SECRET = os.getenv("X_API_SECRET")
    X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
    X_ACCESS_SECRET = os.getenv("X_ACCESS_SECRET")
    NASA_APOD_KEY = os.getenv("NASA_APOD_KEY")
    
    if any(token is None or token == "" for token in [X_BEARER_TOKEN, X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_SECRET, NASA_APOD_KEY]):
        raise Exception("One or more API credentials missing in .env file!")
    
main()
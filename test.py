#function to test API

import requests
import json

url = "https://wordle.votee.dev:8000/random?guess=hello&size=5"

try:
    response = requests.get(url)
    response.raise_for_status()

except requests.exceptions.RequestException as e:
    print(f"Error making request to {url}: {e}")

except ValueError as ve:
    print(f"Error parsing JSON response: {ve}")

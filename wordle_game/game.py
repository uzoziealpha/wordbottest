import random
import requests
import json

class WordleGame:
    def __init__(self):

        self.base_url = "https://wordle.votee.dev:8000/random"
        self.word_list = ["sogzd", "hello", "world", "apple", "grape", "peach", "lemon"]

    def guess_word(self, guess: str, size: int = 5):

        url = f"{self.base_url}?guess={guess}&size={size}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()  # Parse JSON response
            return json.dumps(data, indent=4)
        except requests.exceptions.RequestException as e:
            print(f"Error making request to {url}: {e}")
            return json.dumps({"error": "Unable to make a guess", "status_code": response.status_code if 'response' in locals() else None}, indent=4)
        except ValueError as ve:
            print(f"Error parsing JSON response: {ve}")
            return json.dumps({"error": "Invalid JSON response"}, indent=4)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return json.dumps({"error": "An unexpected error occurred"}, indent=4)

    def guess_word_random(self, seed: int = None):

        try:
            random.seed(seed)
            random_word = random.choice(self.word_list)
            return self.guess_word(random_word)
        except IndexError as ie:
            print(f"Error: The word list is empty. {ie}")
            return json.dumps({"error": "Word list is empty"}, indent=4)
        except Exception as e:
            print(f"An unexpected error occurred in guess_word_random: {e}")
            return json.dumps({"error": "An unexpected error occurred during the random guess"}, indent=4)
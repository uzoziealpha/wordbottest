from wordle_game.game import WordleGame

def main():

    game = WordleGame()  # Corrected typo here
    result = game.guess_word_random()
    print("Random Guess Result:", result)

if __name__ == "__main__":
    main()
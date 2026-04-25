import random

def hangman():
    words = ["python", "coding", "github", "software", "development"]
    word = random.choice(words)
    guessed = "_" * len(word)
    attempts = 6
    
    while attempts > 0 and "_" in guessed:
        print(f"\nWord: {guessed} | Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()
        
        if guess in word:
            # Update the underscores with the correctly guessed letter
            guessed_list = list(guessed)
            for i, char in enumerate(word):
                if char == guess:
                    guessed_list[i] = guess
            guessed = "".join(guessed_list)
        else:
            attempts -= 1
            print("Wrong guess!")

    if "_" not in guessed:
        print(f"Congratulations! The word was {word}")
    else:
        print(f"Game Over! The word was {word}")

hangman()

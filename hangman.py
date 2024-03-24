import random
theme = "cars"
letters = []
words = ["lamborghini", "bugati", "audi", "bentley", "volkswagen", "rolls royce",
         "mercedes benz", "suzuki", "hyundai", "honda", "toyota", "mahindra"]
word = random.choice(words)  # picking a random word from words
display_word = ['_' for _ in word]  # displays n dashes for a word of n letters
attempts = 7
user_name = input("Your Name: ")
print("Welcome to Hangman\n")
print(f"The theme is {theme}\n")
while attempts > 0 and '_' in display_word:
    print(" ".join(display_word))  # printing dashes
    guess = input("Guess a letter: ").lower()
    if guess in word:
        # enumerate separates each letter of the word
        for index, letter in enumerate(word):
            if letter == guess:
                display_word[index] = guess
                print("\n")
    else:
        print("Wrong Letter\n")
        attempts -= 1


if '_' not in display_word:
    print(f"You have guessed the word 🥳\nCongratulation {user_name} 🍾")
else:
    print(f"You ran out of attempts!!\nYou lost {user_name} hahahaha")
    print(f"The word was: {word}")

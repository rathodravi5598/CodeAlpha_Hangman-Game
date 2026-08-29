import random

categories = {
    "Technologies": ["python", "android", "flutter", "java", "csharp"],
    "Sports": ["cricket", "badminton", "kabaddi", "snooker", "volleyball"],
    "Fruits": ["mango", "apple", "pineapple", "kiwi", "berry"],
    "Animals": ["lion", "tiger", "elephant", "horse", "dog"]
}

print("-" * 45)
print("           🎮 HANGMAN GAME 🎮")
print("-" * 45)

print("\nChoose A Category:\n")

print("1. Technologies 💻")
print("2. Sports 🏏")
print("3. Fruits 🍎")
print("4. Animals 🐯")


while True:

    choice = input("\nEnter Your Choice (1 - 4): ")

    if choice == "1":
        category = "Technologies"
        break

    elif choice == "2":
        category = "Sports"
        break

    elif choice == "3":
        category = "Fruits"
        break

    elif choice == "4":
        category = "Animals"
        break

    else:
        print("❌ Invalid choice! Please choose 1, 2, 3, or 4.")


word = random.choice(categories[category])

# Store guessed letters
guessed_letters = []

wrong_guesses = 0
max_wrong_guesses = 6


print("\n" + "-" * 45)
print("Selected Category:", category)
print("-" * 45)

print("\nYou Have 6 Wrong Guesses Allowed.")
print("Guess The Word One Letter At A Time!")


while wrong_guesses < max_wrong_guesses:

    display_word = ""

    for letter in word:

        if letter in guessed_letters:
            display_word += letter + " "

        else:
            display_word += "_ "


    print("\nWord:", display_word)


    if guessed_letters:
        print("Guessed letters:", ", ".join(guessed_letters))

    if all(letter in guessed_letters for letter in word):

        print("\n" + "=" * 45)
        print("🎉 CONGRATULATIONS!")
        print("You guessed the word correctly!")
        print("You guessed the word:", word)
        print("You Won!")
        print("=" * 45)

        break


    print("Remaining chances:", max_wrong_guesses - wrong_guesses)


    guess = input("Guess a letter: ").lower().strip()


    if len(guess) != 1 or not guess.isalpha():

        print("❌ Please Enter Only One Alphabet Letter.")

        continue


    if guess in guessed_letters:

        print("⚠️ You Already Guessed This Letter!")

        continue

    guessed_letters.append(guess)


    if guess in word:

        print("✅ Correct Guess!")

    else:

        wrong_guesses += 1

        print("❌ Wrong Guess!")

if wrong_guesses == max_wrong_guesses:

    print("\n" + "-" * 45)
    print("💀 GAME OVER!")
    print("The correct word was:", word)
    print("-" * 45)
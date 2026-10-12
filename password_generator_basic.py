import random
import string

while True:

    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8.")
            continue

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = ''.join(
            random.choice(characters)
            for _ in range(length)
        )

        print("\nGenerated Password:")
        print(password)

        again = input("\nGenerate another password? (y/n): ")

        if again.lower() != "y":
            break

    except ValueError:
        print("Please enter a valid number.")
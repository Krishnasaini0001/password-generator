import random
import string

def generate_password(length, use_symbols=True):
    characters = string.ascii_letters + string.digits

    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=" * 40)
    print("      Password Generator")
    print("=" * 40)

    while True:
        try:
            length = int(input("Enter password length: "))
            if length < 4:
                print("Password length should be at least 4.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    choice = input("Include symbols? (y/n): ").strip().lower()
    use_symbols = choice == "y"

    password = generate_password(length, use_symbols)

    print("\nGenerated Password:")
    print(password)

if _name_ == "_main_":
    main()
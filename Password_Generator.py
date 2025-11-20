import random
import string
import argparse
import sys

# Optional clipboard support
try:
    import pyperclip
    HAVE_PYPERCLIP = True
except Exception:
    pyperclip = None
    HAVE_PYPERCLIP = False


def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special_chars

    pwd = ""
    meet_criteria = False
    has_number = False
    has_special_char = False
    has_upper = False
    has_lower = False

    while (not meet_criteria) or (len(pwd) < min_length):
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special_chars:
            has_special_char = True

        if new_char.isupper():
            has_upper = True
        if new_char.islower():
            has_lower = True

        meet_criteria = True
        # Always require at least one upper and one lower
        meet_criteria = meet_criteria and has_upper and has_lower
        if numbers:
            meet_criteria = meet_criteria and has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special_char

    return pwd


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="Password_Generator",
        description="Generate secure random passwords (interactive if no length provided).",
    )
    parser.add_argument("-l", "--length", type=int, help="minimum password length (interactive if omitted)")
    parser.add_argument("--numbers", dest="numbers", action="store_true", help="include numbers")
    parser.add_argument("--no-numbers", dest="numbers", action="store_false", help="exclude numbers")
    parser.set_defaults(numbers=True)
    parser.add_argument("--special", dest="special", action="store_true", help="include special characters")
    parser.add_argument("--no-special", dest="special", action="store_false", help="exclude special characters")
    parser.set_defaults(special=True)
    parser.add_argument("-n", "--count", dest="count", type=int, default=1, help="how many passwords to generate")
    parser.add_argument("--copy", dest="copy", action="store_true", help="copy the last generated password to clipboard (requires pyperclip)")

    args = parser.parse_args(argv)

    if args.length is None:
        try:
            min_length = int(input("Enter the minimum length: ").strip())
        except Exception:
            print("Invalid length. Using default 8.")
            min_length = 8
    else:
        min_length = args.length

    numbers = args.numbers
    special = args.special

    last_pwd = None
    for i in range(max(1, args.count)):
        last_pwd = generate_password(min_length, numbers, special)
        if args.count == 1:
            print("Your Password is:", last_pwd)
        else:
            print(f"Password {i+1}: {last_pwd}")

    if args.copy:
        if not HAVE_PYPERCLIP:
            print("Cannot copy to clipboard: 'pyperclip' not installed. Run 'pip install pyperclip' to enable this feature.")
        else:
            try:
                pyperclip.copy(last_pwd or "")
                print("Password copied to clipboard.")
            except Exception as e:
                print("Failed to copy to clipboard:", e)


if __name__ == "__main__":
    main()

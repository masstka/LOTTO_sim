import random

# Get and validate user's numbers
def get_user_numbers():
    numbers = []

    while len(numbers) < 6:
        user_input = input("Please enter a number between 1 and 49: ")

        if not user_input.isdigit():
            print("That's not a number! Try again.")
            continue

        number = int(user_input)

        if number < 1 or number > 49:
            print("Number must be between 1 and 49. Try again.")
        elif number in numbers:
            print("That number is already in use. Try again.")
        else:
            numbers.append(number)

    numbers.sort()
    print(f"You have entered: {', '.join(map(str, numbers))}")
    return numbers

# Generate lottery numbers
def get_lotto_numbers():
    lotto_numbers = random.sample(range(1, 50), 6)
    print(f"The lottery numbers are: {', '.join(map(str, lotto_numbers))}")
    return lotto_numbers

# Check and print matched numbers
def check_matches(user_numbers, lotto_numbers):
    matches = set(user_numbers) & set(lotto_numbers)
    if matches:
        print(f"You have matched {len(matches)} numbers: {', '.join(map(str, matches))}")
    else:
        print("You have not matched any numbers.")

# Main game function
def main():
    user_numbers = get_user_numbers()
    lotto_numbers = get_lotto_numbers()
    check_matches(user_numbers, lotto_numbers)

# Run the game
main()
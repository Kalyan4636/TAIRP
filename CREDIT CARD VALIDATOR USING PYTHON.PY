def is_valid_credit_card(number):
    # Remove spaces and convert the number to a list of integers
    digits = [int(digit) for digit in number if digit.isdigit()]

    # Check if the number of digits is valid for a credit card
    if len(digits) != 16:
        return False

    # Apply Luhn's algorithm
    checksum = sum(digits[::-2] + [sum(divmod(d * 2, 10)) for d in digits[-2::-2]])
    return checksum % 10 == 0

def main():
    while True:
        credit_card_number = input("Enter a credit card number (1234567890111234): ")

        if credit_card_number.isdigit() and len(credit_card_number) == 16:
            if is_valid_credit_card(credit_card_number):
                print("Valid credit card number!")
            else:
                print("Invalid credit card number.")
        else:
            print("Invalid input. Please enter a 16-digit number.")

        choice = input("Do you want to validate another credit card number? (yes/no): ")
        if choice.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

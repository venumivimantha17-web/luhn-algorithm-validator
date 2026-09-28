def verify_card_number(card_number):
    # Remove spaces and dashes
    card_number = card_number.replace(" ", "").replace("-", "")

    # Convert the card number into a list of integers
    digits = [int(digit) for digit in card_number]

    # Double every other digit, starting from the second-to-last digit
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2

        # If the result is greater than 9, subtract 9
        if digits[i] > 9:
            digits[i] -= 9

    # Calculate the sum of all digits
    total = sum(digits)

    # A valid Luhn number has a sum divisible by 10
    if total % 10 == 0:
        return "VALID!"

    return "INVALID!"

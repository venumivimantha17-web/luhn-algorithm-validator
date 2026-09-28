# Luhn Algorithm Validator

A simple Python implementation of the **Luhn Algorithm**, also known as the **Modulus 10** or **Mod 10** algorithm.

The Luhn Algorithm is a checksum formula commonly used to validate identification numbers such as credit card numbers.

## Features

* Validates numbers using the Luhn Algorithm
* Supports card numbers containing spaces
* Supports card numbers containing dashes
* Returns `VALID!` for valid numbers
* Returns `INVALID!` for invalid numbers
* Written entirely in Python

## How the Luhn Algorithm Works

The algorithm follows these steps:

1. Start from the rightmost digit and exclude the check digit.
2. Double every other digit moving from right to left.
3. If a doubled digit is greater than `9`, subtract `9` from it.
4. Add all the resulting digits together.
5. If the total is divisible by `10`, the number is valid.
6. Otherwise, the number is invalid.

## Example

For the card number:

```text
453914889
```

The function returns:

```text
VALID!
```

Another example:

```text
453914881
```

returns:

```text
INVALID!
```

The program also accepts formatted card numbers:

```text
4111-1111-1111-1111
```

which returns:

```text
VALID!
```

## Usage

Import or run the `verify_card_number` function:

```python
from luhn_algorithm import verify_card_number

print(verify_card_number("453914889"))
print(verify_card_number("4111-1111-1111-1111"))
print(verify_card_number("453914881"))
print(verify_card_number("1234 5678 9012 3456"))
```

### Output

```text
VALID!
VALID!
INVALID!
INVALID!
```

## Function

```python
verify_card_number(card_number)
```

### Parameter

* `card_number` – A string containing the number to be validated. Spaces and dashes are supported.

### Return Value

* `VALID!` – If the number passes the Luhn Algorithm.
* `INVALID!` – If the number fails the Luhn Algorithm.

## Technologies Used

* Python 3

## Project Structure

```text
luhn-algorithm-validator/
│
├── luhn_algorithm.py
└── README.md
```

## Purpose

This project was created as a practical implementation of the Luhn Algorithm and demonstrates Python fundamentals including:

* Functions
* Strings
* Lists
* Loops
* Conditional statements
* Arithmetic operations
* Input processing



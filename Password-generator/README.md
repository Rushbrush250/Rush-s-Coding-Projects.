# Secure Password Generator

A robust Python script that generates highly secure passwords using multiple randomization techniques and security libraries.

## Features

- Combines multiple sources of randomness (urandom, secrets, random)
- Generates passwords with:
  - Random numbers
  - Lowercase letters
  - Uppercase letters
  - Special characters
  - Generated words using Faker
- Implements true randomness by seeding with secure random values
- Produces complex passwords with mixed character positioning

## Requirements

- Python 3.x
- Required libraries:
  - `faker`
  - `secrets`
  - `random`
  - `os`

## Installation

1. Clone this repository or download the script
2. Install the required dependencies:
```bash
pip install faker secrets os
```

## Run The Script

Run the script:
```bash
python complicated-password.py
```


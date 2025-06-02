# Problem 0: Example
def print_greeting():
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

print_greeting()


# Problem 1: Vowel or consonant
def check_letter():
    letter = input("Enter a letter (a-z): ").lower()
    if not letter.isalpha() or len(letter) != 1:
        print("Invalid input. Please enter a single alphabet letter.")
    elif letter in 'aeiou':
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")

check_letter()


# Problem 2: Old enough to vote?
def check_voting_eligibility():
    try:
        age = int(input("Please enter your age: "))
        if age < 0:
            print("Age cannot be negative.")
        elif age >= 18:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

check_voting_eligibility()


# Problem 3: Calculate dog years
def calculate_dog_years():
    try:
        age = int(input("Input a dog's age: "))
        if age < 0:
            print("Age cannot be negative.")
        elif age <= 2:
            dog_years = age * 10
        else:
            dog_years = 20 + (age - 2) * 7
        print(f"The dog's age in dog years is {dog_years}.")
    except ValueError:
        print("Invalid input. Please enter a number.")

calculate_dog_years()


# Problem 4: Weather advice
def weather_advice():
    cold = input("Is it cold? (yes/no): ").strip().lower()
    raining = input("Is it raining? (yes/no): ").strip().lower()

    if cold == "yes" and raining == "yes":
        print("Wear a waterproof coat.")
    elif cold == "yes" and raining == "no":
        print("Wear a warm coat.")
    elif cold == "no" and raining == "yes":
        print("Carry an umbrella.")
    elif cold == "no" and raining == "no":
        print("Wear light clothing.")
    else:
        print("Invalid input. Please answer yes or no.")

weather_advice()


# Problem 5: What’s the season?
def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ").capitalize()
    try:
        day = int(input("Enter the day of the month: "))
        if day < 1 or day > 31:
            print("Invalid day.")
            return

        if (month == "Dec" and day >= 21) or (month in ["Jan", "Feb"]) or (month == "Mar" and day <= 19):
            season = "Winter"
        elif (month == "Mar" and day >= 20) or (month in ["Apr", "May"]) or (month == "Jun" and day <= 20):
            season = "Spring"
        elif (month == "Jun" and day >= 21) or (month in ["Jul", "Aug"]) or (month == "Sep" and day <= 21):
            season = "Summer"
        elif (month == "Sep" and day >= 22) or (month in ["Oct", "Nov"]) or (month == "Dec" and day <= 20):
            season = "Fall"
        else:
            print("Invalid date range.")
            return

        print(f"{month} {day} is in {season}.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the day.")

determine_season()

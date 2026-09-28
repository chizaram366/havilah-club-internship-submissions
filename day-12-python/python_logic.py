# ============================================================
# HAVILAH CLUB INTERNSHIP - DAY 12
# PYTHON LOGIC & FUNCTIONS
# ============================================================


# ============================================================
# EXERCISE 1: GRADE CALCULATOR
# ============================================================

def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


# ============================================================
# EXERCISE 2: MULTIPLICATION TABLE
# ============================================================

def multiplication_table(number):
    print(f"\n===== MULTIPLICATION TABLE FOR {number} =====")

    for multiplier in range(1, 13):
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")


# ============================================================
# EXERCISE 3: TEMPERATURE CONVERTER
# ============================================================

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# ============================================================
# EXERCISE 4: ERROR HANDLING
# ============================================================

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


# ============================================================
# EXERCISE 5: PYTHON UTILITY MENU
# ============================================================

def utility_menu():

    while True:
        print("\n========================================")
        print("         PYTHON UTILITY MENU")
        print("========================================")
        print("1. Grade Calculator")
        print("2. Multiplication Table")
        print("3. Temperature Converter")
        print("4. Exit")
        print("========================================")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            score = get_number("Enter your score (0-100): ")

            if 0 <= score <= 100:
                grade = calculate_grade(score)
                print(f"Score: {score}")
                print(f"Grade: {grade}")
            else:
                print("Invalid score. Please enter a value from 0 to 100.")

        elif choice == "2":
            number = get_number("Enter a number: ")
            multiplication_table(number)

        elif choice == "3":
            celsius = get_number("Enter temperature in Celsius: ")
            fahrenheit = celsius_to_fahrenheit(celsius)

            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

        elif choice == "4":
            print("\nThank you for using the Python Utility!")
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


# ============================================================
# START THE PROGRAM
# ============================================================

print("\n========================================")
print("     HAVILAH CLUB - DAY 12 PYTHON")
print("========================================")
print("Python Logic & Functions")

utility_menu()
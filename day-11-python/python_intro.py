# ============================================================
# HAVILAH CLUB INTERNSHIP - DAY 11
# INTRODUCTION TO PYTHON
# ============================================================


# ============================================================
# EXERCISE 1: STUDENT / ENGINEER INFORMATION
# ============================================================

print("\n===== EXERCISE 1: STUDENT INFORMATION =====")

# Creating variables using different Python data types
student_name = "Chizaram"
student_age = 20
student_gpa = 4.25
is_enrolled = True

# Displaying each value and its data type
print("Student Name:", student_name)
print("Data Type:", type(student_name))

print("Student Age:", student_age)
print("Data Type:", type(student_age))

print("Student GPA:", student_gpa)
print("Data Type:", type(student_gpa))

print("Currently Enrolled:", is_enrolled)
print("Data Type:", type(is_enrolled))


# ============================================================
# EXERCISE 2: BASIC CALCULATOR
# ============================================================

print("\n===== EXERCISE 2: BASIC CALCULATOR =====")

# Asking the user to enter two numbers
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Performing arithmetic operations
sum_result = first_number + second_number
difference_result = first_number - second_number
product_result = first_number * second_number

# Avoiding division by zero
if second_number != 0:
    quotient_result = first_number / second_number
    remainder_result = first_number % second_number
else:
    quotient_result = "Cannot divide by zero"
    remainder_result = "Cannot calculate remainder with zero"

# Displaying the results
print("\n--- Calculation Results ---")
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)
print("Remainder:", remainder_result)


# ============================================================
# EXERCISE 3: TEMPERATURE CONVERTER
# ============================================================

print("\n===== EXERCISE 3: TEMPERATURE CONVERTER =====")

# Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

# Fahrenheit to Kelvin
fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))

kelvin = (fahrenheit_input - 32) * 5 / 9 + 273.15

print(f"{fahrenheit_input}°F is equal to {kelvin:.2f} K")


# ============================================================
# EXERCISE 4: ROBOT SENSOR MONITOR
# ============================================================

print("\n===== EXERCISE 4: ROBOT SENSOR MONITOR =====")

# Collecting robot information from the user
robot_name = input("Enter Robot Name: ")
robot_id = input("Enter Robot ID: ")
sensor_name = input("Enter Sensor Name: ")

# Converting sensor values to floating-point numbers
sensor_reading = float(input("Enter Sensor Reading: "))
operating_limit = float(input("Enter Operating Limit: "))

# Calculating the difference between the operating limit
# and the current sensor reading
difference = operating_limit - sensor_reading

# Determining the sensor status
if sensor_reading <= operating_limit:
    status = "Within Operating Limit"
else:
    status = "EXCEEDS Operating Limit"

# Displaying the robot sensor report
print("\n========================================")
print("         ROBOT SENSOR REPORT")
print("========================================")
print("Robot Name:", robot_name)
print("Robot ID:", robot_id)
print("Sensor Name:", sensor_name)
print("Sensor Reading:", sensor_reading)
print("Operating Limit:", operating_limit)
print("Difference:", difference)
print("Status:", status)
print("========================================")
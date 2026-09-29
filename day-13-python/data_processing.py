# ============================================================
# HAVILAH CLUB INTERNSHIP - DAY 13
# WORKING WITH DATA
# ============================================================

import csv


# ============================================================
# EXERCISE 2 & 3: READ, CLEAN AND CONVERT THE DATA
# ============================================================

def load_data(filename):
    records = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["name"] = row["name"].strip()
            row["department"] = row["department"].strip().lower()
            row["score"] = float(row["score"])
            row["level"] = int(row["level"])

            records.append(row)

    return records


# ============================================================
# EXERCISE 4: ANALYSE THE DATA
# ============================================================

def calculate_summary(records):
    scores = [record["score"] for record in records]

    total_records = len(records)
    minimum_score = min(scores)
    maximum_score = max(scores)
    average_score = sum(scores) / len(scores)

    return total_records, minimum_score, maximum_score, average_score


# ============================================================
# EXERCISE 5: FILTER THE RECORDS
# ============================================================

def filter_records(records, minimum_score):
    filtered_records = []

    for record in records:
        if record["score"] >= minimum_score:
            filtered_records.append(record)

    return filtered_records


# ============================================================
# EXERCISE 6: SORT AND SAVE THE RESULTS
# ============================================================

def save_results(filename, records):
    fieldnames = ["name", "score", "department", "level"]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(records)


# ============================================================
# MAIN PROGRAM
# ============================================================

print("\n========================================")
print("     HAVILAH CLUB - DAY 13")
print("        WORKING WITH DATA")
print("========================================")

input_file = "students.csv"
output_file = "processed_students.csv"

# Read and process the dataset
students = load_data(input_file)

print("\n===== DATASET LOADED =====")
print("Records loaded:", len(students))

# Analyse the dataset
total, minimum, maximum, average = calculate_summary(students)

print("\n===== DATA SUMMARY =====")
print("Total Records:", total)
print("Minimum Score:", minimum)
print("Maximum Score:", maximum)
print(f"Average Score: {average:.2f}")

# Filter records
passing_students = filter_records(students, 70)

print("\n===== STUDENTS WITH SCORE 70 OR HIGHER =====")

for student in passing_students:
    print(
        f"{student['name']} | "
        f"Score: {student['score']} | "
        f"Department: {student['department']} | "
        f"Level: {student['level']}"
    )

# Sort filtered records from highest to lowest score
passing_students.sort(key=lambda student: student["score"], reverse=True)

print("\n===== SORTED RESULTS =====")

for student in passing_students:
    print(f"{student['name']} - {student['score']}")

# Save processed results
save_results(output_file, passing_students)

print("\n===== FILE SAVED =====")
print(f"Processed results saved to: {output_file}")
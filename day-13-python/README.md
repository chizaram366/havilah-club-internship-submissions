\# Havilah Club Internship — Day 13



\## Working With Data



This project contains my Day 13 Python data-processing exercises for the Havilah Club Internship.



The project demonstrates how to work with structured CSV data using Python, including reading records, cleaning and converting values, analysing data, filtering records, sorting results, and writing processed data to a new CSV file.



\## Dataset



The project uses a student dataset containing 20 records with the following fields:



\* Name

\* Score

\* Department

\* Level



The dataset is stored in `students.csv`.



\## Exercises



\### Exercise 1 — Create the Dataset



Created a CSV dataset containing 20 student records with four columns:



\* Name

\* Score

\* Department

\* Level



\### Exercise 2 — Read the Dataset



Used Python's `csv` module and `csv.DictReader` to read the CSV file.



The records are stored as a list of dictionaries, allowing each student's information to be accessed using column names.



\### Exercise 3 — Clean and Convert the Data



Cleaned text values using:



\* `strip()` to remove unnecessary spaces

\* `lower()` to standardise department names



The score values were converted from strings to `float` values, while level values were converted to integers.



\### Exercise 4 — Analyse the Dataset



Created a data summary showing:



\* Total records: 20

\* Minimum score: 45.0

\* Maximum score: 95.0

\* Average score: 72.50



Python functions such as `min()`, `max()`, `sum()`, and `len()` were used for the analysis.



\### Exercise 5 — Filter the Records



Filtered the dataset to select students who scored 70 or higher.



The filter produced 12 qualifying student records.



\### Exercise 6 — Sort and Save the Results



The filtered records were sorted from the highest score to the lowest score.



The sorted results were written to `processed\_students.csv` using `csv.DictWriter`, including the column headers.



\### Exercise 7 — Apply Functions



Functions were used to organise the data-processing workflow:



\* `load\_data()` — reads, cleans, and converts the dataset

\* `calculate\_summary()` — calculates the dataset statistics

\* `filter\_records()` — selects records based on a score condition

\* `save\_results()` — writes the processed records to a new CSV file



\## Technologies Used



\* Python

\* CSV

\* Visual Studio Code

\* Git

\* GitHub



\## Project Structure



```text

day-13-python/

├── README.md

├── data\_processing.py

├── students.csv

├── processed\_students.csv

└── screenshots/

&#x20;   ├── Screenshot 1.png

&#x20;   ├── Screenshot 2.png

&#x20;   ├── Screenshot 3.png

&#x20;   └── Screenshot 2026-09-29 112731.png

```



\## What I Learned



This exercise helped me understand how Python can be used to process structured data.



I practised reading CSV files with `DictReader`, representing data as lists of dictionaries, cleaning text values, converting strings to numerical values, calculating statistics, filtering and sorting records, and exporting processed results with `DictWriter`.



I also gained more experience organising data-processing logic into reusable Python functions.


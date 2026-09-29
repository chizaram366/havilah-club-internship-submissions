\# Week 3 Day 14 — Python + APIs



\## Project Overview



This project demonstrates how to use Python to communicate with a public REST API, receive JSON data, parse the response, and display useful information in a clear format.



For this project, I used the \*\*Open Library Search API\*\*.



The API provides information about books and does not require an API key.



\## API Used



\*\*API:\*\* Open Library Search API



\*\*Base Endpoint:\*\*



`https://openlibrary.org/search.json`



\*\*HTTP Method:\*\* GET



\*\*Authentication:\*\* None required



\### Query Parameters



The program uses these parameters:



| Parameter | Description                            |

| --------- | -------------------------------------- |

| `q`       | The book title, author, or search term |

| `limit`   | The maximum number of results returned |



Example request:



`https://openlibrary.org/search.json?q=harry+potter\&limit=5`



\## JSON Response Structure



The API returns a JSON object containing information such as:



\* `numFound` — the number of matching results

\* `docs` — a list containing individual book records



Each book record can contain fields such as:



\* `title` — book title

\* `author\_name` — list of authors

\* `first\_publish\_year` — first publication year

\* `edition\_count` — number of editions



The Python program accesses the `docs` list and loops through the returned books.



\## What the Program Does



The program:



1\. Asks the user to enter a book search query.

2\. Sends a GET request to the Open Library API.

3\. Prints the HTTP status code.

4\. Prints the final request URL.

5\. Checks whether the request was successful.

6\. Converts the response into JSON using `.json()`.

7\. Extracts book information using dictionary access.

8\. Loops through the results.

9\. Displays the title, author, first publication year, and number of editions.

10\. Handles network errors using `requests.exceptions.RequestException`.



\## Error Handling



The program checks the HTTP status code before processing the JSON response.



It also uses `try` and `except` to handle request-related errors.



If the API request fails, the program displays an error message instead of crashing.



\## Python Environment



A Python virtual environment was created for this project:



```text

.venv

```



The virtual environment contains the required `requests` and `pytest` packages.



The `.venv` directory is excluded from Git using `.gitignore`.



\## Installation



From the Day 14 project directory, create a virtual environment with:



```powershell

python -m venv .venv

```



Install the required package:



```powershell

.\\.venv\\Scripts\\python.exe -m pip install requests

```



Pytest can be installed for running the instructor tests:



```powershell

.\\.venv\\Scripts\\python.exe -m pip install pytest

```



\## Running the Program



From the repository root:



```powershell

.\\week-3\\day-14-python-apis\\.venv\\Scripts\\python.exe .\\week-3\\day-14-python-apis\\main.py

```



The program will ask:



```text

Enter a book search query:

```



Enter a search such as:



```text

harry potter

```



or:



```text

atomic habits

```



\## Example Output



```text

========================================

&#x20;    HAVILAH CLUB - DAY 14

&#x20;         PYTHON + APIs

========================================



Enter a book search query: atomic habits



===== API REQUEST =====

Status Code: 200

Request URL: https://openlibrary.org/search.json?q=atomic+habits\&limit=5



===== JSON RESPONSE TYPE =====

dict



===== BOOK SEARCH RESULTS =====



Book 1

Title: Atomic Habits

Author: James Clear

First Publication Year: 2016

Number of Editions: 42

```



The exact results may change because the API data can be updated over time.



\## Testing



The instructor-provided tests can be run from the repository root with:



```powershell

.\\week-3\\day-14-python-apis\\.venv\\Scripts\\python.exe -m pytest .\\week-3\\day-14-python-apis\\test\_main.py

```



All six instructor tests currently pass.



\## Security



This API does not require an API key.



The project still includes `.env.example` as required by the assignment. Any real `.env` file is excluded through `.gitignore` and must not be committed.



\## Project Files



```text

day-14-python-apis/

├── .env.example

├── .gitignore

├── main.py

├── README.md

└── test\_main.py

```




# ============================================================
# HAVILAH CLUB INTERNSHIP - DAY 14
# PYTHON + APIs
# ============================================================

import requests


# Open Library Search API
# This API is free and does not require an API key.
BASE_URL = "https://openlibrary.org/search.json"


# ============================================================
# STEP 1: FETCH DATA
# ============================================================

def fetch_data(query):
    """Fetch book data from the Open Library API."""

    params = {
        "q": query,
        "limit": 5
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        print("\n===== API REQUEST =====")
        print("Status Code:", response.status_code)
        print("Request URL:", response.url)

        if response.status_code != 200:
            print("API request failed.")
            return None

        data = response.json()

        print("\n===== JSON RESPONSE TYPE =====")
        print(type(data).__name__)

        return data

    except requests.exceptions.RequestException as error:
        print("\nNetwork error occurred:")
        print(error)
        return None


# ============================================================
# STEP 2: PARSE AND DISPLAY
# ============================================================

def display_results(data):
    """Extract and display useful information from the API response."""

    if not data:
        print("No data was returned.")
        return

    books = data.get("docs", [])

    if not books:
        print("No books found.")
        return

    print("\n===== BOOK SEARCH RESULTS =====")

    for number, book in enumerate(books, start=1):
        title = book.get("title", "Unknown title")

        authors = book.get("author_name", ["Unknown author"])
        author = ", ".join(authors[:2])

        year = book.get("first_publish_year", "Unknown")

        editions = book.get("edition_count", "Unknown")

        print(f"\nBook {number}")
        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"First Publication Year: {year}")
        print(f"Number of Editions: {editions}")


# ============================================================
# MAIN
# ============================================================

def main():
    print("\n========================================")
    print("     HAVILAH CLUB - DAY 14")
    print("          PYTHON + APIs")
    print("========================================")

    query = input("\nEnter a book search query: ").strip()

    if not query:
        print("Please enter a search query.")
        return

    data = fetch_data(query)

    if data:
        display_results(data)


if __name__ == "__main__":
    main()
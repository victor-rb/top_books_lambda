import requests
from bs4 import BeautifulSoup

def craw_page():
    try:
        response = requests.get('https://openlibrary.org/trending/daily')
        response.raise_for_status()
    except requests.RequestException as error:
        print(f"Error fetching the page: {error}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    books = []

    for tag in soup.find_all('div', {'class': 'details'}):
        books.append({
            'title': tag.find('h3', {'class': 'booktitle'}).text.strip(),
            'author': tag.find('span', {'class': 'bookauthor'}).text.strip(),
            'year': tag.find('span', {'class': 'resultDetails'}).text.strip().removeprefix(
                'First published in ')[0:4]
        })
    return books

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": craw_page()
    }
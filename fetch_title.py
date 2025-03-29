import requests
from bs4 import BeautifulSoup
import sys

def fetch_title(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip()
        return title
    except Exception as e:
        return f"Error fetching title: {e}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python fetch_title.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    title = fetch_title(url)
    print(f"[{title}]({url})")

if __name__ == "__main__":
    main()


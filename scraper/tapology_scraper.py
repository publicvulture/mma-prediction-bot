import requests
from bs4 import BeautifulSoup

def fetch_upcoming_fights():
    url = "https://www.tapology.com/fightcenter"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Parse and return fights as a list of dicts
    # Simplified placeholder below
    return [{
        "fighter1": "Fighter A",
        "fighter2": "Fighter B",
        "event_name": "UFC 300",
        "event_date": "2025-08-15",
        "organization": "UFC"
    }]

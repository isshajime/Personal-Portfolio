import requests
from flask import current_app as app
from .models import Quote, db
from datetime import date

today_date = date.today()

def retrieve_and_store_data():
    zen_quotes_endpoint = 'https://zenquotes.io/api/today/'
    response = requests.get(zen_quotes_endpoint)
    response.raise_for_status()
    zen_data = response.json()[0]
    daily_quote = Quote(date=today_date, quote=zen_data['q'], author=zen_data['a'])
    daily_quote.save_to_db()
    
# SI 206 Winter 2019
# Final Project
# Eva Smith

from news_info import news_api
from newsapi import NewsApiClient
import sqlite3


def news_scrape():
    api = NewsApiClient(api_key = news_api)

    conn = sqlite3.connect('Eva_test.sqlite')
    cur = conn.cursor()

    #cur.execute('CREATE TABLE IF NOT EXISTS News()')
    requests = api.get_everything(q='politics') #returns dictionary

if __name__ == "__main__":
    news_scrape()
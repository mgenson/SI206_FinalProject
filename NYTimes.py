from nyt_info import nyt_key
import sqlite3
from nytimesarticle import articleAPI


def scrape_nyt_politics():
    api = articleAPI(nyt_key)

    #make connection to database
    conn = sqlite3.connect("NYT.sqlite")
    cur = conn.cursor()
    #cur.execute("CREATE TABLE IF DOESN'T EXIST")
    results = api.search( q = 'Obama' )
    print(results)
if __name__ == '__main__':
    scrape_nyt_politics()



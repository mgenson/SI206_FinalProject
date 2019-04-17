from nyt_info import nyt_key
import sqlite3
from nytimesarticle import articleAPI
import json


def scrape_nyt_politics():
    api = articleAPI(nyt_key)
    bush_dict = api.search(q="Immigration", begin_date = 20010120, end_date = 20010430)
    obama_dict = api.search(q = 'Immigration', begin_date = 20080120, end_date = 20080429)
    trump_dict = api.search(q = "Immigration", begin_date = 20160120, end_date = 20160429)
    #getting into docs
    bush = bush_dict["response"]
    obama = obama_dict["response"]
    trump = trump_dict["response"]
    print(bush)
    # Make bush json
    dumped_json_bush = json.dumps(bush)
    bw = open("bush_json","w")
    bw.write(dumped_json_bush)
    bw.close() 
    #make obama json
    dumped_json_obama = json.dumps(obama)
    ow = open("obama_json", "w")
    ow.write(dumped_json_obama)
    ow.close
    #make trump json
    dumped_json_trump = json.dumps(trump)
    tw = open
    tw.write("trump_json", "w")
    tw.close()
def data_nyt(dumped_json_bush, dumped_json_obama, dumped_json_trump):   

    #make connection to database
    conn = sqlite3.connect("NYT.sqlite")
    cur = conn.cursor()
    #cur.execute("CREATE TABLE IF DOESN'T EXIST")
def visual_nyt()
    
    
if __name__ == '__main__':
    scrape_nyt_politics()



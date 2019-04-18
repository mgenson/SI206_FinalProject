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
    bush = bush_dict["response"]["docs"][0]
    
    obama = obama_dict["response"]['docs'][0]
    trump = trump_dict["response"]["docs"][0]
    print("BUSH", bush,"OBAMA", obama,"TRUMP", trump)
    # Make bush json
    dumped_json_bush = json.dumps(bush)
    bush_json = open(bush ,"w")
    bush_json.write(dumped_json_bush)
    bush_json.close() 
    #make obama json
    dumped_json_obama = json.dumps(obama)
    obama_json = open(obama, "w")
    obama_json.write(dumped_json_obama)
    obama_json.close
    #make trump json
    dumped_json_trump = json.dumps(trump)
    trump_json = open(trump, "w")
    trump_json.write(dumped_json_trump)
    trump_json.close()
#def data_nyt(dumped_json_bush, dumped_json_obama, dumped_json_trump):   

    #make connection to database
    #conn = sqlite3.connect("NYT.sqlite")
    #cur = conn.cursor()
    #cur.execute("CREATE TABLE IF DOESN'T EXIST NYT")
    #cur.execute("CREATE TABLE NYT(")
#def visual_nyt()
    
    
if __name__ == '__main__':
    scrape_nyt_politics()



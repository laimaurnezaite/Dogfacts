import json
import sqlite3


db = sqlite3.connect("dogfacts_project/db.sqlite3")

with open("all_facts.json", "r") as json_file:
    data = json.load(json_file)

  
    for p in data['all']:
        db.execute("INSERT INTO facts_fact (text, type, user_id) VALUES (:text, :type, :user_id);",
            {"text":p["text"], "type":p["type"], "user_id":4})
        db.commit()



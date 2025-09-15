#here I load data through shell/terminal of VS. but for that I have to install "Mongo DB Tools"
#Ungip that "Mongo DB Tool" folder and open bin folder & check "mongoimport.exe" file is present their or not
#copy their path ( C:\Users\gaura-----------\bin ) & open "environment variable"->"user variable for gaura"-> double click on "path" then "New" then pasr the copy path"
#open shell or terminal in VS & type "mongoimport --version" to check it
#Now move to root folder of our project(here "cd "C:\Users\gaura\OneDrive\Desktop\mongo2snowflake-etl"") where my data is stored in .jsonl file 
#then write this cmd for import data im mongoDB by locally
#mongoimport --uri "mongodb://localhost:27017" --db retail_db --collection customers --file .\data\customers.jsonl
#mongoimport --uri "mongodb://localhost:27017" --db retail_db --collection products  --file .\data\products.jsonl
#mongoimport --uri "mongodb://localhost:27017" --db retail_db --collection orders    --file .\data\orders.jsonl
#mongoimport --uri "mongodb://localhost:27017" --db retail_db --collection reviews   --file .\data\reviews.jsonl

#How to check data is load or not
# type "mongosh"->"show dbs"->"use retail_db"->"show collection"

import os, json
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "retail_db")
DATA_DIR = "../data" 

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]

def load_collection(filename, coll_name):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        batch = []
        for line in f:
            obj = json.loads(line)
            batch.append(obj)
            if len(batch) >= 500:
                db[coll_name].insert_many(batch)
                batch = []
        if batch:
            db[coll_name].insert_many(batch)
    print(f"Loaded {coll_name} from {path}")

if __name__ == "__main__":
    load_collection("customers.jsonl", "customers")
    load_collection("products.jsonl", "products")
    load_collection("orders.jsonl", "orders")
    load_collection("reviews.jsonl", "reviews")

#How to run this script
#python scripts/load_data_to_mongo.py
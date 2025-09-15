import os
import json
from pymongo import MongoClient
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
MONGO_URI = os.getenv("mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "retail_db")

# Ensure data/raw folder is in project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(PROJECT_ROOT, "data", "raw")
os.makedirs(OUTDIR, exist_ok=True)

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]

# Function to dump a collection to JSONL
def dump_collection(coll_name):
    docs = list(db[coll_name].find({}))
    filepath = os.path.join(OUTDIR, f"{coll_name}.jsonl")
    with open(filepath, "w", encoding="utf-8") as f:
        for d in docs:
            # convert ObjectId to string
            d["_id"] = str(d.get("_id"))
            f.write(json.dumps(d, default=str) + "\n")
    print(f"Dumped {coll_name} -> {filepath}")

# Dump all collections
if __name__ == "__main__":
    for c in ["customers", "products", "orders", "reviews"]:
        dump_collection(c)

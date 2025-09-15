import os, json
import pandas as pd
from dotenv import load_dotenv

# Load environment variables if needed
load_dotenv()

# Define input/output folders
RAW = "data/raw"
STAGED = "data/staged"
os.makedirs(STAGED, exist_ok=True) 

# 1. Customers (Dimension table)
customers = pd.read_json(os.path.join(RAW, "customers.jsonl"), lines=True)

# Drop MongoDB "_id" if present
if "_id" in customers.columns:
    customers = customers.drop(columns=["_id"])

customers.to_csv(os.path.join(STAGED, "dim_customers.csv"), index=False)

# 2. Products (Dimension table)
products = pd.read_json(os.path.join(RAW, "products.jsonl"), lines=True)

if "_id" in products.columns:
    products = products.drop(columns=["_id"])

products.to_csv(os.path.join(STAGED, "dim_products.csv"), index=False)

# 3. Orders + Order Items (Fact tables)
orders = []
order_items_rows = []

with open(os.path.join(RAW, "orders.jsonl"), "r", encoding="utf-8") as f:
    for line in f:
        o = json.loads(line)
        orders.append({
            "order_id": o["order_id"],
            "customer_id": o["customer_id"],
            "order_date": o["order_date"],
            "num_items": o.get("num_items", 0),
            "order_total": o.get("order_total", 0.0),
            "shipping_city": o.get("shipping_city"),
            "status": o.get("status")
        })
        # Flatten order items
        for it in o.get("items", []):
            order_items_rows.append({
                "order_id": o["order_id"],
                "customer_id": o["customer_id"],
                "order_date": o["order_date"],
                "product_id": it["product_id"],
                "quantity": it["quantity"],
                "unit_price": it["unit_price"],
                "item_total": it["item_total"]
            })

orders_df = pd.DataFrame(orders)
order_items_df = pd.DataFrame(order_items_rows)

orders_df.to_csv(os.path.join(STAGED, "fact_orders.csv"), index=False)
order_items_df.to_csv(os.path.join(STAGED, "fact_order_items.csv"), index=False)

# 4. Reviews (Fact table)
reviews = pd.read_json(os.path.join(RAW, "reviews.jsonl"), lines=True)

if "_id" in reviews.columns:
    reviews = reviews.drop(columns=["_id"])

reviews.to_csv(os.path.join(STAGED, "fact_reviews.csv"), index=False)

print("Staged CSVs written to", STAGED)
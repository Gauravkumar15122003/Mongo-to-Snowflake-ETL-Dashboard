import os
import pandas as pd
from dotenv import load_dotenv
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

# Load environment variables
load_dotenv()
SNOW_USER = os.getenv("SNOW_USER")
SNOW_PASSWORD = os.getenv("SNOW_PASSWORD")
SNOW_ACCOUNT = os.getenv("SNOW_ACCOUNT")
SNOW_WAREHOUSE = os.getenv("SNOW_WAREHOUSE")
SNOW_DATABASE = os.getenv("SNOW_DATABASE")
SNOW_SCHEMA = os.getenv("SNOW_SCHEMA")
SNOW_ROLE = os.getenv("SNOW_ROLE")

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=SNOW_USER,
    password=SNOW_PASSWORD,
    account=SNOW_ACCOUNT,
    warehouse=SNOW_WAREHOUSE,
    database=SNOW_DATABASE,
    schema=SNOW_SCHEMA,
    role=SNOW_ROLE
)

# Ensure session uses correct database and schema
conn.cursor().execute(f"USE DATABASE {SNOW_DATABASE}")
conn.cursor().execute(f"USE SCHEMA {SNOW_SCHEMA}")

# Load staged CSVs
staged = "data/staged"
df_customers = pd.read_csv(os.path.join(staged, "dim_customers.csv"))
df_products = pd.read_csv(os.path.join(staged, "dim_products.csv"))
df_orders = pd.read_csv(os.path.join(staged, "fact_orders.csv"))
df_items = pd.read_csv(os.path.join(staged, "fact_order_items.csv"))
df_reviews = pd.read_csv(os.path.join(staged, "fact_reviews.csv"))

# Rename invalid columns for Snowflake (uppercase, valid names)
for df in [df_customers, df_products, df_orders, df_items, df_reviews]:
    new_cols = {}
    for col in df.columns:
        new_col = col.strip().replace(" ", "_").replace("-", "_")
        if new_col.startswith("_"):
            new_col = new_col[1:]
        new_col = new_col.upper()  # Snowflake prefers uppercase
        new_cols[col] = new_col
    df.rename(columns=new_cols, inplace=True)

# Write DataFrames to Snowflake
write_pandas(conn, df_customers, 'DIM_CUSTOMERS')
write_pandas(conn, df_products, 'DIM_PRODUCTS')
write_pandas(conn, df_orders, 'FACT_ORDERS')
write_pandas(conn, df_items, 'FACT_ORDER_ITEMS')
write_pandas(conn, df_reviews, 'FACT_REVIEWS')

# Close connection
conn.close()
print("Loaded staged CSVs into Snowflake tables successfully!")
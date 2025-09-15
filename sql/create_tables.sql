--write these queris in the workbench of snowflake

CREATE DATABASE IF NOT EXISTS MY_DB;
USE DATABASE MY_DB;

CREATE SCHEMA IF NOT EXISTS PUBLIC;
USE SCHEMA PUBLIC;

CREATE OR REPLACE TABLE DIM_CUSTOMERS (
  customer_id STRING,
  name STRING,
  email STRING,
  city STRING,
  signup_date TIMESTAMP_NTZ,
  preferred_category STRING
);

CREATE OR REPLACE TABLE DIM_PRODUCTS (
  product_id STRING,
  name STRING,
  category STRING,
  price FLOAT,
  stock INT
);

CREATE OR REPLACE TABLE FACT_ORDERS (
  order_id STRING,
  customer_id STRING,
  order_date TIMESTAMP_NTZ,
  num_items INT,
  order_total FLOAT,
  shipping_city STRING,
  status STRING
);

CREATE OR REPLACE TABLE FACT_ORDER_ITEMS (
  order_id STRING,
  customer_id STRING,
  order_date TIMESTAMP_NTZ,
  product_id STRING,
  quantity INT,
  unit_price FLOAT,
  item_total FLOAT
);

CREATE OR REPLACE TABLE FACT_REVIEWS (
  review_id STRING,
  customer_id STRING,
  product_id STRING,
  rating INT,
  review_text STRING,
  review_date TIMESTAMP_NTZ
);
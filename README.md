# MongoDB to Snowflake ETL & Power BI Dashboard

![Project Logo](Pic/Project_Workflow.png)  

## Overview
This project demonstrates an end-to-end **ETL pipeline** where data is extracted from **MongoDB**, transformed, and loaded into **Snowflake**. Insights from the data are visualized using **Power BI** dashboards. 

The pipeline is designed to be simple, efficient, and scalable for retail/analytics datasets.

---

## Project Features
- Extracts data from MongoDB collections.
- Transforms nested and unstructured data into structured tables.
- Loads transformed data into Snowflake tables.
- Power BI dashboard for visualizing trends, metrics, and KPIs.
- Includes multiple visualization types like bar charts, line charts, and heatmaps.
- Clean, organized code structure for ETL scripts and dashboard files.

---

## Folder Structure
.
├── pic/ # Images used in README or dashboard
├── scripts/ # Python scripts for ETL (extract, transform, load)
├── data/ # Sample datasets as a input(optional)
├── PowerBI_Dashboard/ # Power BI files (.pbix)

## Screenshots
### Data Set before Processing
I have a retail_db database that contains four collections: customers, orders, products, and reviews. Each collection has thousands of documents on which we are performing our tasks
![Data](Pic/Data.png) 

### Number of Records in each Documents - Mongo Compass
![Data](Pic/Mongo_Compass.png) 

### Structure of Data - Mongo Shell
Data view in Mongo Shell, displayed in JSON format.
![Data](Pic/Mongo_Shell.png) 

### How to Switch to DB, Collections & Documents through Terminal
![Data](Pic/NoSQL_DB.png) 

### Database, Schema, and Table Creation in Snowflake
It shows the creation of a database, schema, and tables in **Snowflake** to store data coming from **MongoDB**.  
The workflow followed:
1. **Extract:** Data is extracted from MongoDB using a Python script and stored in the **raw** layer.  
2. **Transform:** The extracted data is cleaned and transformed using Python scripts.
3. **Load:** The transformed data is then loaded into these **Snowflake tables** (staged layer) for further analysis.

### Data Cleaning & Transformation
In this step, we performed several data cleaning operations to prepare the dataset for analysis, including:
- **Renaming attributes** to make them consistent and meaningful.
- **Removing the `_id` attribute** which was not required for further processing.
- **Restructuring nested data** to simplify the schema and make it easier to query.
![Data](Pic/DDL.png) 

### Analytics Query Results in Snowflake (Snowsight)
It shows the result of an analytical query executed in **Snowflake Snowsight**.  
The query retrieves product-level revenue data after performing transformations and loading the cleaned dataset into Snowflake tables.
![Data](Pic/Snowsight.png) 

> Add as many screenshots from your `pic` folder as needed.  

---

## Tech Stack
- **MongoDB**: Source database for raw data.
- **Python**: ETL scripts using pandas and pymongo.
- **Snowflake**: Cloud-based data warehouse.
- **Power BI**: Data visualization and reporting.

---

## How to Run
1. Clone the repository:  
   git clone https://github.com/your-username/mongo-to-snowflake-etl-dashboard.git
Install Python dependencies:

pip install -r requirements.txt
Update config.py with your MongoDB and Snowflake credentials.

Run ETL scripts in order:

python scripts/extract_mongo.py
python scripts/transform.py
python scripts/load_to_snowflake.py
Open the Power BI dashboard (PowerBI_Dashboard/project_dashboard.pbix) and connect to Snowflake.

Sample Data
If your dataset is large, provide a small sample in data/sample_data/.

Include instructions for connecting MongoDB collections or Snowflake tables.

Author
Gaurav Kumar

Data Engineering & Analytics Enthusiast

Linkedln: https://www.linkedin.com/in/gaurav-kumar-4124732a4/

License
This project is licensed under the MIT License.

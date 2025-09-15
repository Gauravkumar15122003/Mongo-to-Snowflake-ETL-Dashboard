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
### Dashboard Overview
![Dashboard Overview](pic/dashboard_overview.png)

### Sales Analysis
![Sales Analysis](pic/sales_analysis.png)

### Customer Insights
![Customer Insights](pic/customer_insights.png)


### Dashboard Overview
![Dashboard Overview](pic/dashboard_overview.png)

### Sales Analysis
![Sales Analysis](pic/sales_analysis.png)

### Customer Insights
![Customer Insights](pic/customer_insights.png)

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

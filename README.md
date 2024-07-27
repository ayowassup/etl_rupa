# ETL Pipeline for Extracting Product Data with Python and SQLite

This project is an automated ETL (Extract, Transform, Load) pipeline designed to efficiently extract product data from the e-commerce platform ruparupa.com. The pipeline systematically gathers product information such as names, prices (including discounts), ratings, URLs, and image links, and stores it in a structured SQLite database for analysis and further use.

## Table of Contents

- [ETL Pipeline for Extracting Product Data with Python and SQLite](#etl-pipeline-for-extracting-product-data-with-python-and-sqlite)
  - [Table of Contents](#table-of-contents)
  - [Project Description](#project-description)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Project Structure](#project-structure)
  - [Usage](#usage)
    - [1. Extract Data](#1-extract-data)
    - [2. Transform Data](#2-transform-data)
    - [3. Load Data](#3-load-data)
  - [Database Schema](#database-schema)
  - [ETL Process Diagram](#etl-process-diagram)

## Project Description

The goal of this project is to build an ETL pipeline that extracts product information from the e-commerce website: ruparupa.com. The extracted data includes product names, prices (both discounted and non-discounted), ratings, URLs, and image links. After extraction, the data undergoes transformation to clean and format it appropriately. Finally, the transformed data is loaded into a SQLite database for analysis and further use.

This project demonstrates an automated solution for collecting, transforming, and storing data. The modular structure with separate scripts for each stage of the ETL process, simplifies maintenance and allows for updates as needed.

## Requirements

- Python 3.8 or above
- curl_cffi
- BeautifulSoup4
- sqlite3

## Project Structure

```plaintext
etl_rupa/
│
├── extract.py                  # Extraction script
├── transform.py                # Transformation script
├── load.py                     # Loading script
├── requirements.txt            # Project dependencies
├── raw_products.json           # Raw products data
└── transformed_products.json   # Transformed products data
```

## Installation
1. Clone this repository:

   ```sh
   git clone https://github.com/ayowassup/etl_rupa.git
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Extract data:
   
    ```sh
    python extract.py
    ```

   This will create `raw_products.json` containing the raw scraped data.

    
3. Transform data:
   
   ```sh
    python transform.py
   ```

   This will create `transformed_products.json` containing the cleaned and formatted data.

   
3. Load data:
   
   ```sh
   python load.py
   ```

   This will create a SQLite database named `etl.db` and populate it with the transformed product data.

## Database Schema
```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    final_price TEXT,
    initial_price TEXT,
    discounted TEXT,
    rating TEXT,
    product_url TEXT,
    image_url TEXT
);
```

## ETL Process Diagram
![ETL Process Diagram](https://github.com/user-attachments/assets/81624225-754b-42f2-887c-a699654bd0c7)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


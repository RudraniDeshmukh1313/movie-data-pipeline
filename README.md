# Movie Data Pipeline

This project implements an end-to-end ETL (Extract, Transform, Load) pipeline using Python to process and store movie data efficiently.

## 🚀 Features
- Extracts raw movie data from CSV
- Cleans missing values and removes duplicates
- Transforms data (filters recent movies, adds new features)
- Loads processed data into SQLite database

## 🛠 Tech Stack
- Python
- Pandas
- SQLite

## 📂 Project Structure
movie-data-pipeline/
│
├── pipeline.py
├── README.md

## ▶️ How to Run
1. Install dependencies:
pip install pandas

2. Run the pipeline:
python pipeline.py

## 📊 Output
- Creates a SQLite database (`db.sqlite`)
- Stores cleaned data in a `movies` table

## 💡 Key Learnings
- Built a modular ETL pipeline
- Worked with real-world data cleaning techniques
- Implemented structured data storage using SQL

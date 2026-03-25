# Movie Data Pipeline

This project implements an end-to-end ETL (Extract, Transform, Load) pipeline using Python.

## Features
- Extracts movie data from a CSV file
- Cleans and processes data using Pandas
- Removes missing values and duplicates
- Stores structured data in SQLite database

## Tech Stack
- Python
- Pandas
- SQLite

## Project Structure
movie-data-pipeline/
│
├── pipeline.py
├── README.md

## How to Run
1. Install dependencies:
pip install pandas

2. Run the pipeline:
python pipeline.py

## Output
- Creates a SQLite database (`db.sqlite`)
- Stores cleaned movie data in `movies` table

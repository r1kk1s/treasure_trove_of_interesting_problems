# async write data to databases

## The purpose of this mini application is to create some amount of CSV files of 10_000 rows each with data in any format and then write all data to db concurrently and measure the result.

### Create virtual environment (venv)

`python3 -m venv .venv`

### Activate venv

`. .venv/bin/activate`

### Install necessary requirements

`pip install -r requirements.txt`

### Run postgresql

`docker-compose up -d`

### Run this application

`python main.py`

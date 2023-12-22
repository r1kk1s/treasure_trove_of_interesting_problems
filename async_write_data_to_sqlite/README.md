# async write data to sqlite

## The purpose of this mini application is to create 7 CSV files of 10_000 rows each with data in any format and then write all data to sqlite concurrently.
## After testing I found that the fastest way is to concurrently read files and write sequentyally in sqlite, since each row of data is written so quickly that using an event loop with coroutines to write data will slow down the process.
### It takes 0.7s on my machine (MacBook Air M2 16GB RAM 8-core processor)

### Create virtual environment (venv)

`python3 -m venv .venv`

### Activate venv

`. .venv/bin/activate`

### Install necessary requirements

`pip install -r requirements.txt`

### Run this application

`python main.py`

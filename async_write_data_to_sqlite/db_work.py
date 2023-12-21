import os
import sqlite3


PATH_TO_DB = "db"
DB = "db.sqlite"

if not os.path.exists(PATH_TO_DB):
    os.mkdir(PATH_TO_DB)

if not os.path.exists(f"{PATH_TO_DB}/{DB}"):
    open(f"{PATH_TO_DB}/{DB}", "w").close()


CREATE_TABLE_QUERY = f"""
CREATE TABLE IF NOT EXISTS my_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    int_col INTEGER,
    float_col REAL,
    str_col TEXT,
    bool_col BOOLEAN,
    int_col_2 INTEGER,
    array_col TEXT,
    json_col TEXT,
    int_col_3 INTEGER,
    bool_col_2 BOOLEAN,
    bool_col_3 BOOLEAN
)"""


INSERT_QUERY = f"""
INSERT INTO my_table (int_col, float_col, str_col, bool_col, int_col_2,
                          array_col, json_col, int_col_3, bool_col_2, bool_col_3)
VALUES
    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""


def create_table() -> None:
    with sqlite3.connect(f"{PATH_TO_DB}/{DB}") as conn:
        conn.execute(CREATE_TABLE_QUERY)
        conn.commit()

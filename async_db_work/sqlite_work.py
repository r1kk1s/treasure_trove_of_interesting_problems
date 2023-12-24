import aiosqlite

import os
import asyncio
import sqlite3
from collections.abc import Iterator
from typing import Any


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
    with sqlite3.connect(f"{PATH_TO_DB}/{DB}") as db:
        db.execute(CREATE_TABLE_QUERY)
        db.commit()


def insert(db: sqlite3.Connection, data: list[list[str]]) -> Any:
    cursor = db.cursor()
    cursor.executemany(INSERT_QUERY, data)
    db.commit()
    cursor.close()


def sqlite_work(get_data: Iterator[list[list[str]]]) -> int:
    with sqlite3.connect(f"{PATH_TO_DB}/{DB}") as db:
        return len([insert(db, data) for data in get_data])


async def async_sqlite_work(gen_data: Iterator[list[list[str]]]) -> int:
    async with aiosqlite.connect(f"{PATH_TO_DB}/{DB}") as db:
        coros = [db.executemany(INSERT_QUERY, data) for data in gen_data]
        nums = len(await asyncio.gather(*coros))
        await db.commit()
        return nums


create_table()

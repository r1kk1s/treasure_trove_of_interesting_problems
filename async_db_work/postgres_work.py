import psycopg2
import asyncpg  # type: ignore

import asyncio
from collections.abc import Iterator
from typing import Any


DB = "postgres://user:password@localhost:5432/database"

CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS my_table (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    int_col TEXT,
    float_col TEXT,
    str_col TEXT,
    bool_col TEXT,
    int_col_2 TEXT,
    array_col TEXT,
    json_col TEXT,
    int_col_3 TEXT,
    bool_col_2 TEXT,
    bool_col_3 TEXT
)"""


INSERT_QUERY = """
INSERT INTO my_table (int_col, float_col, str_col, bool_col, int_col_2,
                      array_col, json_col, int_col_3, bool_col_2, bool_col_3)
VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""


ASYNC_INSERT_QUERY = """
INSERT INTO my_table (int_col, float_col, str_col, bool_col, int_col_2,
                      array_col, json_col, int_col_3, bool_col_2, bool_col_3)
VALUES
    ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)
"""


def create_table() -> None:
    with psycopg2.connect(DB) as conn:
        with conn.cursor() as curs:
            curs.execute(CREATE_TABLE_QUERY)
        conn.commit()


def insert(conn: psycopg2.extensions.connection, data: list[list[str]]) -> Any:
    with conn.cursor() as curs:
        curs.executemany(INSERT_QUERY, data)


def postgres_work(gen_data: Iterator[list[list[str]]]) -> int:
    with psycopg2.connect(DB) as conn:
        return len([insert(conn, data) for data in gen_data])


async def async_insert(pool: asyncpg.Pool, data: list[list[str]]) -> None:
    async with pool.acquire() as conn:
        await conn.executemany(ASYNC_INSERT_QUERY, data)


async def async_postgres_work(gen_data: Iterator[list[list[str]]]) -> int:
    async with asyncpg.create_pool(DB) as pool:
        coros = [async_insert(pool, data) for data in gen_data]
        return len(await asyncio.gather(*coros))


create_table()

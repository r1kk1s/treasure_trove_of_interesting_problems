from aiocsv import AsyncReader
import aiofiles

import asyncio
from time import perf_counter as pc
import sqlite3
from collections.abc import AsyncGenerator

from csv_work import PATH_TO_FILES, FILE_NUMBERS, create_csv_files
from db_work import INSERT_QUERY, PATH_TO_DB, DB, create_table


async def gen_async_csv_data(num: int) -> AsyncGenerator[list[str], None]:
    async with aiofiles.open(f"{PATH_TO_FILES}/csv_file_{num}.csv", "r") as file:
        async_csv_data_iterator = AsyncReader(file)
        await async_csv_data_iterator.__anext__()
        async for reader in async_csv_data_iterator:
            yield reader


async def db_write(numbers: int) -> None:
    t = pc()
    with sqlite3.connect(f"{PATH_TO_DB}/{DB}") as conn:
        for num in range(numbers):
            async for reader in gen_async_csv_data(num):
                conn.execute(INSERT_QUERY, reader)
        conn.commit()
    print(pc() - t)


def main(numbers: int) -> None:
    create_csv_files(numbers)
    create_table()
    asyncio.run(db_write(numbers))


if __name__ == "__main__":
    main(FILE_NUMBERS)

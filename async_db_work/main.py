import uvloop

from time import perf_counter as pc
from collections.abc import Iterator, Callable, Awaitable

from csv_work import FILE_NUMBERS, gen_data_from_file
from sqlite_work import sqlite_work, async_sqlite_work
from postgres_work import postgres_work, async_postgres_work


def main(
    write_data: Callable[[Iterator[list[list[str]]]], int],
    gen_data: Callable[[int], Iterator[list[list[str]]]] = gen_data_from_file,
    numbers: int = FILE_NUMBERS,
) -> None:
    t = pc()
    nums = write_data(gen_data(numbers))
    print(
        f"sequential write data with {write_data.__name__} from {nums} files", pc() - t
    )


async def async_main(
    async_write_data: Callable[[Iterator[list[list[str]]]], Awaitable[int]],
    gen_data: Callable[[int], Iterator[list[list[str]]]] = gen_data_from_file,
    numbers: int = FILE_NUMBERS,
) -> None:
    t = pc()
    nums = await async_write_data(gen_data(numbers))
    print(
        f"concurrent write data with {async_write_data.__name__} from {nums} files",
        pc() - t,
    )


if __name__ == "__main__":
    main(sqlite_work)
    uvloop.run(
        async_main(async_sqlite_work)
    )  # sinchronos is faster since sqlite work with one changer

    main(postgres_work)
    uvloop.run(async_main(async_postgres_work))

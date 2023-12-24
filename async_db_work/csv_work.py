import os
import csv
import json
import random
import string
from collections.abc import Iterator


FILE_NUMBERS = 10


PATH_TO_FILES = "files"

if not os.path.exists(PATH_TO_FILES):
    os.mkdir(PATH_TO_FILES)


ASCII_LETTERS = string.ascii_letters
LENGTH = 10


def _get_random_letters_generator(
    letters: str = ASCII_LETTERS, length: int = LENGTH
) -> Iterator[str]:
    return (random.choice(letters) for _ in range(length))


def generate_random_string() -> str:
    return "".join(_get_random_letters_generator())


def generate_random_list() -> list:
    return list(_get_random_letters_generator())


def generate_random_dict() -> dict:
    return {k: v for k, v in enumerate(_get_random_letters_generator())}


def generate_csv_file(filename: str) -> None:
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "IntCol",
                "FloatCol",
                "StrCol",
                "BoolCol",
                "IntCol2" "ArrayCol",
                "JsonCol",
                "IntCol3",
                "BoolCol2",
                "BoolCol3",
            ]
        )

        for _ in range(10000):
            writer.writerow(
                [
                    random.randint(1, 777),
                    random.random(),
                    generate_random_string(),
                    random.choice([True, False]),
                    random.randint(777, 1000),
                    json.dumps(generate_random_list()),
                    json.dumps(generate_random_dict()),
                    random.randint(1000, 1777),
                    random.choice([True, False]),
                    random.choice([True, False]),
                ]
            )


def create_csv_files(num: int = FILE_NUMBERS) -> None:
    for i in range(num):
        generate_csv_file(f"{PATH_TO_FILES}/csv_file_{i}.csv")


def gen_data_from_file(numbers) -> Iterator[list[list[str]]]:
    for num in range(numbers):
        with open(f"{PATH_TO_FILES}/csv_file_{num}.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            yield [row for row in reader]


create_csv_files()

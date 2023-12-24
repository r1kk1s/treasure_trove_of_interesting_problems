import os
from datetime import datetime

from api_interface import User
from exceptions import RenameFileError, WriteFileError, handle_exception


filename = "tasks/{}.txt"


@handle_exception(WriteFileError)
def write_user_report(user: User, message: str) -> None:
    with open(filename.format(user.username), "w") as file:
        file.write(message)


def ensure_tasks_dir_existance() -> None:
    if not os.path.exists("tasks/"):
        os.mkdir("tasks/")


@handle_exception(RenameFileError)
def rename_old_file(username: str) -> None:
    old_name = filename.format(username)
    if os.path.exists(old_name):
        new_name = f"tasks/old_{username}_{_get_file_time_creation(old_name)}.txt"
        os.rename(old_name, new_name)


def _get_file_time_creation(name: str) -> str:
    return datetime.strftime(
        datetime.fromtimestamp(os.path.getctime(name)), "%Y-%m-%dT%H:%M"
    )

import requests
import json
from typing import NamedTuple
from exceptions import RequestsAPIError, handle_exception


todos_url = "https://json.medrocket.ru/todos"
users_url = "https://json.medrocket.ru/users"


class Todo(NamedTuple):
    user_id: int
    title: str
    completed: bool


class User(NamedTuple):
    full_name: int
    username: str
    company_name: str
    email: str
    todos: list[Todo]


@handle_exception(exception=RequestsAPIError)
def create_users_list() -> list[User]:
    """Serialize api data to the desired format"""
    users_content, todos_content = _get_data_from_API(users_url, todos_url)
    users = []
    todos = _create_todos_list(todos_content)
    users_dict_list = json.loads(users_content)
    for user in users_dict_list:
        users.append(
            User(
                full_name=user["name"],
                username=user["username"],
                company_name=user["company"]["name"],
                email=user["email"],
                todos=[todo for todo in todos if user["id"] == todo.user_id],
            )
        )
    return users


def _get_data_from_API(users_url: str, todos_url: str) -> tuple[bytes, bytes]:
    """Return tuple of responses_content from API, according to the order of transmitted urls"""
    return requests.get(users_url).content, requests.get(todos_url).content


def _create_todos_list(todos_content: bytes) -> list[Todo]:
    todos = []
    todos_dict_list = json.loads(todos_content)

    for todo in todos_dict_list:
        if "userId" in todo and "title" in todo and "completed" in todo:
            todos.append(
                Todo(
                    user_id=todo["userId"],
                    title=todo["title"],
                    completed=todo["completed"],
                )
            )
    return todos


if __name__ == "__main__":
    print(create_users_list())

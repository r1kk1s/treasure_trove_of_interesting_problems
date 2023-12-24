from datetime import datetime

from api_interface import User, Todo


def create_user_report_message(user: User) -> str:
    completed_todos = [todo for todo in user.todos if todo.completed]
    not_completed_todos = [todo for todo in user.todos if not todo.completed]

    message = (
        f"# Отчёт для {user.company_name}.\n"
        f'{user.full_name} <{user.email}> {datetime.now().strftime("%d.%m.%Y %H:%M")}\n'
        f"Всего задач: {len(user.todos)}\n"
        f"\n## Актуальные задачи ({len(not_completed_todos)}):\n"
        f"{_add_todos_to_message(not_completed_todos)}"
        f"\n## Завершённые задачи ({len(completed_todos)}):\n"
        f"{_add_todos_to_message(completed_todos)}"
    )

    return message


def _add_todos_to_message(todos: list[Todo]) -> str:
    message = ""
    for todo in todos:
        message += (
            f'- {todo.title[:46] + "..." if len(todo.title) > 46 else  todo.title}\n'
        )
    return message

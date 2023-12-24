from collections.abc import Callable


def sum(*values: int) -> Callable | int:
    """Sum all given arguments until no argument is passed"""
    total = 0
    for i in values:
        total += i

    def func(*new_values: int) -> Callable | int:
        nonlocal total
        if not new_values:
            return total
        for i in new_values:
            total += i
        return func

    return func


if __name__ == "__main__":
    print(sum(1, 2, 3)(4, 5)())  # type: ignore

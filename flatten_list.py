from collections.abc import Iterable, Iterator


def get_flatten_list(iterable: Iterable[int | Iterable]) -> list[int]:
    """Flatten any iterable"""
    flatten_list = []
    for el in iterable:
        if isinstance(el, Iterable):
            flatten_list.extend(get_flatten_list(el))
        else:
            flatten_list.append(el)
    return flatten_list


def gen_flatten_list(iterable: Iterable[int | Iterable]) -> Iterator[int]:
    """Generate elements of any nesting iterable"""
    for el in iterable:
        if isinstance(el, Iterable):
            yield from gen_flatten_list(el)
        else:
            yield el


if __name__ == "__main__":
    l = [1, [[2]], [[[3, 4]]], 5, 6, [], 7]
    print(get_flatten_list(l))  # type: ignore
    print([i for i in gen_flatten_list(l)])  # type: ignore

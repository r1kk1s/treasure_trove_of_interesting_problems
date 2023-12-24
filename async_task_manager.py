import asyncio
from time import perf_counter as pc
from typing import Literal
from collections.abc import Coroutine


class TaskManager:
    def __init__(self) -> None:
        self.tasks: list[Coroutine[None, None, str]] = []
        self.results: list[str] = []

    def add_task(self, coroutine: Coroutine) -> None:
        self.tasks.append(coroutine)

    async def run_tasks_concurrently(self) -> None:
        self.results.extend(await asyncio.gather(*self.tasks))

    async def run_tasks_sequentially(self) -> None:
        self.results.extend([await coro for coro in self.tasks])

    def get_results(self) -> list[str]:
        return self.results


async def task(i: int) -> str:
    await asyncio.sleep(i)
    return f"Task {i} result"


async def main(
    launch_type: Literal["Sequential"] | Literal["Concurrent"],
) -> None:
    t_0 = pc()
    manager = TaskManager()
    for i in range(4):
        manager.add_task(task(i))

    if launch_type == "Sequential":
        await manager.run_tasks_sequentially()
    else:
        await manager.run_tasks_concurrently()

    print(
        f"{launch_type} launch of tasks took {pc() - t_0}s",
        f"Results: {manager.get_results()}",
        sep="\n",
    )


if __name__ == "__main__":
    asyncio.run(main("Sequential"))
    asyncio.run(main("Concurrent"))

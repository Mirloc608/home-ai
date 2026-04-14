import asyncio


async def schedule(task_coro):
    return await asyncio.create_task(task_coro)

from proj.async_generator import generate


async def consume():
    async for item in generate():
        print(item)

async def generate():
    lst = list(range(10))
    for item in lst:
        yield item

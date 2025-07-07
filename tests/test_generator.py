import pytest
from proj.async_consumer import consume


@pytest.mark.asyncio
async def test_consume():
    await consume()

"""
This program calls your API concurrently to measure its performance
"""
import time
import asyncio
import httpx

# async def defines a coroutine function
async def call_api(client, url):
    start = time.perf_counter()
    # await pauses the coroutine until the operation completes
    response = await client.get(url, timeout=30)
    end = time.perf_counter()
    print(f"Response: {response.status_code}, Time: {end-start:.2f}sec")


async def main():
    # Make sure your app is up and running
    url = "http://localhost:8000/sleep/sys"
    async with httpx.AsyncClient(timeout=30) as client:
        tasks = [call_api(client, url) for _ in range(10)]
        # asyncio.gather() runs multiple coroutines concurrently
        await asyncio.gather(*tasks)


# asyncio.run() starts the event loop
asyncio.run(main())

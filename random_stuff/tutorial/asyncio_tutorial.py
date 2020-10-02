"""
Asynchronous programming. Handling multiple processes concurrently.
"""

import asyncio
import time

async def find_divisibles(inrange, div_by):
    print(f"finding nums in range {inrange} divisible by {div_by}")
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 50000 == 0:
            await asyncio.sleep(0.00001)
    print(f"Done with nums in range {inrange} divisible by {div_by}")
    return located


async def main():
    divs1 = loop.create_task(find_divisibles(508000, 34113))
    divs2 = loop.create_task(find_divisibles(100052, 3210))
    divs3 = loop.create_task(find_divisibles(500, 3))
    await asyncio.wait([divs1, divs2, divs3])
    return divs1, divs2, divs3


if __name__ == '__main__':
    start_time = time.process_time()
    try:
        loop = asyncio.get_event_loop()
        d1, d2, d3 = loop.run_until_complete(main())
        print(d1.result())
    except Exception as e:
        pass
    finally:
        loop.close()
        print(time.process_time() - start_time)

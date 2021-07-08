"""
coroutine
"""
import asyncio

async def fun1():
    print("fun1 start")
    await asyncio.sleep(2)
    print("fun1 over")

async def fun2():
    print("fun2 start")
    await asyncio.sleep(3)
    print("fun2over")

if __name__ == '__main__':
    cor1=fun1()
    cor2=fun2()
    tasks=[asyncio.ensure_future(cor1),
           asyncio.ensure_future(cor2)]
    loop=asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    pass
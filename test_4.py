import asyncio

async def print_numbers():
    for i in range(1, 27):
        print(i, '->', end=' ')
        await asyncio.sleep(0.25)

async def print_alphabet():
    for i in range(26):
        print(chr(ord('a')+i))
        await asyncio.sleep(0.25)

async def main():    
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_alphabet())

    await task1
    await task2

asyncio.run(main())

# print((print(n) for n in [1, 2, 3]))
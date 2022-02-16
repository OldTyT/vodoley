from aiobalaboba import balaboba
from sqlighter import SQLighter
import asyncio
import random

balabob = ''  # В кавычки пишем запрос(то, что нужно продолжить)
r = 10  # Количество строк результата в БД


def rnd():
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    length = 10
    randomized = ''
    for i in range(length):
        randomized += random.choice(chars)
    return randomized


my_rnd = rnd()
db = SQLighter(f'{my_rnd}.db')


async def main():
    count = 0
    db.create_result()
    with open(f'{my_rnd}.txt', 'w') as f:
        while True:
            if count >= r:
                break
            response = await balaboba(balabob)
            db.add_result(response)
            f.write(f'''____________________№{count+1}____________________
{response}
____________________END____________________\n''')
            count += 1


if __name__ == "__main__":
    asyncio.run(main())

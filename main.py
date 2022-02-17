from aiobalaboba import balaboba
from sqlighter import SQLighter
import asyncio
import random

query = '''Привет'''  # В кавычки пишем запрос(то, что нужно продолжить)
requests = 100  # Количество строк результата в БД


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
    db.create_result()
    f = open(f'{my_rnd}.txt', 'w')
    r = ''
    for i in range(requests):
        response = await balaboba(query)
        db.add_result(response)
        r += f'''____________________№{i + 1}____________________\n{response}\n____________________END____________________\n'''
    f.write(r)


if __name__ == "__main__":
    asyncio.run(main())

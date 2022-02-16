import asyncio

from aiobalaboba import balaboba
from sqlighter import SQLighter
import random

balabob = ''  # В кавычки пишем запрос(то, что нужно продолжить)

r = 10  # Количество строк результата в БД


def rnd():
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    length = 10
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password


db = SQLighter(f'{rnd()}.db')


async def main():
    count = 0
    db.create_result()
    while True:
        if count >= r:
            break;
        response = await balaboba(balabob)
        db.add_result(response)
        count += 1


if __name__ == "__main__":
    asyncio.run(main())

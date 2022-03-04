import asyncio


async def ticker():
    for i in range(2):
        yield i
        await asyncio.sleep(0.1)


async def run():
    try:
        agen = aiter(ticker())
    except NameError as err:
        print(f"NameError: {err}")
    try:
        print(await anext(agen))
        print(await anext(agen))
    except NameError as err:
        print(f"NameError: {err}")


def main():
    asyncio.run(run())


if __name__ == "__main__":
    main()
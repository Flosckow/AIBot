import aiohttp
import asyncio
import pprint

from yarl import URL

class GetPrice():

    def __init__(self, name, price, date, url) -> None:
        self.name = name
        self.price = price
        self.date = date
        self.url = url



    async def get_data_for_url(url):
        timeout = aiohttp.ClientTimeout(total=120)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resposne:
                print(await resposne.text())


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1') as resposne:
            k = await resposne.json()
            pprint.pprint(k.get('prices'))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

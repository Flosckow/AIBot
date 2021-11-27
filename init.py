import aiohttp
import asyncio
import pprint
import csv
import datetime

from yarl import URL

class GetPrice():

    def __init__(self, name, url) -> None:
        self.name = name
        # self.price = price
        self.date = datetime.datetime.now()
        self.url = url



    async def get_data_for_url(self):
        timeout = aiohttp.ClientTimeout(total=120)
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as resposne:
                data = await resposne.json()
                return data.get('prices')

    def write_csv(self, data):
        with open('test.csv', mode="w", newline='') as file:
            split_data = data[0]
            writer = csv.writer(file)
            writer.writerows(zip(split_data.split(', ')))
           


async def main():
    get = GetPrice(name='Bitcoin', url='https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1')
    data_to_csv = await get.get_data_for_url()
    res = ["".join([", ".join([str(i) for i in s]) for s in data_to_csv])]
    get.write_csv(res)
    


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

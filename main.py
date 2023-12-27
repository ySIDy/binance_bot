from binance.client import AsyncClient
import asyncio

async def main():
    client = await AsyncClient.create(1, 1, testnet=True)
    #tld='ua'





if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
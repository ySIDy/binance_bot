from binance.client import AsyncClient
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import asyncio
import json
from io import StringIO

def main():
    client = Client("1", "1", testnet=True)
    #tld='ua'
    res = client.get_exchange_info()
    data = client.get_order_book(symbol='BNBBTC')

 
    with open('data.json', 'w') as f:
        f.write(json.dumps(data))
    
    
    
def get_curancy_data(symbol):
    client = Client("1", "1", testnet=True)
    #tld='ua'
    res = client.get_exchange_info()
    data = client.get_order_book(symbol=symbol)
    return data



if __name__ == "__main__":
    main()
    

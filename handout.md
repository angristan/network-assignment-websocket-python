# ENE419 - Computer Networks - Assignment 3

> Stanislas Lange - 9319520196

```py
#!/usr/bin/env python3

import asyncio
import websockets
import json


async def ws_print():
    uri = "wss://api.upbit.com/websocket/v1"
    async with websockets.connect(uri) as websocket:

        await websocket.send('[{"ticket":"UNIQUE_TICKET"},{"type":"trade","codes":["KRW-BTC"]},{"type":"orderbook","codes":["KRW-BTC"]}]')
        while True:
            raw_response = await websocket.recv()
            response_str = raw_response.decode('utf8')
            response_json = json.loads(response_str)

            if response_json['type'] == 'orderbook':
                print(response_json['orderbook_units'][0])

            elif response_json['type'] == 'trade':
                print("trade_price: {}, trade_volume: {}, ask_bid: {}".format(response_json['trade_price'], response_json['trade_volume'], response_json['ask_bid']))

asyncio.get_event_loop().run_until_complete(ws_print())
```

Ouput:

```
trade_price: 8411000.0, trade_volume: 0.1510598, ask_bid: ASK
{'ask_price': 8418000.0, 'bid_price': 8411000.0, 'ask_size': 0.05790747, 'bid_size': 1.97662502}
trade_price: 8411000.0, trade_volume: 0.01550594, ask_bid: ASK
{'ask_price': 8418000.0, 'bid_price': 8411000.0, 'ask_size': 0.05790747, 'bid_size': 1.97026686}
{'ask_price': 8418000.0, 'bid_price': 8411000.0, 'ask_size': 0.05790747, 'bid_size': 1.97026686}
{'ask_price': 8418000.0, 'bid_price': 8411000.0, 'ask_size': 0.05790747, 'bid_size': 1.97026686}
trade_price: 8411000.0, trade_volume: 0.94251801, ask_bid: ASK
{'ask_price': 8418000.0, 'bid_price': 8411000.0, 'ask_size': 0.05790747, 'bid_size': 1.02774885}
{'ask_price': 8418000.0, 'bid_price': 8411000.0, 'ask_size': 0.05790747, 'bid_size': 1.02774885}
{'ask_price': 8418000.0, 'bid_price': 8411000.0, 'ask_size': 0.05790747, 'bid_size': 1.02774885}
```

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

#!/usr/bin/env python

import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'tetris-clone.azurewebsites.net', 5000))
print("starting websocket...")
asyncio.get_event_loop().run_forever()
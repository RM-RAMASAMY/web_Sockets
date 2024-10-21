# server.py
import asyncio
import websockets
import random

async def echo(websocket, path):
    async for message in websocket:
        modified_message = f"{message} {random.randint(1, 100)}"
        await websocket.send(modified_message)

start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
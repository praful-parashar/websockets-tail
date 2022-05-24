import asyncio
import websockets
 
async def test():
    async with websockets.connect('ws://localhost:5000/', ping_interval=None) as websocket:
        await websocket.send("hello")
        while True:
        # await websocket.send("hello")
            response = await websocket.recv()
            print(response)
        # await websocket.send("hello")
        # while
        # response = await websocket.recv()
        # print(response)
        # print(response.__dict__)
 
asyncio.get_event_loop().run_until_complete(test())
asyncio.get_event_loop().run_forever()
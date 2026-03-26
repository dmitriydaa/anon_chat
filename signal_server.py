import asyncio
import websockets
import json

clients = {}

async def handler(ws):
    user_id = await ws.recv()
    clients[user_id] = ws
    print(f"{user_id} подключился")

    try:
        async for message in ws:
            data = json.loads(message)
            to = data.get("to")

            if to in clients:
                await clients[to].send(json.dumps(data))

    except:
        pass
    finally:
        if user_id in clients:
            del clients[user_id]

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("Сервер запущен на порту 8765")
        await asyncio.Future()

asyncio.run(main())

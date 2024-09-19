import asyncio
import websockets

async def main():
        try:  
            async with websockets.connect("ws://localhost:8765") as websocket:
                while True:
                    message = input("Enter a message: ")
                    await websocket.send(message)
                    response = await websocket.recv()
                    response2 = await websocket.recv()
                    print(f"Received from server: {response2}")
                    print(f"Received from server: {response}")
        except (asyncio.TimeoutError, websockets.exceptions.ConnectionClosed):
            print("Connection closed. Reconnecting.c..")
            await asyncio.sleep(5)  # 5초 후 재연결 시도
            await main()

asyncio.run(main())
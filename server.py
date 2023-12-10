import asyncio
import websockets
import subprocess

async def handle_message(websocket, message):
    # Function to process the received message
    print(f"Received message: {message}")
    subprocess.call('python hack2.py', creationflags=subprocess.CREATE_NEW_CONSOLE)
    # Perform actions with the message data here

async def server(websocket, path):
    async for message in websocket:
        await handle_message(websocket, message)

if __name__ == '__main__':
    start_server = websockets.serve(server, 'localhost', 8765)  # Change host and port if needed
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

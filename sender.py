import asyncio
import websockets
import json

async def send_message():
    async with websockets.connect('ws://localhost:8765') as websocket:  # Change host and port if needed
        message_text = input("Enter the message to send: ")
        sender_name = input("Enter your name: ")
        
        message = {
            "text": message_text,
            "sender": sender_name
        }
        await websocket.send(json.dumps(message))

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(send_message())

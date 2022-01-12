from channels.generic.websocket import AsyncJsonWebsocketConsumer

#how to connect, send data and disconnect with consumers
class EventConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("Commentary", self.channel_name)
        print(f"Added {self.channel_name} channel to Commentary")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("Commentary", self.channel_name)
        print(f"Removed {self.channel_name} channel to Commentary")

    async def cricket_commentary(self, event):
        await self.send_json(event)
        print(f"Got message {event} at {self.channel_name}")

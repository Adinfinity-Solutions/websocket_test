from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync


class TestConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name="test_consumer"
        self.room_group_name="test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(     #group ass if we want to call it form any views or model

            self.channel_name, self.room_group_name
        )
        self.accept()
        self.send(text_data=json.dump({'status':'connected'}))     #sending data to backend to frondend


    def recieve(self,text_data):
        print(text_data)
        self.send(text_data=json.dump({'status':'copnnected from frontend to backend '}))
        # when we need to send data from frontend to backend

    def disconnect(self):
        pass

    def send_notification(self,event):

        print(event)

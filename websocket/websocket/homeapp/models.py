from django.db import models
from django.contrib.auth.models import User
from channels.layers import  get_channel_layer
from asgiref.sync import async_to_sync
import json




class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification=models.TextField(max_length=100)
    is_seen=models.BooleanField(default=False)



# to save and once the object is created we send data to frontend
    def save(self,*args,**kwargs):
        channel_layer= get_channel_layer()
        # notification_objs = Notification.objects.all(is_seen=False).count()
        notification_objs = Notification.objects.filter(is_seen=False).count()

        data={'count':notification_objs,'current_notificaton':self.notification}
        # fronend to
        # print('save called')

        async_to_sync(channel_layer.group_send)(
            'test_consumer_group',{
                'type':'send_notification',
                'value':json.dumps(data)
            }
        )
        super(Notification,self).save(*args,**kwargs)

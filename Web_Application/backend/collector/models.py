from email.policy import default
from django.db import models
from tourist.models import User
from map.models import Place
from django.utils import timezone

class Log(models.Model):
    created = models.DateTimeField('date happened', default=timezone.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="logs")
    content_id = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="log")
    event = models.CharField(max_length=200)

    def __str__(self):
        return "user_id: {}, content_id: {}, event: {}".format(str(self.user_id),
                                                               str(self.content_id),
                                                               self.event)
import uuid

from django.db import models


class Reducer(models.Model):
    objects = None
    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField(max_length=3000)
    date_time = models.DateTimeField(auto_now_add=True)

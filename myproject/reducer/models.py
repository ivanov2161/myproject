from django.db import models


class Url(models.Model):
    key = models.CharField(primary_key=True, max_length=10)
    url = models.URLField(max_length=3000)
    date_time = models.DateTimeField(auto_now_add=True)

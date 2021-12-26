from django.db import models

# Create your models here.
class Url(models.Model):
    num = models.AutoField(primary_key=True)
    url = models.URLField(null=False)
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
from django.db import models
from django.utils import timezone
# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=10)
    introduce = models.TextField()
    age = models.CharField(max_length=5)
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
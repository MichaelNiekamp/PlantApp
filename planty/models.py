from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

from accounts.models import CustomUser

User = get_user_model()

# Create your models here.
class Plant(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    description = models.TextField()
    date_planted = models.DateTimeField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plant_detail", kwargs={"pk": self.pk})


class Event(models.Model):
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="plants")
    event_title = models.CharField(max_length=200)
    height = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(blank=True, null=True, upload_to="media")

    processed_picture = ImageSpecField(
        source="picture",
        processors=[ResizeToFill(400, 200)],
        format="JPEG",
        options={"quality": 60},
    )

    description = models.TextField()

    def __str__(self):
        return str(self.plant_id)

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})

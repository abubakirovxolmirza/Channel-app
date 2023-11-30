from django.db import models
from django.utils import timezone

# Create your models here.


class post(models.Model):
    post_image = models.ImageField(upload_to="photos", blank=True, null=True)
    post_header = models.CharField(max_length=60)
    post_content = models.CharField(max_length=200)
    post_date = models.DateTimeField(default=timezone.datetime.now)

    def __str__(self):
        return f"Post: {self.post_header}"

from django.db import models
from django.contrib.auth.models import User  # If you want to link reviews to users

class Reviews(models.Model):
    text = models.TextField()
    punctuation = models.PositiveSmallIntegerField(default=0, help_text="Rating from 1 to 5")  # You can customize the rating scale
    date = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the review is created


    def __str__(self):
        return f'Review text {self.text }'



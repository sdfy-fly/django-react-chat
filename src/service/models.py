from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    image_link = models.CharField(max_length=255, default="https://api-private.atlassian.com/users/3ed7bde5a8c78e8d0d38eca297f62495/avatar")

    def __str__(self):
        return self.full_name


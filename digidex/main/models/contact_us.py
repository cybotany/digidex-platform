from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.name}"

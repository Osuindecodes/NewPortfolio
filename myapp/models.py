from django.db import models

# Create your models here.

class getdata(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
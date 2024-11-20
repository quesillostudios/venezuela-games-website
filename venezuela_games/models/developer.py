from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    found_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
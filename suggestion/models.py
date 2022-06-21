from django.db import models

# Create your models here.
class suggestion(models.Model):
    title=models.CharField(max_length=100,default=None)
    author=models.CharField(max_length=100, default=None)
    published=models.DateField(blank=True, null=True, default=None)

    def __str__(self) -> str:
        return self.title
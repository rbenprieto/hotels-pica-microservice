from django.db import models


class Hotels(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    image = models.URLField(max_length=500)
    short_description = models.TextField()
    large_description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"
        unique_together = ('name', 'city', 'address')

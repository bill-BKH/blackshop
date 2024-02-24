from django.db import models
 
class Product(models.Model):
    titel = models.CharField(max_length = 300)
    # category = models.ManyToManyField(category)
    is_actie = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    short_description = models.CharField(max_length = 260)
    description = models.TextField()

from django.db import models
 

class ProductCategory(models.Model):
    title = models.CharField(max_length=64)
    def __str__(self):
        return self.title 

class Product(models.Model):
    title = models.CharField(max_length = 300)
    is_actie = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    short_description = models.CharField(max_length = 260)
    description = models.TextField()
    category = models.ManyToManyField(ProductCategory)
    price = models.IntegerField()
    slug = models.SlugField()
    picture = models.ImageField(upload_to="product" ,null= True, blank=True)
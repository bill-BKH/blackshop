from django.db import models


class category(models.Model):
 kinds = models.CharField(max_length=20)
 
class is_actie(models.Model):
    pass

class is_delete(models.Model):
    pass
 
 
class product(models.Model):
    titel = models.CharField(max_length = 300)
    category = models.ManyToManyField(category)
    is_actie = models.ForeignKey(is_actie,on_delete=models.SET_NULL,null = True)
    is_delete = models.ForeignKey(is_delete,on_delete = models.CASCADE)
    short_description = models.CharField(max_length = 260)
    description = models.TextField()

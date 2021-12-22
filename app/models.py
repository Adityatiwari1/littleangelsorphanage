from django.db import models

class Students(models.Model):
    name= models.CharField(max_length=50)
    phone= models.CharField(max_length=50)
    subject= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    message= models.TextField()

    def __str__(self):
        return self.name
 
class feedback(models.Model):
    name= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    message= models.TextField()

    def __str__(self):
        return self.name


class stories(models.Model):
    mes= models.CharField(max_length=200)

    def __str__(self):
        return self.mes
from django.db import models
from django.contrib.auth.forms import User

class Extended_User(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    bdate = models.DateField()
    address = models.TextField(max_length= 100, null= True)

class Selected_cities(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    cities = models.CharField(max_length = 20, null= True)
    hometown = models.BooleanField(default= True)

    def __str__(self):
        return self.cities, self.hometown
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    groups = None
    user_permissions = None


    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        #db_table = '"name_left_in_lowercase"'


class TestModel(models.Model):
    name = models.CharField(max_length=120, blank=True,default='hello',null=True)


class Car(TestModel):
    price = models.IntegerField(_('Price of Car'),default=10)
    tag = models.CharField(max_length=100,blank=True,null=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)


class Example(models.Model):
    users = models.ManyToManyField(User, through='TestThroughModel')


class TestThroughModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    example = models.ForeignKey(Example,on_delete=models.CASCADE)
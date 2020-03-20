from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    enrollment_no= models.IntegerField(null=True)
    name= models.CharField(max_length=200,null=True)
    room_no= models.CharField(max_length=10,null=True)
    phone= models.IntegerField(null=True)
    email= models.CharField(max_length=200,null=True)
    date_created= models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.room_no


class Company(models.Model):
    # CATEGORY=(
    #     ('Amazon','Amazon'),
    #     ('Flipkart','Flipkart'),
    #     ('Ebay','Ebay'),
    #     ('Post','Post'),
    #     ('Other','Other'),
    # )

    name= models.CharField(max_length=200,null=True)
    # category= models.CharField(max_length=200,null=True,choices=CATEGORY)
    description= models.CharField(max_length=200,null=True,blank=True)
    date_created= models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Order(models.Model):

    STATUS=(
        ('Pending','Pending'),
        ('Delivered','Delivered'),
    )

    student = models.ForeignKey(Student,null=True,on_delete= models.SET_NULL)
    company = models.ForeignKey(Company,null=True,on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)




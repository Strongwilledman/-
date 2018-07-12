from django.db import models

# Create your models here.

class Classes(models.Model):
    id = models.IntegerField(primary_key=True)
    caption = models.CharField(max_length=32,null=False)


class Student(models.Model):
    name = models.CharField(primary_key=True, max_length=32)
    email = models.CharField(max_length=32,null=True)
    cls = models.ForeignKey(Classes, models.CASCADE, db_column='cls', blank=False, null=False)


class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    cls = models.ManyToManyField(Classes)


class Administrator(models.Model):
    username = models.CharField(primary_key=True, max_length=45)
    password = models.CharField(max_length=45)



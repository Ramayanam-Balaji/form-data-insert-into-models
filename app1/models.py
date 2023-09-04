from django.db import models

# Create your models here.
class School(models.Model):
    scname=models.CharField(max_length=100,primary_key=True)
    scprincipal=models.CharField(max_length=100)
    sclocation=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.scname
    
class Student(models.Model):
    scname=models.ForeignKey(School,on_delete=models.CASCADE)
    sname=models.CharField(max_length=100)
    sid=models.IntegerField(primary_key=True)
    def __str__(self) -> str:
        return self.sname
# from django.db import models

# # Create your models here.
# class Student(models.Model):
#     name=models.TextField()
#     course=models.CharField(max_length = 200)
#     year=models.IntegerField()


from django.db import models

#Create your model here.

class student(models.Model):
   Title =models.TextField()
   location=models.CharField(max_length=150)
   Trainer=models.TextField()
   Edit=models.TextField()
   Delete=models.TextField()

       
from django.db import models

# Create your models here.
class Customerlist(models.Model):
    Postid=models.AutoField(primary_key=True)
    # default user for to alter the rows while makemigrations
    name=models.CharField(max_length=40,default="")
    address=models.CharField(max_length=40,default="")
    title=models.CharField(max_length=40,default="")
    date=models.DateTimeField(blank=True)
    # UPLOAD TO ===  media/Carcutomizations/images
    images=models.ImageField(upload_to="Carcustomization/image",default="")


    def __str__(self):
        
        return self.name + ' is '  + self.title

# class login(models.Model):
#     name=models.CharField(max_length=40,default="")
#     password=models.CharField(max_length=100,default="")
#     email=models.CharField(max_length=40,default="")
#     def __str__(self):
#         return self.name

from django.db import models

class Customerlist(models.Model):
    Postid=models.AutoField(primary_key=True)
    # default user for to alter the rows while makemigrations
    name=models.CharField(max_length=40,default="")
    address=models.CharField(max_length=40,default="")
    title=models.CharField(max_length=40,default="")
    date=models.DateTimeField(blank=True)
    

    def __str__(self):
        
        return self.name + ' is '  + self.title

from django.db import models


class DesireInfo(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='info/pdfs/')
    cover = models.ImageField(upload_to='info/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

    def upload_title_blank(self):
        return(self.title != False)

    def title_char(self):
        punctuation=''
        return(self.title != punctuation)

    def image_blank(self):
        return(self.pdf != False)
    
    
   
from django.db import models

# Create your models here.
class Image(models.Model):
    img = models.ImageField(upload_to="images")
    alt_txt = models.CharField(max_length=100)
    
    def __str__(self):
        return self.alt_txt
    
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.OneToOneField(Image, on_delete=models.CASCADE, blank=True, )
    
    def __str__(self):
        return self.title

from django.db import models

class Avatar_pic(models.Model):
    image = models.ImageField(upload_to='avatars/')
    cartoon_img = models.ImageField(upload_to='cartoons/', null=True, blank=True)
    
    def __str__(self):
        return f"Avatar {self.id}"

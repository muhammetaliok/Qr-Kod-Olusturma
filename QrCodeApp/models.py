from django.db import models
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File

# Create your models here.
import random
class QrCode(models.Model):
   url=models.URLField()
   name = models.CharField(max_length=150,null=True,blank=True)
   get_email = models.CharField(max_length=250,null=True,blank=True)
   phone = models.CharField(max_length=150,null=True,blank=True)
   image=models.ImageField(upload_to='qrcode',blank=True)


   def save(self,*args,**kwargs):
      qrcode_img=qrcode.make(self.url)
      canvas=Image.new("RGB", (300,300),"white")
      draw=ImageDraw.Draw(canvas)
      canvas.paste(qrcode_img)
      buffer=BytesIO()
      canvas.save(buffer,"PNG")
      self.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
      canvas.close()
      super().save(*args,**kwargs)



from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify # new
from django.urls import reverse


# Create your models here.
class Food(models.Model):  
  foodName = models.CharField(max_length=60,verbose_name="Prato")
  price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Preço")
  pictureFood = models.ImageField( upload_to='foods/',
                                        default='default/default1.png',verbose_name="Imagem")
  description = models.TextField(max_length=120,verbose_name="Descrição")
  employer = models.CharField(max_length=10,verbose_name="Chefe", blank=True)
  is_published = models.BooleanField(default=True,verbose_name="Publicado")
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  slug = models.SlugField(max_length=200)

  def __str__(self):
    return self.foodName
  
  def get_absolute_url(self):
        return reverse('food', kwargs={'slug_text': self.slug})

  def save(self, *args, **kwargs):
        if not self.slug:
          self.slug = slugify(self.foodName)
        return super(Food, self).save(*args, **kwargs)
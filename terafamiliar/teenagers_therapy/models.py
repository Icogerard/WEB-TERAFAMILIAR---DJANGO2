from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField

# Create your models here.
class Teenagers_therapy(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imágen", upload_to="teenagers_therapy")
    created = models.DateTimeField(auto_now=True, verbose_name="Fecha de creación")
    updated =  models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    

    class Meta:
        verbose_name = "terapia para adolecentes"
        verbose_name_plural = "terapias para adolecentes"
        ordering = ['-created']

    def __str__(self):
        return self.title
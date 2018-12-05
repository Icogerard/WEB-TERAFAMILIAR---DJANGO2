from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField

# Create your models here.
class Lgtb(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)

    class Meta:
        verbose_name = "lgtb"
        verbose_name_plural = "lgtb+"
        ordering = ['-created']

    def __str__(self):
        return self.title
from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField

# Create your models here.
class Individual_therapy(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imágen", upload_to="individual_therapy")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)

    class Meta:
        verbose_name = "terapia individual"
        verbose_name_plural = "terapias individuales"
        ordering = ['-created']

    def __str__(self):
        return self.title
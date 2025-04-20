from django.db import models

# Create your models here.
# Modelo de proyectos / blog
class Project(models.Model):
    title = models.CharField(verbose_name="Título", max_length=50)
    description = models.TextField(verbose_name="Descripción", max_length=300)
    image = models.ImageField(verbose_name="Imagen", upload_to='projects/%Y/%m')
    link = models.URLField(verbose_name="Enlace", null=True, blank=True)
    created = models.DateTimeField(verbose_name="Fecha de Creación", auto_now_add=True)
    update = models.DateTimeField(verbose_name="última actualización", auto_now=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ["-created"]

    def __str__(self):
        return self.title

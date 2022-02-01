from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models
from numpy import delete

# Create your models here.
class Libro(models.Model):
    id= models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen",  null=True)
    descripcion = models.TextField(verbose_name="Deescrión", null=True)

    def __str__(self) -> str:
        fila = "titulo:" + self.titulo + "-" + self.descripcion
        
        return fila
    
    def delete(self, using= None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
        
    
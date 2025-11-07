from django.db import models

# Create your models here.
class Saludo(models.Model):
    # Un campo de texto para guardar el mensaje
    mensaje = models.CharField(max_length=100)

    def __str__(self):
        # Para que se vea bien en el panel de admin
        return self.mensaje

class Articulo(models.Model):
    # Cada atributo es una columna en la tabla.
    
    # VARCHAR(200)
    titulo = models.CharField(max_length=200)
    
    # TEXT
    contenido = models.TextField()
    
    # DATETIME (se guarda automáticamente al crear)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
    # BOOLEAN (con valor por defecto)
    esta_publicado = models.BooleanField(default=True)

    def __str__(self):
        # Función mágica de Python para que se vea legible
        # en el panel de admin y en la shell.
        return self.titulo
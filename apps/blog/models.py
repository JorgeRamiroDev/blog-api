from django.db import models

# Create your models here.
class blog(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    autor = models.CharField(max_length=150,null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.autor:
            self.autor = "Anônimo"
        super().save(*args, **kwargs)   

    def __str__(self):
        return self.titulo
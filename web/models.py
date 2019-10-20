from django.db import models

# Create your models here.


class Tours(models.Model):
    titulo = models.CharField('Titulo', max_length=120)
    description = models.CharField('Description', max_length=120)
    precio = models.DecimalField('Precio', max_digits=8, decimal_places=2)
    ciudad = models.CharField('Ciudad', max_length=120)
    views = models.IntegerField()
    reviews = models.IntegerField()
    calification = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = "Tours"

    def __str__(self):
        return self.titulo

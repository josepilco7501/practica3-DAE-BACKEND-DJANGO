from django.db import models

class postulantes(models.Model):

    FRONTEND= 'frontend'
    BACKEND = 'backend'
    SENIOR = 'senior'
    SEMISENIOR = 'semisenior'
    JUNIOR = 'junior'


    PERFIL_CHOICES = (
        (FRONTEND, 'Frontend'),
        (BACKEND, 'Backend'),

    )

    NIVEL_CHOICES = (
        (JUNIOR, 'Junior'),
        (SEMISENIOR, 'Semisenior'),
        (SENIOR, 'Senior'),
    )

    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)
    perfil= models.CharField(max_length=100, choices=PERFIL_CHOICES)
    nivel= models.CharField(max_length=10, choices=NIVEL_CHOICES)
    fecha_nacimiento = models.DateField()
    
from django.db import models
from django.utils import timezone

class Registro(models.Model):
    idAlumno = models.ForeignKey(Alumno, null=True, blank=True, on_delete=models.CASCADE)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Registro'

class Alumno(models.Model):
    rfidAlumno = models.CharField(max_length=254, null=False)
    nameAlumno = models.CharField(max_length=254, null=False)
    apellidoMaterno = models.CharField(max_length=254, null=False)
    apellidoPaterno = models.CharField(max_length=254, null=False)
    matriculaAlumno = models.IntegerField(null=False)
    carreraAlumno = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Alumno'
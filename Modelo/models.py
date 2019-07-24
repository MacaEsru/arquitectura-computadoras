from django.db import models
from django.utils import timezone

class Registro(models.Model):
    id_alumno = models.ForeignKey(Alumno, null=True, blank=True, on_delete=models.CASCADE)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Registro'

class Alumno(models.Model):
    rfid_alumno = models.CharField(max_length=254, null=False)
    name_alumno = models.CharField(max_length=254, null=False)
    apellidoMaterno = models.CharField(max_length=254, null=False)
    apellidoPaterno = models.CharField(max_length=254, null=False)
    matricula_alumno = models.IntegerField(null=False)
    carrera_alumno = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Alumno'
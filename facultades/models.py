from django.db import models


# Create your models here.
class Academia(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    web = models.CharField(max_length=100)

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    academia_id = models.ForeignKey(Academia,on_delete=models.CASCADE)


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    academia_id = models.ForeignKey(Academia,on_delete=models.CASCADE)


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    profesor_id = models.ForeignKey(Profesor,on_delete= models.CASCADE)


class Nota(models.Model):
    nota = models.FloatField()
    curso_id = models.ForeignKey(Curso,on_delete=models.CASCADE)
    alumno_id = models.ForeignKey(Alumno,on_delete=models.CASCADE)


class Alumno_x_Curso(models.Model):
    alumno_id = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    curso_id = models.ForeignKey(Curso,on_delete=models.CASCADE)

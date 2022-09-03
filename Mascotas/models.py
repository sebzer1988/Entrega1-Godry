from django.db import models

class Perro(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre + " , " + self.raza + " , " + str(self.edad) + " meses."

class Gato(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre + " , " + self.raza + " , " + str(self.edad) + " meses."


class Animal(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    animal_tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + " , " + self.animal_tipo + " ."
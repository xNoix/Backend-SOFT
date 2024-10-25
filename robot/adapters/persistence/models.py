# adapters/persistence/models.py
from django.db import models
#from django.contrib.auth.models import User

class SecuenciaMovimiento(models.Model):
    TIPO_CHOICES = [
        ('joints', 'Joints'),
        ('pose', 'Pose'),
    ]

    #usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Suponiendo que User es el modelo de usuario de Django
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    movimientos = models.JSONField()  # Almacena los movimientos en formato JSON
    #privado = models.BooleanField(default=False)
    fechacreado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    

class RobotDatos(models.Model):
    nombre = models.CharField(max_length=100, unique=True) #Nombre del robot
    ip = models.GenericIPAddressField(protocol='IPv4', unique=True) # Ip del robot
    minH = models.DecimalField(max_digits=5, decimal_places=4) #Altura minima del robot en pose
    minmaxJoints = models.JSONField() # valores minimos y maximos para los ejes

    def __str__(self):
        return self.nombre
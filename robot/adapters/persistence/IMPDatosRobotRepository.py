from robot.adapters.persistence.models import RobotDatos
from django.db import transaction

class RobotDatosRepository:
    def get_robot_datos(self): #listo
        try:
            datos = RobotDatos.objects.first() #Dado que es un solo robot, no deberían haber más registros, por lo que el primero es el único
            datosj = {"nombre": datos.nombre,
                      "ip": datos.ip,
                      "minH": datos.minH,
                      "minmaxJoints": datos.minmaxJoints}
            return datosj
        except RobotDatos.DoesNotExist:
            return None

    @transaction.atomic #esta funcion tambien funciona tomando en cuenta solamente el primer elemento
    def update_robot_datos(self, nombre, ip, minH, maxJoints): #listo
        robot_datos = self.get_robot_datos()
        if robot_datos:
            robot_datos.nombre = nombre
            robot_datos.ip = ip
            robot_datos.minH = minH
            robot_datos.maxJoints = maxJoints
            robot_datos.save()
            return robot_datos
        else:
            return RobotDatos.objects.create(nombre=nombre, ip=ip, minH=minH, maxJoints=maxJoints)
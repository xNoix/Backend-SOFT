from pyniryo import *  # Importa la librería que usas para manejar el robot.
from application.interfaces import RobotConnection

class RobotConnectIP(RobotConnection):
    
    def __init__(self):
        self.robot = None
        pass

    def conectar(self, datos: dict):
        """conectar al robot mediante ip"""

        self.robot = NiryoRobot(datos) #datos = ["10.10.10.10"]
        if self.robot:
            return self.robot
        else:
            raise Exception("Error al conectar a robot.")
        

    def desconectar(self):
        """desconectar el robot"""

        self.robot.end()


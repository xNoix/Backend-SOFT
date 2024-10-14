from pyniryo import *  # Importa la librería que usas para manejar el robot.
from robot.test.NiryoTest import NiryoRobotTest
from robot.domain.ports.output.IrobotConection import RobotConnection
from dotenv import load_dotenv
import os

class RobotConnectionIP(RobotConnection):
    
    def __init__(self):
        self.robot = None

    def conectar(self):
        """conectar al robot mediante ip"""

        load_dotenv()
        self.robot = NiryoRobotTest(os.getenv("IP_ROBOT")) #datos = '10.10.10.10' por ejemplo
        if self.robot:
            return self.robot
        else:
            raise Exception("Error al conectar a robot.")
        

    def desconectar(self):
        """desconectar el robot"""

        self.robot.close_connection()
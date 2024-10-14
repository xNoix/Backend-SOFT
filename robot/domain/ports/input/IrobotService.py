from abc import ABC, abstractmethod
from robot.domain.ports.output.IrobotConection import RobotConnection

class RobotService(ABC): #Interfaz para la conexión del robot

    @abstractmethod
    def __init__(self, Rconnection: RobotConnection):
        pass
    
    @abstractmethod
    def conectar(self):
        """Establece conexión con el robot."""
        pass

    @abstractmethod
    def desconectar(self):
        """Cierra la conexion del robot"""
        pass
    
    @abstractmethod
    def move_pose(self, posiciones: dict):
        """Mueve el robot por pose"""
        pass
    
    @abstractmethod
    def move_joints(self, posiciones: dict):
        """Mueve el robot por joints"""
        pass

    @abstractmethod
    def obtener_pos(self):
        """Obtiene las posiciones actuales del robot"""
        pass
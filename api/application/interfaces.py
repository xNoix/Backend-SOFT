from abc import ABC, abstractmethod

class RobotHandler(ABC): #Interfaz para el manejo del robot

    @abstractmethod
    def __init__(self, robot_pointer):
        """Recibe el puntero del robot con el cual se mandaran los comandos, puntero dado por la conexion"""
        pass
    
    @abstractmethod
    def moveJoints(self, posicion: dict):
        """Envía un comando para mover el robot a una posición específica."""
        pass

    @abstractmethod
    def movePose(self, posicion: dict):
        """Envía un comando para mover el robot a una posición específica."""
        pass
    
    @abstractmethod
    def detener(self):
        """Detiene cualquier movimiento del robot."""
        pass

    @abstractmethod
    def obtenerPos(self):
        """obtiene la posicion en radianes y xyz"""
        pass


class RobotConnection(ABC): #Interfaz para la conexión del robot
    
    @abstractmethod
    def conectar(self, datos: dict):
        """Establece conexión con el robot."""
        pass
    
    @abstractmethod
    def desconectar(self, posicion: tuple):
        """Cierra la conexion con el robot."""
        pass
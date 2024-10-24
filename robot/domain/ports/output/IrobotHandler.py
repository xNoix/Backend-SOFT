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
    def obtenerPos(self):
        """obtiene la posicion en radianes y xyz"""
        pass

    @abstractmethod
    def getJoints(self) -> list[float]:
        pass

    @abstractmethod
    def getPose(self) -> list[float]:
        pass





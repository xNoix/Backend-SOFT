from abc import ABC, abstractmethod

class RobotConnection(ABC): #Interfaz para la conexión del robot
    
    @abstractmethod
    def conectar(self, datos: dict):
        """Establece conexión con el robot."""
        pass
    
    @abstractmethod
    def desconectar(self, posicion: tuple):
        """Cierra la conexion con el robot."""
        pass
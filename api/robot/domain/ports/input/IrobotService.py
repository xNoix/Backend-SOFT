from abc import ABC, abstractmethod

class RobotService(ABC): #Interfaz para la conexión del robot
    
    @abstractmethod
    def hacerWeas(self, datos: dict):
        """Establece conexión con el robot."""
        pass
    
    @abstractmethod
    def hacerOtrasWeas(self, posicion: tuple):
        """Cierra la conexion con el robot."""
        pass
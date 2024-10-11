from pyniryo import *  # Importa la librería que usas para manejar el robot.
from api.robot.domain.ports.output.IrobotHandler import RobotHandler

class IMPRobotHandler(RobotHandler):
    
    def __init__(self, robot_pointer):
        self.robot = robot_pointer
    
    def moveJoints(self, posicion: dict):
        #Mover por grados/radianes
        """Envía la posición al robot utilizando la librería."""
        if self.robot:
            self.robot.arm.move_joints(posicion) #posicion = [0.2, -0.3, 0.1, 0.0, 0.5, -0.8] ejemplo
            print(f"Moviendo a {posicion}")
        else:
            raise Exception("No conectado al robot.")
        
    def movePose(self, posicion: dict):
        #mover por posicion xyz
        """Envía la posición al robot utilizando la librería."""
        if self.robot:
            self.robot.arm.move_pose(posicion) #posicion = [0.2, 0.0, 0.2, 0.0, 0.0, 0.0] ejemplo
            print(f"Moviendo a {posicion}")
        else:
            raise Exception("No conectado al robot.")
    
    def detener(self):
        """Detiene el movimiento del robot."""
        if self.robot:
            self.robot.detener()
            print("Movimiento detenido.")
        else:
            raise Exception("No conectado al robot.")
        
    def obtenerPos(self):
        """Devuelve un diccionario de la posicion [rad,xyz]"""
        joints_read = self.robot.arm.get_joints()
        pose_read = self.robot.arm.get_pose()

        return [joints_read, pose_read]
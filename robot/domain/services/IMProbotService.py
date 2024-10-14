from robot.domain.ports.output.IrobotHandler import RobotHandler
from robot.domain.ports.output.IrobotConection import RobotConnection
from robot.domain.ports.input.IrobotService import RobotService
from robot.domain.services.IMProbotHandler import IMPRobotHandler  # El servicio del robot

# core/robot_service.py
class RobotService_imp(RobotService):
    def __init__(self, Rconnection: RobotConnection):
        self.handler:RobotHandler #es la implementacion del robot
        self.robot = None
        self.Rconnection = Rconnection
        self.conectar()

    def conectar(self):
        self.robot = self.Rconnection.conectar() #realiza la conexion
        self.handler = IMPRobotHandler(self.robot) #da el puntero del robot al handler

    def desconectar(self):
        self.Rconnection.desconectar()
        

    def move_joints(self, posiciones: dict):
        
        #codigo para comprobaciones antes de mandar el comando

        #-----
        #mandar comando al 

        #si falla:
        #return [] vacio
        
        self.handler.moveJoints(posiciones)
        current_pos = self.handler.obtenerPos()
        print(f"Robot movido a {current_pos}")
        return current_pos


    def move_pose(self, posiciones: dict):
        
        #codigo para comprobaciones antes de mandar el comando

        #-----
        #mandar comando al 
        
        self.handler.movePose(posiciones)
        current_pos = self.handler.obtenerPos()
        print(f"Robot movido a {current_pos}")
        return current_pos

    def obtener_pos(self):
        current_pos = self.handler.obtenerPos()
        return current_pos
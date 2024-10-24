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
        

    def move_joints(self, posiciones: dict): #devuelve ambas posiciones
        
        #codigo para comprobaciones antes de mandar el comando

        #-----
        #mandar comando al 

        #si falla:
        #return [] vacio
        fallo = False
        if fallo:
            return []
        else:
        
            self.handler.moveJoints(posiciones)
            current_pos = self.obtener_pos_both() # [current_joints, current_pose]
            print(f"[joint] Robot movido a {current_pos}")
            return current_pos


    def move_pose(self, posiciones: dict): #devuelve ambas posiciones
        
        #codigo para comprobaciones antes de mandar el comando

        #-----
        #mandar comando al 
        
        self.handler.movePose(posiciones)
        current_pos = self.obtener_pos_both() # [current_joints, current_pose]
        print(f"[pose] Robot movido a {current_pos}")
        return current_pos

    def obtener_pos_both(self):
        current_joints = self.handler.getJoints()
        current_pose = self.handler.getPose()
        return [current_joints, current_pose]
    

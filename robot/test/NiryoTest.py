

class NiryoRobotTest():
    def __new__(self, ip_to_connect: dict):
        #realiza conexion
        return RobotPuntero()


class RobotPuntero():
    def __init__(self):
        pass

    def move_joints(self, posiciones: dict):
        pass

    def move_pose(self, posiciones: dict):
        pass

    def get_joints(self):
        return ['j1', 'j2', 'j3', 'j4', 'j5', 'j6']

    def get_pose(self):
        return ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']
    
    def close_connection(self):
        pass
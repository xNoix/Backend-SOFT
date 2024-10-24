

class NiryoRobotTest():
    def __new__(self, ip_to_connect: dict):
        #realiza conexion
        return RobotPuntero()


class poseObject():
    def __init__(self, pose):
        self.pose = pose

    def to_list(self) -> list[float]:
        return self.pose


class RobotPuntero():
    def __init__(self):
        pass

    def move_joints(self, posiciones: dict) -> None:
        print("NiryoTest: move_joints")

    def move_pose(self, posiciones: dict) -> None:
        print("NiryoTest: move_pose")

    def move_to_home_pose(self) -> None:
        pass

    def get_joints(self) -> list[float]:
        return ['joint1', 'j2', 'j3', 'j4', 'j5', 'j6']

    def get_pose(self) -> poseObject: # poseObject.to_list() devuelve la lista
        pose = ['joint1', 'j2', 'j3', 'j4', 'j5', 'j6']
        poseO = poseObject(pose)
        return poseO
    
    def update_tool(self):
        pass

    def release_with_tool(self):
        pass

    def grasp_with_tool(self):
        pass
    
    def close_connection(self) -> None:
        pass

    def calibrate_auto(self) -> None:
        pass
    
    def need_calibration(self) -> bool:
        #return True
        return False

    def close_connection(self):
        pass

    def wait(self, duracion: float) -> None:
        print(f"Esperar {duracion} segundos. [float]")


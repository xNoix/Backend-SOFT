from robot.adapters.persistence.IMPDatosRobotRepository import RobotDatosRepository


class RobotDatosService:
    def __init__(self):
        self.repository = RobotDatosRepository()

    def obtener_robot_datos(self): #listo
        datosj =  self.repository.get_robot_datos()
        return datosj

    def actualizar_robot_datos(self, nombre, ip, minH, maxJoints):
        try:
            if not isinstance(maxJoints, dict):
                raise ValueError("maxJoints debe ser un diccionario válido.")
            
            return self.repository.update_robot_datos(nombre, ip, minH, maxJoints)
        except Exception as e:
            return str(e)
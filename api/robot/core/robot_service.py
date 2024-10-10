from application.interfaces import RobotHandler, RobotConnection

# core/robot_service.py
class RobotService:
    def __init__(self, handler: RobotHandler):
        self.handler = handler #es la implementacion del robot
        self.tope = 30 #ejemplo

    def hacerWeas(self, direccion):
        """hacer varias weas"""
        if direccion < self.tope:
            self.handler.moveJoints(direccion)
            print(f"Robot movido a {self.handler.obtenerPos()}")
        else:
            print(f"No movido, posicion actual {self.handler.obtenerPos()}")

    def hacerOtrasWeas(self):
        """Hace muchas weas mas"""
        pass
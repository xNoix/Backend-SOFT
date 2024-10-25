from robot.adapters.persistence.IMPSecuenciaMovimientosRepository import SecuenciaMovimientoRepository
from robot.domain.services.IMProbotDatos import RobotDatosService

class SecuenciaMovimientoService:
    def __init__(self):
        self.robotDatosServ = RobotDatosService()
        self.repository = SecuenciaMovimientoRepository()

        self.tipo = ("joints", "pose")
        self.tipos = {"wait": self.waitComp,
                      "move": self.moveComp,
                      "tool": self.toolComp
                      }
        self.toolOps = ["agarrar", "soltar"]
        
    def waitComp(self, valor, tipo = None): #listo
        """Comprueba que el valor devuelto es un entero, esto indica segundos"""
        if not isinstance(valor, int):
            raise ValueError("[item: wait] El valor entregado en 'wait' no es de tipo entero.")

    
    def moveComp(self, valor, tipo): #listo
        """Comprueba la altura minima para los movimientos"""

        altura_minima = self.robotDatosServ.obtener_robot_datos()["minH"] #obtiene la altura minima de los datos del propio robot en BD

        if tipo == "joints": #aquí hay que hacer la misma comprobación, pero hay que transformar los joints a pose para validar
            pass
        elif tipo == "pose": #la altura es el eje z
            if int(valor["p3"]) < altura_minima:
                raise ValueError(f"[item: move] La nueva posición no puede ser menor a la altura mínima ({altura_minima}).")

    def toolComp(self, valor, tipo): #listo
        """Comprueba que la instruccion de la herramienta sea valida"""
        if valor not in self.toolOps:
            raise ValueError("[item: tool] Instrucción de herramienta no valida, debe ser 'agarrar' o 'soltar'.")

    #reservado para cuando haya usuarios
    """def create_secuencia(self, usuario, titulo, tipo, movimientos, privado):
        # Aquí podrías agregar lógica de validación o transformación si es necesario
        return self.repository.create(usuario, titulo, tipo, movimientos, privado)"""
    
    def create_secuencia(self, titulo, tipo, movimientos): #listo

        if tipo not in self.tipo: #comprueba que el tipo especificado de movimientos sea joints o pose
            return ("Solo se admiten movimientos del tipo 'joints' o 'pose'.")

        tiposKeys = list(self.tipos.keys()) #los tipos de elementos aceptados

        for item in movimientos: #por cada elemento en la secuencia
            if item['tipo'] in tiposKeys: #revisa que cada elemento sea del tipo aceptado, ya sea move, wait, o tool
                valor = item['valor'] #toma el valor del tipo indicado, sea cual sea
                funcionComprobacion = self.tipos[item['tipo']] #según el tipo del elemento, obtiene la función que cmoprueba su valor
                try:
                    funcionComprobacion(valor, tipo)  # Llama a la función de comprobación para el valor del elemento
                except ValueError as e: #si la comprobación devuelve un error
                    return str(e)  # devuelve el error de la función
            else:
                return (f"[item: {item['tipo']}] Tipo de item no válido.")

        # Aquí podrías agregar lógica de validación o transformación si es necesario
        return self.repository.create(titulo, tipo, movimientos)


    def get_all_secuencias(self):
        return self.repository.get_all()

    def get_secuencia(self, id):
        return self.repository.get_by_id(id)

    def update_secuencia(self, id, **kwargs):
        return self.repository.update(id, **kwargs)

    def delete_secuencia(self, id):
        return self.repository.delete(id)
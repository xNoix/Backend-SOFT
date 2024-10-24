from robot.adapters.persistence.IMPSecuenciaMovimientosRepository import SecuenciaMovimientoRepository

class SecuenciaMovimientoService:
    def __init__(self):
        self.repository = SecuenciaMovimientoRepository()

        self.tipo = ("joints", "pose")
        self.tipos = {"wait": self.waitComp,
                      "move": self.moveComp,
                      "tool": self.toolComp
                      }
        
    def waitComp(self, valor, tipo = None):
        """Comprueba que el valor devuelto es un entero, esto indica segundos"""
        if isinstance(valor, int):
            pass
        else:
            raise ValueError("[item: wait] El valor entregado en 'wait' no es de tipo entero.")

    
    def moveComp(self, valor, tipo):
        """Comprueba la sintaxis y semantica para joints y pose"""

        if tipo == "joints":
            pass
        elif tipo == "pose":
            pass

    def toolComp(self, valor, tipo):
        """Comprueba que la instruccion de la herramienta sea valida"""
        if valor not in ["agarrar", "soltar"]:
            raise ValueError("[item: tool] Instrucción de herramienta no valida.")

    def get_all_secuencias(self):
        return self.repository.get_all()

    def get_secuencia(self, id):
        return self.repository.get_by_id(id)

    #reservado para cuando haya usuarios
    """def create_secuencia(self, usuario, titulo, tipo, movimientos, privado):
        # Aquí podrías agregar lógica de validación o transformación si es necesario
        return self.repository.create(usuario, titulo, tipo, movimientos, privado)"""
    
    def create_secuencia(self, titulo, tipo, movimientos):

        tipos = list(self.tipos.keys())
        for item in movimientos:
            if item["tipo"] in tipos:
                valor = item["valor"]
                funcionComprobacion = self.tipos[item["tipo"]]
                try:
                    funcionComprobacion(valor, tipo)  # Llama a la función de comprobación
                except ValueError as e:
                    return str(e)  # O manejar el error como desees
            else:
                return (f"[item: {item["tipo"]}] Tipo de item no válido.")
        
        if tipo not in self.tipo:
            return ("Solo se admiten movimientos del tipo 'joints' o 'pose'.")


        # Aquí podrías agregar lógica de validación o transformación si es necesario
        return self.repository.create(titulo, tipo, movimientos)

    def update_secuencia(self, id, **kwargs):
        return self.repository.update(id, **kwargs)

    def delete_secuencia(self, id):
        return self.repository.delete(id)
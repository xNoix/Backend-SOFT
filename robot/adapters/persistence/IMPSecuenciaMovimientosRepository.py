from robot.adapters.persistence.models import SecuenciaMovimiento
from django.db import transaction

class SecuenciaMovimientoRepository:

    def _to_dict(self, secuencia): #listo
        """Convierte una instancia de SecuenciaMovimiento a un diccionario"""
        return {
            "id": secuencia.id,
            #"usuario": secuencia.usuario,
            "titulo": secuencia.titulo,
            "tipo": secuencia.tipo,
            "movimientos": secuencia.movimientos,
            #"privado": secuencia.privado,
            "fechacreado": secuencia.fechacreado
        }


    def get_all(self): #listo
        secuencias = SecuenciaMovimiento.objects.all()
        return [self._to_dict(secuencia) for secuencia in secuencias]

    def get_by_id(self, id): #listo
        try:
            secuencia = SecuenciaMovimiento.objects.get(id=id)
            return self._to_dict(secuencia)
        except SecuenciaMovimiento.DoesNotExist:
            return None

    @transaction.atomic
    def create(self, titulo, tipo, movimientos): #listo
        secuencia = SecuenciaMovimiento(
            #usuario=usuario,
            titulo=titulo,
            tipo=tipo,
            movimientos=movimientos,
            #privado=privado
        )
        secuencia.save()
        return ("Secuencia creada con éxito")

    @transaction.atomic
    def update(self, id, **kwargs): #no revisado aun
        secuencia = self.get_by_id(id)
        if secuencia:
            for attr, value in kwargs.items():
                setattr(secuencia, attr, value)
            secuencia.save()
        return secuencia

    @transaction.atomic
    def delete(self, id):
        secuencia = SecuenciaMovimiento.objects.get(id=id)
        if secuencia:
            print("eliminar")
            secuencia.delete()
        return ("Secuencia eliminada con exito")
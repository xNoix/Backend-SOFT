from robot.adapters.persistence.models import SecuenciaMovimiento
from django.db import transaction

class SecuenciaMovimientoRepository:
    def get_all(self):
        return SecuenciaMovimiento.objects.all()

    def get_by_id(self, id):
        return SecuenciaMovimiento.objects.filter(id=id).first()

    @transaction.atomic
    def create(self, usuario, titulo, tipo, movimientos, privado):
        secuencia = SecuenciaMovimiento(
            usuario=usuario,
            titulo=titulo,
            tipo=tipo,
            movimientos=movimientos,
            privado=privado
        )
        secuencia.save()
        return secuencia

    @transaction.atomic
    def update(self, id, **kwargs):
        secuencia = self.get_by_id(id)
        if secuencia:
            for attr, value in kwargs.items():
                setattr(secuencia, attr, value)
            secuencia.save()
        return secuencia

    @transaction.atomic
    def delete(self, id):
        secuencia = self.get_by_id(id)
        if secuencia:
            secuencia.delete()
        return secuencia
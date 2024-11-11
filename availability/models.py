from django.db import models
from hotels.models import *


class Reservations(models.Model):
    habitacion = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    dias_reservados = models.IntegerField()
    usuario = models.PositiveIntegerField()
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario} por {self.dias_reservados} en {self.habitacion.hotel}-{self.habitacion}"

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        unique_together = ("habitacion", "usuario")


class PaymentsReservations(models.Model):
    reserva = models.OneToOneField(Reservations, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    id_transaccion = models.CharField(max_length=100)
    fecha = models.DateField()
    metodo_pago = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.fecha} - {self.reserva} - {self.monto}"

    class Meta:
        verbose_name = "Pago de reserva"
        verbose_name_plural = "Pagos de reservas"

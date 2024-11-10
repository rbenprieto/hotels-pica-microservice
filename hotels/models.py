from django.db import models


class Hotels(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    image = models.URLField(max_length=500)
    short_description = models.TextField()
    large_description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.city}"

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"
        unique_together = ("name", "city", "address")


class Rooms(models.Model):
    TIPO_HABITACION_CHOICES = [
        ("EST", "Estándar"),
        ("DLX", "Deluxe"),
        ("VIP", "VIP"),
        ("SUI", "Suite"),
    ]

    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    tipo_habitacion = models.CharField(max_length=3, choices=TIPO_HABITACION_CHOICES)
    nombre = models.CharField(max_length=100)
    numero_habitaciones_disponibles = models.IntegerField()
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()

    # Beneficios generales
    tiene_vista_al_mar = models.BooleanField(default=False)
    tiene_aire_acondicionado = models.BooleanField(default=False)
    tiene_wifi = models.BooleanField(default=True)
    tiene_desayuno_incluido = models.BooleanField(default=False)
    tiene_bano_privado = models.BooleanField(default=True)
    tiene_television = models.BooleanField(default=True)
    tiene_jacuzzi = models.BooleanField(default=False)
    tiene_minibar = models.BooleanField(default=False)
    tiene_servicio_a_habitacion = models.BooleanField(default=True)
    tiene_caja_fuerte = models.BooleanField(default=True)
    tiene_balcón = models.BooleanField(default=False)

    # Información adicional
    metros_cuadrados = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    tipo_cama = models.CharField(max_length=50, default="Cama doble")
    numero_de_camas = models.IntegerField(default=1)
    admite_mascotas = models.BooleanField(default=False)
    tiene_acceso_para_discapacitados = models.BooleanField(default=False)
    tiene_zona_de_trabajo = models.BooleanField(default=False)

    # Tecnología y entretenimiento
    tiene_sistema_sonido = models.BooleanField(default=False)
    tiene_smart_tv = models.BooleanField(default=False)
    tiene_asistente_virtual = models.BooleanField(default=False)

    # Seguridad
    tiene_detector_humo = models.BooleanField(default=True)
    tiene_rociadores = models.BooleanField(default=True)
    tiene_sistema_de_seguridad = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - {self.tipo_habitacion}"

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        unique_together = ("hotel", "nombre", "tipo_habitacion")

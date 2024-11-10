from django.contrib import admin
from .models import Hotels, Rooms


@admin.register(Hotels)
class HotelsAdmin(admin.ModelAdmin):
    model = Hotels
    list_display = ("name", "city", "address", "phone", "email")
    list_display_links = list_display
    list_per_page = 50


@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    model = Rooms
    list_display = (
        "nombre",
        "tipo_habitacion",
        "hotel",
        "precio_por_noche",
    )
    list_display_links = list_display
    list_per_page = 50

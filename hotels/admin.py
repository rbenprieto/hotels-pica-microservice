from django.contrib import admin
from .models import Hotels

@admin.register(Hotels)
class HotelsAdmin(admin.ModelAdmin):
    model = Hotels
    list_display = (
        "name",
        "city",
        "address",
        "phone",
        "email"
    )
    list_display_links = list_display
    list_per_page = 50

from django.contrib import admin
from .models import Farm, Produce

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'location','description', 'logo', 'created_at', 'updated_at')


@admin.register(Produce)
class ProduceAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'description', 'price', 'quantity', 'image', 'created_at', 'updated_at')


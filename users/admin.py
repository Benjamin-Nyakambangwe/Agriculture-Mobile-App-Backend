from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('first_name',)
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'bio',  'profile_pic', 'created_at', 'updated_at')

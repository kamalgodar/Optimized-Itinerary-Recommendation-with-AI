from django.contrib import admin
from .models import Log

# Register your models here.
class LogAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Log, LogAdmin)
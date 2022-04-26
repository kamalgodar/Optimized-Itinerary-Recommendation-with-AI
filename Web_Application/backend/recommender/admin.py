from django.contrib import admin
from .models import SeededRecs

# Register your models here.
class SeededRecAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(SeededRecs, SeededRecAdmin)
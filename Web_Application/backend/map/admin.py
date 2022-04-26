from django.contrib import admin
from .models import Place,Genre,Rating
from django.contrib.gis import admin

# Register your models here.
class PlaceAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class GenreAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Place, PlaceAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Rating, RatingAdmin)
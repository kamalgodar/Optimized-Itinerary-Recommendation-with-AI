from pyexpat import model
from django.db import models
from location_field.models.spatial import LocationField
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point
from tourist.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.utils import timezone

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    photo = models.ImageField(blank=True, upload_to='place',default='media/place/default.jpeg')
    location= LocationField(based_fields=['pulchowk campus'],zoom=7,default=Point(85.3178166,27.6828417))
    genres = models.ManyToManyField(Genre, related_name="places")

    def __str__(self):
        return self.name

    @property
    def lat_lng(self):
        return f"({self.location[1]},{self.location[0]})"
    
    @property
    def lat(self):
        return f"{self.location[1]}"
    
    @property 
    def long(self):
        return f"{self.location[0]}"

class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(5)])
    rating_timestamp = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=8, default='explicit')

    def __str__(self):
        return "user_id: {}, place_id: {}, rating: {}, type: {}"\
            .format(self.user_id, self.place_id, self.rating, self.type)

    

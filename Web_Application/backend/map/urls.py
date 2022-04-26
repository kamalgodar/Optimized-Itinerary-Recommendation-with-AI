from django.urls import path,include
from .views import index,recommend,detail,search_recommend,searchcollaborative_recommend
from .apiviews import PlaceList, PlaceDetail, PlaceRecommend, RatingList, RatingDetail, CollaborativeRecommend, HybridRecommend, ItineraryRecommend

urlpatterns = [
    path('',index,name='home'),
    path('recommend',recommend,name='recommend'),
    path('place/<int:place_id>', detail, name='detail'),
    path('search', search_recommend, name='search'),
    path('search-collaborative', searchcollaborative_recommend, name='search-collaborative'),
    path('api/places/',PlaceList.as_view(), name = "places_list"),
    path('api/places/<int:pk>', PlaceDetail.as_view(), name = "places_detail"),
    path('api/places/recommend/<str:place>', PlaceRecommend.as_view(), name='places_recommend'),
    path('api/rating/', RatingList.as_view(), name='rating_list'),
    path('api/rating/<int:pk>', RatingDetail.as_view(), name='rating_detail'),
    path('api/places/recommend/collaborative/<int:pk>', CollaborativeRecommend.as_view(), name='collaborative_recommend'),
    path('api/recommend/hybrid', HybridRecommend.as_view(), name='hybrid_recommend'),
    path('api/itinerary/', ItineraryRecommend.as_view(), name='itinerary_recommend'),
]
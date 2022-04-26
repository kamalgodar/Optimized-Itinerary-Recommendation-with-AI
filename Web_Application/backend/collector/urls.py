from unicodedata import name
from django.urls import path 
from .apiviews import LogList,LogDetail,PopularityRecommend

urlpatterns = [
    path('',LogList.as_view(), name="log_list"),
    path('<int:pk>',LogDetail.as_view(), name="log_detail"),
    path('chart',PopularityRecommend.as_view(), name="popularity_recommend"),
]
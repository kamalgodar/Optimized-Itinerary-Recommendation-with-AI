from django.urls import path 
from .apiviews import get_association_rules_for, recs_using_association_rules

urlpatterns = [
    path('association_content/<int:content_id>', get_association_rules_for, name="get_association_rules_for"),
    path('association_user/<int:user_id>', recs_using_association_rules, name="association_user"),
]
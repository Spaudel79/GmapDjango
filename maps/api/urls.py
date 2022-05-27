from django.urls import path
from .import views


urlpatterns = [
    path('api/location/',views.LocationView.as_view(),name='api-location'),
]
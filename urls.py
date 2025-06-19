from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', include('polls.urls')),
    path('', include('polls.urls')),
    
]
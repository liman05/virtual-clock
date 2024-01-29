from django.urls import path
from .views import *

urlpatterns = [
    path('view', view_clock, name="clock"),
    
]

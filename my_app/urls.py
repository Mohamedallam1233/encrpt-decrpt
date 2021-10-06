from django.urls import path
from . import views
urlpatterns = [
    path('',views.encrypt , name = "encrypt"),
    path('decrypt',views.decrypt , name = "decrypt"),
]

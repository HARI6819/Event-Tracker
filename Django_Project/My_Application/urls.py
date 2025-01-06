from django.urls import path
from . import views

urlpatterns = [
    path("home1",views.home),
    path('logout',views.logout_view)
]

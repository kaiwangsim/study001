from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("money/<str:pk>/", views.money, name="money"),

]


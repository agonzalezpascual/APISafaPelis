from django.urls import path

from api import views

urlpatterns = [
    path('', views.apiOverView, name="api-overview"),
    path('lista/', views.peliList, name="lista"),
    path('detail/<str:pk>/', views.peliDetalle, name="detail"),
    path('add/', views.peliAdd, name="anadir"),
]
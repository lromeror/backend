from django.urls import path
from . import views

urlpatterns = [
    path('v1/backend/', views.BackEndApi.as_view()),
    path('v1/backend/<str:pk>/', views.BackendDetailAPI.as_view()),
]

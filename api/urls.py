from django.urls import path
from . import views

urlpatterns = [
    path('v1/backend/', views.BackEndApi.as_view(), name='firebase_resources' ),
]
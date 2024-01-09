from django.urls import path
from . import views

app_name = 'crop'
urlpatterns = [
    path('', views.index, name="index"),
    path('prediction', views.prediction, name="prediction"),
    path('result', views.result, name="result")
]

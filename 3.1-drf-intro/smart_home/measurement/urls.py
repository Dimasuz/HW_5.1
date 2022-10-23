from django.contrib import admin
from django.urls import path

from .views import SensorsView, SensorView, MeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты

    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),

]

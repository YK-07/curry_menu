from django.urls import path
from . import views


urlpatterns = [
    path('', views.CalculationPageView, name='calculation'),
    path('curry/',views.CurryPageView, name='curry'),
]
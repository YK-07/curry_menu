from django.urls import path
from . import views


urlpatterns = [
    path('',views.IndexPageView, name='index'),
    path('calculation/', views.CalculationPageView, name='calculation'),

]
from django.urls import path
from . import views


urlpatterns = [
    path('',views.CurryPageView, name='curry'),
    path('calculation/', views.CalculationPageView, name='calculation'),

]
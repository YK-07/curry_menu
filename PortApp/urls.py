from django.urls import path
from . import views
'''
urlpatterns = [
    path('', CalculationPageView.as_view()),
    path('curry/',CurryPageView.as_view()),
]
path('', views.Calculate, name='Calculate'),
'''
urlpatterns = [
    path('', views.CalculationPageView, name='calculation'),
    path('curry/',views.CurryPageView, name='curry'),
]
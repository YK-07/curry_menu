from django.urls import path
#from .views import CalculationPageView, CurryPageView
from . import views
'''
urlpatterns = [
    path('', CalculationPageView.as_view()),
    path('curry/',CurryPageView.as_view()),
]
'''
urlpatterns = [
    path('', views.CalculationPageView, name='calculation'),
    path('curry/',views.CurryPageView, name='curry'),
]
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
'''
class CalculationPageView(TemplateView):
    template_name = "calculation.html"

class CurryPageView(TemplateView):
    template_name = "curry.html"
'''
def CalculationPageView(request):
    return render(request, "calculation.html")

def CurryPageView(request):
    return render(request, "curry.html")


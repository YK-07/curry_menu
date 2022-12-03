from django.shortcuts import render
from .form import numForm

# Create your views here.
'''
from django.views.generic import TemplateView
class CalculationPageView(TemplateView):
    template_name = "calculation.html"

class CurryPageView(TemplateView):
    template_name = "curry.html"
'''
def CalculationPageView(request):
    if request.method == 'POST':
        form = numForm(request.POST)
        if form.is_valid():# バリデーションを行う

            chicken=float(form.cleaned_data['chicken'])
            rice=float(form.cleaned_data['rice'])
            ans=chicken/100*108 + rice*538
    else:
        form=numForm()
        ans=""
    return render(request, "calculation.html",{'form':form, 'ans' : ans})

def CurryPageView(request):
    return render(request, "curry.html")

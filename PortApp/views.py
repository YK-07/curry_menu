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
def CurryPageView(request):
    return render(request, "curry.html")

def CalculationPageView(request):
    if request.method == 'POST':
        form = numForm(request.POST)
        if form.is_valid():# バリデーションを行う

            chicken=float(form.cleaned_data['chicken'])
            rice=float(form.cleaned_data['rice'])
            onion=float(form.cleaned_data['onion'])
            calorie=chicken/100*108 + rice*538 + onion/100*33
            protein=chicken/100*23 + rice*8 + onion/100*1
            ans=f'カロリー: {str(calorie)}kcal \n タンパク質: {str(protein)}g'
    else:
        form=numForm()
        ans=""
    return render(request, "calculation.html",{'form':form, 'ans' : ans})



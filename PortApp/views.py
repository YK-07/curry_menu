from django.shortcuts import render
from .form import numForm

# Create your views here.

def IndexPageView(request):
    return render(request, "index.html")
    
def CalculationPageView(request):
    if request.method == 'POST':
        form = numForm(request.POST)

        if form.is_valid():# バリデーションを行う

            meals=int(form.cleaned_data['meals'])
            chicken=float(form.cleaned_data['chicken'])
            onion=float(form.cleaned_data['onion'])
            carrot=float(form.cleaned_data['carrot'])
            tomato=float(form.cleaned_data['tomato'])
            rice=float(form.cleaned_data['rice'])
            egg=float(form.cleaned_data['egg'])
           
            if meals==1:
                calorie=round(chicken/100*108 + rice*538 + onion/100*33 + carrot/100*39 + tomato*84 + egg*87,2)
                protein=round(chicken/100*23 + rice*8 + onion/100*1 + + carrot/100*0.7 + tomato*4.8 + egg*7.4,2)
                ans=f'[{str(meals)}食分] カロリー: {str(calorie)}kcal \n タンパク質: {str(protein)}g'
            else:
                calorie=round(chicken/100*108 + rice*538 + onion/100*33 + carrot/100*39 + tomato*84 + egg*87,2)
                calorie_meal=round(calorie/meals,2)
                protein=round(chicken/100*23 + rice*8 + onion/100*1 + + carrot/100*0.7 + tomato*4.8 + egg*7.4,2)
                protein_meal=round(protein/meals,2)
                ans_meals=f'[{str(meals)}食分] カロリー: {str(calorie)}kcal \n　　　タンパク質: {str(protein)}g\n' 
                ans_meal=f'[1食分] カロリー: {str(calorie_meal)}kcal \n 　　　タンパク質: {str(protein_meal)}g'
                ans=ans_meals + ans_meal
    else:
        form=numForm()
        ans=""
    return render(request, "calculation.html",{'form':form, 'ans' : ans})



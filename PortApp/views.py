from django.shortcuts import render
from .form import numForm

# Create your views here.

def CurryPageView(request):
    return render(request, "curry.html")
    
def CalculationPageView(request):
    if request.method == 'POST':
        form = numForm(request.POST)

        if form.is_valid():# バリデーションを行う

            chicken=float(form.cleaned_data['chicken'])
            onion=float(form.cleaned_data['onion'])
            carrot=float(form.cleaned_data['carrot'])
            tomato=float(form.cleaned_data['tomato'])
            meals=int(form.cleaned_data['meals'])
            rice=float(form.cleaned_data['rice'])
            if meals==0:
                ans='0以外の数字で、何食分か入力してください'
            elif meals==1:
                calorie=round(chicken/100*108 + rice*538 + onion/100*33 + carrot/100*39 + tomato*84,2)
                protein=round(chicken/100*23 + rice*8 + onion/100*1 + + carrot/100*0.7 + tomato*4.8,2)
                ans=f'[{str(meals)}食分] カロリー: {str(calorie)}kcal \n タンパク質: {str(protein)}g'
            else:
                calorie=round(chicken/100*108 + rice*538 + onion/100*33 + carrot/100*39 + tomato*84,2)
                calorie_meal=round(calorie/meals,2)
                protein=round(chicken/100*23 + rice*8 + onion/100*1 + + carrot/100*0.7 + tomato*4.8,2)
                protein_meal=round(protein/meals,2)
                ans_meals=f'[{str(meals)}食分] カロリー: {str(calorie)}kcal \n　　　タンパク質: {str(protein)}g\n' 
                ans_meal=f'[1食分] カロリー: {str(calorie_meal)}kcal \n 　　　タンパク質: {str(protein_meal)}g'
                ans=ans_meals + ans_meal
    else:
        form=numForm()
        ans=""
    return render(request, "calculation.html",{'form':form, 'ans' : ans})



from django.shortcuts import render
from .form import numForm

# Create your views here.

def IndexPageView(request):
    return render(request, "index.html")
    
def CalculationPageView(request):
    if request.method == 'POST':
        form = numForm(request.POST)

        if form.is_valid():# バリデーションを行う

            #入力受け取り
            meals=int(form.cleaned_data['meals'])
            chicken=float(form.cleaned_data['chicken'])
            onion=float(form.cleaned_data['onion'])
            carrot=float(form.cleaned_data['carrot'])
            tomato=float(form.cleaned_data['tomato'])
            rice=float(form.cleaned_data['rice'])
            egg=float(form.cleaned_data['egg'])
            sex=float(form.cleaned_data['sex'])
            height=float(form.cleaned_data['height'])
            weight=float(form.cleaned_data['weight'])
            age=float(form.cleaned_data['age'])
            intensity=float(form.cleaned_data['intensity'])
            
            #基礎代謝、カロリー消費計算
            ans_burn=''
            if sex!=0 and height!=0 and weight!=0:
                if sex==1:#男性
                    basal_metabolism=round(13.397*weight + 4.799*height - 5.677*age + 88.362,2)
                    calorie_burn=round(basal_metabolism*intensity,2)
                    protein_cons=round(weight*1.5,2)
                elif sex==2:#女性
                    basal_metabolism=round(9.247*weight + 3.098*height - 4.33*age + 447.593,2)
                    calorie_burn=round(basal_metabolism*intensity,2)
                    protein_cons=round(weight*1.5,2)
                
                ans_burn=f'基礎代謝：約{str(basal_metabolism)}kcal　一日の消費カロリー：約{str(calorie_burn)}kcal　タンパク質量摂取目安：約{protein_cons}g'

            #摂取カロリー計算
            calorie=round(chicken/100*108 + rice*538 + onion/100*33 + carrot/100*39 + tomato*84 + egg*87,2)
            protein=round(chicken/100*23 + rice*8 + onion/100*1 + + carrot/100*0.7 + tomato*4.8 + egg*7.4,2)
            ans_meals=f'[{str(meals)}食分] カロリー: {str(calorie)}kcal \n 　　　タンパク質: {str(protein)}g\n'

            if meals==1:
                ans=ans_meals + ans_burn

            else:
                calorie_meal=round(calorie/meals,2)
                protein_meal=round(protein/meals,2)
                ans_meal=f'[1食分] カロリー: {str(calorie_meal)}kcal \n 　　　タンパク質: {str(protein_meal)}g\n'
                ans=ans_meals + ans_meal + ans_burn
    else:
        form=numForm()
        ans=""
    return render(request, "calculation.html",{'form':form, 'ans' : ans})


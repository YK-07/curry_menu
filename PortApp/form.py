from django import forms

class numForm(forms.Form):
  #入力フォーム
  meals = forms.DecimalField(label='何食分', initial=1, min_value=1, help_text='何食分作るのか入力してください', required=True)
  chicken = forms.DecimalField(label='鶏むね肉(g)', initial=0, min_value=0, step_size=10, required=True)
  onion = forms.DecimalField(label='玉ねぎ(g)', initial=0, min_value=0, step_size=10, required=True)
  carrot = forms.DecimalField(label='にんじん(g)', initial=0, min_value=0, step_size=10, required=True)
  tomato = forms.DecimalField(label='トマト缶(缶)', initial=0, min_value=0, step_size=0.1, required=True)
  rice = forms.DecimalField(label='白米(合)', initial=0, min_value=0, step_size=0.25, required=True)
  egg = forms.DecimalField(label='卵Mサイズ(個)', initial=0, min_value=0, step_size=1, required=True)
  sex = forms.DecimalField(label='性別', initial=0, min_value=0, step_size=1, help_text='男性は1を、女性は2を入力してください', required=True)
  height = forms.DecimalField(label='身長(cm)', initial=0, min_value=0, step_size=1, required=True)
  weight = forms.DecimalField(label='体重(kg)', initial=0, min_value=0, step_size=1, required=True)
  age = forms.DecimalField(label='年齢', initial=20, min_value=0,required=True)
  intensity = forms.DecimalField(label='活動レベル', initial=1.2, min_value=0, step_size=0.15, help_text='ほぼ運動しない(1.2),軽い運動 (1.35),中程度の運動(1.5),激しい運動(1.8)',required=True)
  
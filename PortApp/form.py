from django import forms

class numForm(forms.Form):
  meals = forms.DecimalField(label='何食分', initial=1, min_value=1, help_text='何食分作るのか入力してください', required=True)
  chicken = forms.DecimalField(label='鶏むね肉(g)', initial=0, min_value=0, step_size=10, required=True)
  onion = forms.DecimalField(label='玉ねぎ(g)', initial=0, min_value=0, step_size=10, required=True)
  carrot = forms.DecimalField(label='にんじん(g)', initial=0, min_value=0, step_size=10, required=True)
  tomato = forms.DecimalField(label='トマト缶(缶)', initial=0, min_value=0, step_size=0.1, required=True)
  rice = forms.DecimalField(label='白米(合)', initial=0, min_value=0, step_size=0.25, required=True)
  egg = forms.DecimalField(label='卵Mサイズ(個)', initial=0, min_value=0, step_size=1, required=True)
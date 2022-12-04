from django import forms

class numForm(forms.Form):
  chicken = forms.DecimalField(label='鶏むね肉(g)', initial=0, required=True)
  onion = forms.DecimalField(label='玉ねぎ(g)', initial=0, required=True)
  carrot = forms.DecimalField(label='にんじん(g)', initial=0, required=True)
  tomato = forms.DecimalField(label='トマト缶(缶)', initial=0, required=True)
  meals = forms.DecimalField(label='何食分か', initial=1, required=True)
  rice = forms.DecimalField(label='白米(合)', initial=0, required=True)
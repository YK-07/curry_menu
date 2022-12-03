from django import forms

class numForm(forms.Form):
  chicken = forms.DecimalField(label='鶏むね肉(g)', initial=0, required=True)
  rice = forms.DecimalField(label='白米(合)', initial=0, required=True)
  onion = forms.DecimalField(label='玉ねぎ(g)', initial=0, required=True)

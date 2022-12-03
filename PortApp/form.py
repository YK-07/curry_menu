from django import forms

class numForm(forms.Form):
  chicken = forms.DecimalField(label='鶏むね肉', initial=1000, required=True)
  rice = forms.DecimalField(label='白米', initial=0, required=True)

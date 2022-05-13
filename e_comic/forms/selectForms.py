from django import forms


class SelectForm(forms.Form):
    point = forms.fields.FloatField(min_value=0.00, max_value=5.00, widget=forms.widgets.TextInput)
    select1 = forms.fields.ChoiceField(required=True, widget=forms.widgets.Select)
    select2 = forms.fields.ChoiceField(required=True, widget=forms.widgets.Select)
    select3 = forms.fields.ChoiceField(required=True, widget=forms.widgets.Select)


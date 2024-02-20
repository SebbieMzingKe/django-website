from django import forms 


class FruitSearchForm(forms.Form):
    search_query = forms.CharField(max_length=255, required = False, label = 'search for a fruit')
from django import forms

class ObyektivkaForm(forms.Form):
    date_birth = forms.DateField()
    nationality = forms.CharField(max_length=100)
    degree = forms.CharField(max_length=100)
    languages = forms.CharField()
    national_rewards = forms.CharField()
    place_birth = forms.CharField()
    partiyaviylik = forms.CharField()
    completed = forms.CharField()
    education_reward = forms.CharField()
    
    

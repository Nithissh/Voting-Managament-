from django import forms

from . import models

class survey_form(forms.ModelForm):
    CHOICES = [('Male','Male'),('Female','Female')]
    GENDER=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
    class Meta:
        model=models.election_survey_details
        fields=['first_name','last_name','dob','city','party_name']

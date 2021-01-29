from django.shortcuts import render
from . import models,forms

from django.http import HttpResponseRedirect
def home_view(request):
    return render(request,'survey_app/home.html')

def fill(request):
    survey_form=forms.survey_form()
    if request.method=='POST':
        survey_form=forms.survey_form(request.POST)
        if survey_form.is_valid():
            gender=survey_form.cleaned_data['GENDER']
            dob=survey_form.cleaned_data['dob']
            first_name=survey_form.cleaned_data['first_name']
            last_name=survey_form.cleaned_data['last_name']
            city=survey_form.cleaned_data['city']
            party_name=survey_form.cleaned_data['party_name']

            survey=models.election_survey_details()

            survey.gender=gender
            survey.first_name=first_name
            survey.last_name=last_name
            survey.city=city
            survey.dob=dob
            survey.party_name=party_name

            survey.save()
            return HttpResponseRedirect('/')
        else:
            print('form invalid')
    return render(request,'survey_app/survey_form.html',{'survey_form':survey_form})

def results(request):
    aaa=models.election_survey_details.objects.all().filter(party_name='AAA').count()
    aab=models.election_survey_details.objects.all().filter(party_name='AAB').count()
    aac=models.election_survey_details.objects.all().filter(party_name='AAC').count()
    aad=models.election_survey_details.objects.all().filter(party_name='AAD').count()

    dict={
        'aaa':aaa,
        'aab':aab,
        'aac':aac,
        'aad':aad,
    }
    return render(request,'survey_app/results.html',context=dict)

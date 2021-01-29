from django.urls import path

from survey_app import views

urlpatterns = [
    
    path('fill',views.fill,name='fill'),
    path('results',views.results,name='results'),
   
]

from django.db import models


class election_survey_details(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    dob=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    parties=[('AAA','AAA'),('AAB','AAB'),('AAC','AAC'),('AAD','AAD')]
    party_name= models.CharField(max_length=10,choices=parties)

    created_on=models.DateField(auto_now=True)

    def __str__(self):
        return self.party_name

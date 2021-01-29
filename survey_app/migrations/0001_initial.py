enerated by Django 3.0.5 on 2020-12-30 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='election_survey_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('party_name', models.CharField(choices=[('AAA', 'AAA'), ('AAB', 'AAB'), ('AAC', 'AAC'), ('AAD', 'AAD')], max_length=10)),
                ('created_on', models.DateField(auto_now=True)),
            ],
        ),
    ]

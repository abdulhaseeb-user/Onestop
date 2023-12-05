# Generated by Django 4.2.5 on 2023-12-04 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Onestop_App', '0004_faculty_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='course',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='section',
        ),
        migrations.AddField(
            model_name='faculty',
            name='course',
            field=models.ManyToManyField(related_name='faculty', to='Onestop_App.course'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='section',
            field=models.ManyToManyField(related_name='faculty', to='Onestop_App.section'),
        ),
    ]

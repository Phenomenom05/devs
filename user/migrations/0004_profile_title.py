# Generated by Django 4.2.7 on 2023-11-05 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile_skill_project_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

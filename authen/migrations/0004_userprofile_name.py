# Generated by Django 5.1.4 on 2025-01-12 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0003_rename_sex_userprofile_gender_userprofile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.TextField(default=''),
        ),
    ]

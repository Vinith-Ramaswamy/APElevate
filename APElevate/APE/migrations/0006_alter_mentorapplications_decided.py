# Generated by Django 4.0.6 on 2023-02-13 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APE', '0005_rename_accepted_mentorapplications_decided'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorapplications',
            name='decided',
            field=models.BooleanField(default=False),
        ),
    ]

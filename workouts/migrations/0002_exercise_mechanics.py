# Generated by Django 3.0.6 on 2020-05-16 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='mechanics',
            field=models.CharField(choices=[('Comp', 'Compound'), ('Iso', 'Isolation'), ('NA', 'Not Applicable')], default='NA', max_length=4),
        ),
    ]
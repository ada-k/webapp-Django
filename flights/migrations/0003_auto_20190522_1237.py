# Generated by Django 2.2.1 on 2019-05-22 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='flights',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='flights.Flight'),
        ),
    ]

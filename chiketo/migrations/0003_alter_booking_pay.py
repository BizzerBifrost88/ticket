# Generated by Django 5.1 on 2024-10-06 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chiketo', '0002_alter_booking_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='pay',
            field=models.TextField(choices=[('not pay', 'Not Pay'), ('paid', 'Paid')], default='not pay'),
        ),
    ]

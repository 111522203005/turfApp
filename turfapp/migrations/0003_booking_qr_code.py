# Generated by Django 4.2.5 on 2024-01-20 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turfapp', '0002_booking_mobile_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qr_codes/'),
        ),
    ]
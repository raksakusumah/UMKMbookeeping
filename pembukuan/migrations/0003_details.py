# Generated by Django 4.0.6 on 2022-07-12 06:22

from django.db import migrations, models
from phone_field import PhoneField

class Migration(migrations.Migration):

    dependencies = [
        ('pembukuan', '0002_auto_20220710_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('pemilik', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', PhoneField(blank=True)),
                ('field', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
    ]

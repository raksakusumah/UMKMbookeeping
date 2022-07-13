# Generated by Django 4.0.6 on 2022-07-12 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pembukuan', '0005_pembukuan_company'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='details',
            options={'verbose_name_plural': 'Company'},
        ),
        migrations.AlterField(
            model_name='pembukuan',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pembukuan.details'),
        ),
    ]
# Generated by Django 4.0.6 on 2022-07-13 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pembukuan', '0014_remove_pembukuan_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='pembukuan',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pembukuan.category'),
        ),
    ]
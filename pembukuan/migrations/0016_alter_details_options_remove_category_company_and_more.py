# Generated by Django 4.0.6 on 2022-07-13 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pembukuan', '0015_pembukuan_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='details',
            options={'verbose_name_plural': 'Company'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='company',
        ),
        migrations.AlterField(
            model_name='pembukuan',
            name='category',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.0.6 on 2022-07-13 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pembukuan', '0018_pembukuan_categ'),
        ('produk', '0003_produk_company_vendor_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='produk',
            name='vend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pembukuan.category'),
        ),
    ]
# Generated by Django 2.2.4 on 2020-12-25 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hollylandApp', '0014_auto_20201225_2257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='products',
            new_name='product_id',
        ),
    ]

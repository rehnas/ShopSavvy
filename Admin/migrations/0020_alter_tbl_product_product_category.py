# Generated by Django 4.2 on 2023-07-06 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0019_alter_tbl_product_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_product',
            name='product_category',
            field=models.CharField(max_length=50),
        ),
    ]

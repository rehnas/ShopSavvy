# Generated by Django 4.2 on 2023-07-06 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0018_remove_tbl_newuser_newuser_confirmpassword_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_product',
            name='product_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.tbl_category'),
        ),
    ]
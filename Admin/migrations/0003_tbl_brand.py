# Generated by Django 4.2 on 2023-05-08 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_tbl_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand_name', models.CharField(max_length=50)),
            ],
        ),
    ]

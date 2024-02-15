# Generated by Django 4.2 on 2024-02-08 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0002_delete_tbl_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_newuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newuser_name', models.CharField(max_length=50)),
                ('newuser_contact', models.CharField(max_length=50)),
                ('newuser_email', models.CharField(max_length=50)),
                ('newuser_address', models.CharField(max_length=50)),
                ('newuser_photo', models.FileField(upload_to='newuser_imgs/')),
                ('newuser_proof', models.FileField(upload_to='newuser_imgs/')),
                ('newuser_password', models.CharField(max_length=50)),
            ],
        ),
    ]
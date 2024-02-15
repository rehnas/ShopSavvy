# Generated by Django 4.2 on 2023-12-18 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0022_alter_tbl_employee_employee_name'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_title', models.CharField(max_length=50)),
                ('complaint_content', models.TextField(max_length=50)),
                ('complaint_status', models.IntegerField(default=0)),
                ('complaint_date', models.DateField(auto_now=True)),
                ('complaint_replay', models.CharField(max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_newuser')),
            ],
        ),
    ]
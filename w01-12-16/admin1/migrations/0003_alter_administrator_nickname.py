# Generated by Django 5.1.3 on 2024-12-10 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0002_alter_administrator_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='nickname',
            field=models.CharField(default='관리자', max_length=100),
        ),
    ]
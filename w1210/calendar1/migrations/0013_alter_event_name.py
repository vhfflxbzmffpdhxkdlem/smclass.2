# Generated by Django 5.1.3 on 2024-12-10 08:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar1', '0012_alter_event_name'),
        ('loginpage', '0003_alter_member_nicname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='loginpage.member'),
        ),
    ]
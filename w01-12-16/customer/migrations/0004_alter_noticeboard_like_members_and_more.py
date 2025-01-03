# Generated by Django 5.1.3 on 2024-12-11 04:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0004_administrator_ano'),
        ('customer', '0003_alter_noticeboard_bfile_and_more'),
        ('loginpage', '0002_alter_member_birthday_alter_member_nicname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticeboard',
            name='like_members',
            field=models.ManyToManyField(blank=True, related_name='lik_noticeboards', to='loginpage.member'),
        ),
        migrations.AlterField(
            model_name='noticeboard',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin1.administrator'),
        ),
    ]

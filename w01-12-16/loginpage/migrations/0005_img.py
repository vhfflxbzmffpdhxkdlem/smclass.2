# Generated by Django 5.1.3 on 2024-12-17 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginpage', '0004_alter_member_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('img', models.ImageField(blank=True, default='../static/images/calendar1/default_profile.png', null=True, upload_to='images/')),
            ],
        ),
    ]

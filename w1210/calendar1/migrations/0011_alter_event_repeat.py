# Generated by Django 5.1.3 on 2024-12-10 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar1', '0010_alter_event_location_alter_event_memo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='repeat',
            field=models.CharField(default='none', max_length=10),
        ),
    ]
# Generated by Django 5.1.3 on 2024-12-10 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar1', '0007_alter_event_end_date_alter_event_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-17 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_content_mdiary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='group_diary',
        ),
        migrations.AddField(
            model_name='content',
            name='group_diary',
            field=models.ManyToManyField(blank=True, to='diary.groupdiary'),
        ),
    ]

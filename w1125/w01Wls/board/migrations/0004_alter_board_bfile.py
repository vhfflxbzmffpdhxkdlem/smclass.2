# Generated by Django 5.1.3 on 2024-11-25 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_board_bfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='bfile',
            field=models.ImageField(null=True, upload_to='board'),
        ),
    ]
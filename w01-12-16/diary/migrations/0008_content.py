# Generated by Django 5.1.3 on 2024-12-11 08:38

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0007_groupdiary'),
        ('loginpage', '0002_alter_member_birthday_alter_member_nicname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('cno', models.AutoField(primary_key=True, serialize=False)),
                ('ctitle', models.CharField(max_length=1000)),
                ('ccontent', models.TextField(null=True)),
                ('cdate', models.DateField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, null=True, upload_to='diary_images/')),
                ('group_diary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='diary.groupdiary')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='loginpage.member')),
            ],
        ),
    ]

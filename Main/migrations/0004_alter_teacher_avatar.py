# Generated by Django 5.0.6 on 2024-06-13 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_alter_teacher_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='avatar',
            field=models.ImageField(upload_to='teacher_profiles/'),
        ),
    ]
# Generated by Django 3.0.4 on 2020-03-22 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0005_student_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='prfile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
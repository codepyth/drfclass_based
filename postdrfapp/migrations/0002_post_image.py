# Generated by Django 3.2.6 on 2021-08-22 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postdrfapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/%y/%m/%d/'),
        ),
    ]
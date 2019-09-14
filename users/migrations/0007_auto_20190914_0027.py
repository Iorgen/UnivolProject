# Generated by Django 2.2.5 on 2019-09-14 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190913_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizator',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='organizator',
            name='city',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='organizator',
            name='country',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='organizator',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics/'),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='description',
            field=models.TextField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics/'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='city',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='country',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]

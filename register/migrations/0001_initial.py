# Generated by Django 4.1.3 on 2022-12-23 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.CharField(max_length=20)),
                ('password', models.TextField()),
                ('retype_password', models.TextField()),
            ],
        ),
    ]

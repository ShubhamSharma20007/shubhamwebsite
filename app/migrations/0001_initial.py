# Generated by Django 4.2 on 2023-07-30 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=52)),
                ('useremail', models.EmailField(max_length=254)),
                ('textfield', models.CharField(max_length=512)),
            ],
        ),
    ]
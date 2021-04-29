# Generated by Django 2.0 on 2017-12-13 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('mobileno', models.CharField(max_length=10)),
                ('emailid', models.EmailField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemno', models.CharField(max_length=20)),
                ('itemname', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.CharField(max_length=20)),
                ('itemno', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]

# Generated by Django 2.2.3 on 2019-08-10 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=900)),
                ('address', models.CharField(max_length=900)),
                ('numOfCustomers', models.IntegerField()),
            ],
        ),
    ]

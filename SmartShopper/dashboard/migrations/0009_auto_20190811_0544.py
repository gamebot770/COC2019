# Generated by Django 2.2.3 on 2019-08-11 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_item_totalstock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='totalStock',
        ),
        migrations.AlterField(
            model_name='item',
            name='soldDaily',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='soldMonth',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='soldWeekly',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='soldYear',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 2.0.7 on 2019-08-18 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bvisa', '0003_auto_20190817_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bvisa',
            name='project',
            field=models.CharField(max_length=70),
        ),
    ]

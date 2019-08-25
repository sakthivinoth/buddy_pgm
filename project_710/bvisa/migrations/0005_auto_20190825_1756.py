# Generated by Django 2.0.7 on 2019-08-25 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bvisa', '0004_auto_20190818_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bvisa',
            name='capability',
            field=models.CharField(choices=[('Capability1', 'Capability1'), ('Capability2', 'Capability2')], max_length=20),
        ),
        migrations.AlterField(
            model_name='bvisa',
            name='employee_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='bvisa',
            name='enterprise_id',
            field=models.EmailField(max_length=40),
        ),
        migrations.AlterField(
            model_name='bvisa',
            name='project',
            field=models.CharField(choices=[('Cigna', 'Cigna'), ('Anthem', 'Anthem')], max_length=20),
        ),
    ]

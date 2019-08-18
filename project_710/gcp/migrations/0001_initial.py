# Generated by Django 2.0.7 on 2019-08-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GCP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=70)),
                ('enterprise_id', models.EmailField(max_length=70)),
                ('project', models.CharField(max_length=20)),
                ('whatsapp_number', models.DecimalField(decimal_places=0, max_digits=10)),
                ('travel_start_date', models.DateField()),
                ('travel_end_date', models.DateField()),
                ('capability', models.CharField(choices=[('1', 'option1'), ('2', 'option2')], max_length=1)),
            ],
        ),
    ]

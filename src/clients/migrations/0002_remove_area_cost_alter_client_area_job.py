# Generated by Django 5.1.1 on 2024-09-04 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='cost',
        ),
        migrations.AlterField(
            model_name='client',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.area'),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.area')),
            ],
        ),
    ]

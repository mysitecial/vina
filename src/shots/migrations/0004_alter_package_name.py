# Generated by Django 5.1.1 on 2024-09-20 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shots', '0003_rename_project_name_project_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]

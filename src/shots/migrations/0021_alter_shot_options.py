# Generated by Django 5.1.1 on 2024-10-09 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shots', '0020_shot_md_alter_shot_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shot',
            options={'ordering': ['id']},
        ),
    ]

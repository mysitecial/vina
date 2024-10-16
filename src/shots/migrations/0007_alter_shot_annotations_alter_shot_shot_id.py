# Generated by Django 5.1.1 on 2024-09-23 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shots', '0006_alter_package_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shot',
            name='annotations',
            field=models.ImageField(blank=True, null=True, upload_to='{package.id}/annotations/'),
        ),
        migrations.AlterField(
            model_name='shot',
            name='shot_id',
            field=models.CharField(editable=False, max_length=24, unique=True),
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-20 05:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_alter_job_name'),
        ('shots', '0002_shot_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='shot',
            old_name='shot_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='package',
            name='package_name',
        ),
        migrations.AddField(
            model_name='package',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='package',
            name='name',
            field=models.CharField(default='default_package_name', max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='shot',
            name='annotations',
            field=models.ImageField(blank=True, upload_to='annotations/'),
        ),
        migrations.AddField(
            model_name='shot',
            name='word_ref',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='shot',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shots', to='clients.job'),
        ),
        migrations.AlterField(
            model_name='shot',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shots', to='shots.package'),
        ),
        migrations.AlterField(
            model_name='shot',
            name='shot_id',
            field=models.CharField(editable=False, max_length=36, unique=True),
        ),
    ]
# Generated by Django 5.1.1 on 2024-09-28 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shots', '0019_alter_shot_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='shot',
            name='md',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='shot',
            name='status',
            field=models.CharField(choices=[('#0', 'Bidding'), ('#1', 'Bidded'), ('#2', 'Go'), ('#3', 'Hold'), ('#4', 'Working'), ('#5', 'Qc-ing'), ('#6', 'Done'), ('#7', 'Posted'), ('#8', 'Additional'), ('#9', 'FB'), ('#10', 'Cancel')], default='#0', max_length=20),
        ),
    ]

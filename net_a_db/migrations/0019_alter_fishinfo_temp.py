# Generated by Django 4.1 on 2024-03-22 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('net_a_db', '0018_alter_fishinfo_fish_size_alter_fishinfo_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishinfo',
            name='temp',
            field=models.CharField(blank=True, choices=[(1, '26'), (2, '10'), (3, '14'), (4, '17'), (5, '20'), (6, '22'), (7, '24'), (8, '25'), (9, '27'), (10, '28'), (11, '29'), (12, '30'), (13, '31'), (14, '33')], max_length=20, null=True),
        ),
    ]

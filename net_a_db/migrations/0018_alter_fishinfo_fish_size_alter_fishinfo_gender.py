# Generated by Django 4.1 on 2024-03-22 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('net_a_db', '0017_alter_fishinfo_fish_mixed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishinfo',
            name='fish_size',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='fishinfo',
            name='gender',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

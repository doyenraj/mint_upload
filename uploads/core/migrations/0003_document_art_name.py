# Generated by Django 2.1 on 2021-10-26 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160801_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='art_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-06 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporte', '0003_copiadora'),
    ]

    operations = [
        migrations.AddField(
            model_name='copiadora',
            name='Bandeja',
            field=models.IntegerField(default='1', max_length=2),
        ),
    ]

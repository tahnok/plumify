# Generated by Django 2.2.6 on 2019-10-19 18:38

from django.db import migrations, models
import overlays.models


class Migration(migrations.Migration):

    dependencies = [
        ('overlays', '0003_overlay_satallite_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overlay',
            name='satallite_map',
            field=models.ImageField(blank=True, null=True, upload_to=overlays.models.satallite_map_path),
        ),
    ]

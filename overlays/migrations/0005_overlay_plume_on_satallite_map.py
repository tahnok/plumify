# Generated by Django 2.2.6 on 2019-10-19 20:42

from django.db import migrations, models
import overlays.models


class Migration(migrations.Migration):

    dependencies = [
        ('overlays', '0004_auto_20191019_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='overlay',
            name='plume_on_satallite_map',
            field=models.ImageField(blank=True, null=True, upload_to=overlays.models.processed_map_path),
        ),
    ]

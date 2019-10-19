# Generated by Django 2.2.6 on 2019-10-19 15:13

from django.db import migrations, models
import overlays.models


class Migration(migrations.Migration):

    dependencies = [
        ('overlays', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='overlay',
            name='plume',
            field=models.ImageField(default='missing.png', upload_to=overlays.models.plume_path),
            preserve_default=False,
        ),
    ]
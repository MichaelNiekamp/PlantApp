# Generated by Django 4.0.8 on 2022-12-07 23:05

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('planty', '0005_alter_event_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='event_images'),
        ),
    ]

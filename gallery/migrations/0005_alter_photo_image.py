# Generated by Django 4.2.3 on 2023-07-29 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_alter_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]

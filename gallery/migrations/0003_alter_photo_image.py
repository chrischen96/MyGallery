# Generated by Django 4.2.3 on 2023-07-28 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]

# Generated by Django 2.2.4 on 2021-02-27 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hilo', '0011_auto_20210226_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]

# Generated by Django 2.0 on 2018-06-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalrecord',
            name='diagnosis',
            field=models.CharField(default='Default diagnosis', max_length=256),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.0 on 2018-06-07 06:58

from django.db import migrations, models
import django.db.models.deletion
import system.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('blob', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('phone', models.IntegerField()),
                ('address', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(storage=system.models.OverwriteStorage(), upload_to=system.models.idcard_directory_path)),
                ('dob', models.DateField(blank=True, null=True)),
                ('relations', models.CharField(blank=True, max_length=50, null=True)),
                ('aadhar_number', models.CharField(default='0', max_length=12)),
                ('file_no', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='pat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Patient'),
        ),
    ]

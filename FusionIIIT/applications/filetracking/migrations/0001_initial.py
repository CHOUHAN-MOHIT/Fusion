# Generated by Django 3.1.5 on 2023-03-18 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('globals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('upload_file', models.FileField(blank=True, upload_to='')),
                ('is_read', models.BooleanField(default=False)),
                ('designation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='upload_designation', to='globals.designation')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_files', to='globals.extrainfo')),
            ],
            options={
                'db_table': 'File',
            },
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receive_date', models.DateTimeField(auto_now_add=True)),
                ('forward_date', models.DateTimeField(auto_now_add=True)),
                ('remarks', models.CharField(blank=True, max_length=250, null=True)),
                ('upload_file', models.FileField(blank=True, upload_to='')),
                ('is_read', models.BooleanField(default=False)),
                ('current_design', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='globals.holdsdesignation')),
                ('current_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
                ('file_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='filetracking.file')),
                ('receive_design', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rec_design', to='globals.designation')),
                ('receiver_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Tracking',
            },
        ),
    ]

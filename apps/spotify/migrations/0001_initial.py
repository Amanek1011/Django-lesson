# Generated by Django 5.1.7 on 2025-03-26 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(blank=True, max_length=50, null=True)),
                ('album_count', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(upload_to='authors')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('song_image', models.ImageField(upload_to='songs/image')),
                ('file', models.FileField(upload_to='songs')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotify.author')),
            ],
            options={
                'verbose_name': 'Song',
                'verbose_name_plural': 'Songs',
            },
        ),
    ]

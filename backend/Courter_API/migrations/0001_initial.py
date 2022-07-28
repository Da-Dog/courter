# Generated by Django 4.0.6 on 2022-07-28 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('rental_status', models.BooleanField(default=False)),
                ('rental_start_time', models.DateTimeField(blank=True, null=True)),
                ('rental_end_time', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=64)),
                ('logged_in', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('current_court', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_court', to='Courter_API.court')),
                ('waiting_court', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='waiting_court', to='Courter_API.court')),
            ],
        ),
    ]

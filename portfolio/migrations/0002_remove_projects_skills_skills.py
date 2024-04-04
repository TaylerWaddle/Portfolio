# Generated by Django 4.2.7 on 2023-11-18 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='skills',
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.projects')),
            ],
        ),
    ]

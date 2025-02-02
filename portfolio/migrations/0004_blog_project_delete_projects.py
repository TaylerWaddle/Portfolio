# Generated by Django 4.2.7 on 2023-11-20 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_projects_skill1_projects_skill2_projects_skill3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('blog_number', models.CharField(max_length=3)),
                ('summary', models.TextField(blank=True, default='default description  -  jkfhbsvliughflkjwshbkuifgbvlsghglifvbksuyhrglbwelsuihgbliuhwliuhgri', max_length=300, null=True)),
                ('date_written', models.DateField(blank=True, default='2023-10-23', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, default='default description  -  jkfhbsvliughflkjwshbkuifgbvlsghglifvbksuyhrglbwelsuihgbliuhwliuhgri', max_length=300, null=True)),
                ('date_created', models.DateField(blank=True, default='2023-10-23', null=True)),
                ('git_link', models.URLField(blank=True, default='https://www.google.com/', null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
    ]

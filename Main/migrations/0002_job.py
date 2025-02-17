# Generated by Django 3.2 on 2021-07-10 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('salary_range', models.CharField(max_length=254)),
                ('experience', models.CharField(max_length=100)),
                ('seats_available', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.company')),
                ('skills_required', models.ManyToManyField(blank=True, to='Main.Skill')),
            ],
        ),
    ]

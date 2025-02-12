# Generated by Django 5.1.5 on 2025-01-30 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='.myimage/')),
                ('bprice', models.IntegerField()),
                ('bvar', models.CharField(max_length=5)),
                ('hprice', models.IntegerField()),
                ('hvar', models.CharField(max_length=5)),
                ('brand', models.CharField(max_length=30)),
            ],
        ),
    ]

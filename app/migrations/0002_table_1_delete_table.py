# Generated by Django 5.0.4 on 2024-07-06 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('flavour', models.TextField(max_length=200)),
                ('topings', models.TextField(max_length=200)),
                ('address', models.TextField(max_length=250)),
                ('phno', models.TextField(max_length=20)),
                ('time', models.TextField(max_length=50)),
                ('quantity', models.TextField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Table',
        ),
    ]
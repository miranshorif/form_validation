# Generated by Django 4.2.3 on 2023-07-27 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('text', models.TextField(max_length=1000, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'FeMale')], max_length=6)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

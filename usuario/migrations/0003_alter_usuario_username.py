# Generated by Django 4.2.7 on 2023-12-01 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_usuario_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(default='o', max_length=150, verbose_name='username'),
        ),
    ]
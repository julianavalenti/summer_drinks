# Generated by Django 4.2 on 2023-04-26 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_trying'),
    ]

    operations = [
        migrations.AddField(
            model_name='trying',
            name='drink',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.drink'),
            preserve_default=False,
        ),
    ]
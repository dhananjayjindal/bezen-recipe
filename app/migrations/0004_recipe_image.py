# Generated by Django 4.1 on 2022-09-11 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_recipe_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
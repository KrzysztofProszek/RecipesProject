# Generated by Django 4.2.3 on 2023-07-18 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_updated_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categorie',
        ),
    ]

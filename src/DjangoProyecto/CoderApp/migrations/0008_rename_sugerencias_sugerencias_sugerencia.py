# Generated by Django 5.0 on 2024-01-25 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoderApp', '0007_rename_repuestos_sugerencias_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sugerencias',
            old_name='sugerencias',
            new_name='sugerencia',
        ),
    ]

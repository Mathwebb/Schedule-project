# Generated by Django 4.0.5 on 2022-06-08 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='data_cricacao',
            new_name='data_criacao',
        ),
    ]

# Generated by Django 5.2 on 2025-04-08 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_post_imagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imagem',
        ),
    ]

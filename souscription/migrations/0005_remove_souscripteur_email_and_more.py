# Generated by Django 5.1 on 2024-08-11 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('souscription', '0004_delete_mode_souscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='souscripteur',
            name='email',
        ),
        migrations.RemoveField(
            model_name='souscripteur',
            name='mot_de_passe',
        ),
    ]
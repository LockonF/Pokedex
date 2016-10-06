# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 22:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0006_auto_20161005_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_has_tipo', to='pokemon.TipoPokemon'),
        ),
    ]
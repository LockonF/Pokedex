# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-04 23:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entrenador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrenadorhaspokemon',
            name='entrenador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entrenador_has_pokemon_entrenador', to='entrenador.Entrenador'),
        ),
        migrations.AlterField(
            model_name='entrenadorhaspokemon',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entrenador_has_pokemon_pokemon', to='pokemon.Pokemon'),
        ),
    ]

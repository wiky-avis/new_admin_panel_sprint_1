# Generated by Django 3.2.4 on 2023-01-31 16:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(sql='CREATE SCHEMA IF NOT EXISTS content;'),
        migrations.RunSQL(sql='ALTER ROLE app SET search_path TO content,public;'),
        migrations.CreateModel(
            name='Filmwork',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, default='', verbose_name='description')),
                ('creation_date', models.DateField(blank=True, null=True, verbose_name='creation_date')),
                ('rating', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='rating')),
                ('type', models.CharField(choices=[('movie', 'movie'), ('tv_show', 'tv_show')], default='movie', max_length=7, verbose_name='type')),
            ],
            options={
                'verbose_name': 'Filmwork',
                'verbose_name_plural': 'Filmworks',
                'db_table': 'film_work',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(blank=True, default='', verbose_name='description')),
            ],
            options={
                'verbose_name': 'genre',
                'verbose_name_plural': 'genres',
                'db_table': 'genre',
                'ordering': ('name',),
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255, verbose_name='full_name')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
                'db_table': 'person',
                'ordering': ('full_name',),
            },
        ),
        migrations.CreateModel(
            name='PersonFilmwork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role', models.TextField(default='', verbose_name='role')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.person', verbose_name='person')),
            ],
            options={
                'verbose_name_plural': 'persons',
                'db_table': 'person_film_work',
                'ordering': ('id',),
                'unique_together': {('film_work', 'person', 'role')},
            },
        ),
        migrations.CreateModel(
            name='GenreFilmwork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre', verbose_name='genre')),
            ],
            options={
                'verbose_name_plural': 'genres',
                'db_table': 'genre_film_work',
                'ordering': ('id',),
                'unique_together': {('film_work', 'genre')},
            },
        ),
        migrations.AddField(
            model_name='filmwork',
            name='genres',
            field=models.ManyToManyField(through='movies.GenreFilmwork', to='movies.Genre', verbose_name='genres'),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='persons',
            field=models.ManyToManyField(through='movies.PersonFilmwork', to='movies.Person', verbose_name='persons'),
        ),
        migrations.AlterUniqueTogether(
            name='filmwork',
            unique_together={('title', 'creation_date')},
        ),
    ]

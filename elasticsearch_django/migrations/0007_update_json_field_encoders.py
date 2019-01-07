# Generated by Django 2.0.5 on 2018-05-11 13:30

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elasticsearch_django', '0006_add_encoder_JSONField_kwarg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchquery',
            name='hits',
            field=django.contrib.postgres.fields.jsonb.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder, help_text='The list of meta info for each of the query matches returned.'),
        ),
        migrations.AlterField(
            model_name='searchquery',
            name='query',
            field=django.contrib.postgres.fields.jsonb.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder, help_text='The raw ElasticSearch DSL query.'),
        ),
    ]
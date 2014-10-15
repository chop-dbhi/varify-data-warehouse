# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Genome'
        db.delete_table('genome')


    def backwards(self, orm):
        # Adding model 'Genome'
        db.create_table('genome', (
            ('released', self.gf('django.db.models.fields.DateField')(null=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('genome', ['Genome'])


    models = {
        'genome.chromosome': {
            'Meta': {'ordering': "['order']", 'object_name': 'Chromosome', 'db_table': "'chromosome'"},
            'code': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'})
        },
        'genome.genotype': {
            'Meta': {'object_name': 'Genotype', 'db_table': "'genotype'"},
            'code': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['genome']
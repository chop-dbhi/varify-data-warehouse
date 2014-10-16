# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    depends_on = (
        ('avocado', '0035_auto__add_field_datafield_indexable__add_field_dataconcept_indexable'),
    )

    def forwards(self, orm):
        "Write your forwards methods here."
        orm['avocado.DataField'].objects.filter(app_name='samples', model_name='cohort',
            field_name__in=['investigator', 'notes']).delete()


    def backwards(self, orm):
        "Write your backwards methods here."
        pass


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 11, 27, 17, 13, 46, 939658)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 11, 27, 17, 13, 46, 939422)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'avocado.datacategory': {
            'Meta': {'ordering': "('parent__order', 'parent__name', 'order', 'name')", 'object_name': 'DataCategory'},
            'archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'_order'", 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['avocado.DataCategory']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'avocado.dataconcept': {
            'Meta': {'ordering': "('category__order', 'category__name', 'order', 'name')", 'object_name': 'DataConcept'},
            'archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['avocado.DataCategory']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fields': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'concepts'", 'symmetrical': 'False', 'through': "orm['avocado.DataConceptField']", 'to': "orm['avocado.DataField']"}),
            'formatter_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'concepts+'", 'null': 'True', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'indexable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'internal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name_plural': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'_order'", 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'queryable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'concepts+'", 'blank': 'True', 'to': "orm['sites.Site']"}),
            'sortable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'viewable': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'avocado.dataconceptfield': {
            'Meta': {'ordering': "('order', 'name')", 'object_name': 'DataConceptField'},
            'concept': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'concept_fields'", 'to': "orm['avocado.DataConcept']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'field': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'concept_fields'", 'to': "orm['avocado.DataField']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_plural': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'_order'", 'blank': 'True'})
        },
        'avocado.datacontext': {
            'Meta': {'object_name': 'DataContext'},
            'accessed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 16, 0, 0)'}),
            'count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'_count'"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('jsonfield.fields.JSONField', [], {'default': '{}', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'forks'", 'null': 'True', 'to': "orm['avocado.DataContext']"}),
            'session': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'session_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tree': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'datacontext+'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'avocado.datafield': {
            'Meta': {'ordering': "('category__order', 'category__name', 'order', 'name')", 'unique_together': "(('app_name', 'model_name', 'field_name'),)", 'object_name': 'DataField'},
            'app_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['avocado.DataCategory']", 'null': 'True', 'blank': 'True'}),
            'code_field_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_version': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'enumerable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fields+'", 'null': 'True', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'internal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'label_field_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'model_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name_plural': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'_order'", 'blank': 'True'}),
            'order_field_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_field_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'fields+'", 'blank': 'True', 'to': "orm['sites.Site']"}),
            'translator': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'unit_plural': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'})
        },
        'avocado.dataquery': {
            'Meta': {'object_name': 'DataQuery'},
            'accessed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'context_json': ('jsonfield.fields.JSONField', [], {'default': '{}', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'distinct_count': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'forks'", 'null': 'True', 'to': "orm['avocado.DataQuery']"}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'record_count': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'session': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'session_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'shared_users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'shareddataquery+'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'template': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tree': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'dataquery+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'view_json': ('jsonfield.fields.JSONField', [], {'default': '{}', 'null': 'True', 'blank': 'True'})
        },
        'avocado.dataview': {
            'Meta': {'object_name': 'DataView'},
            'accessed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 16, 0, 0)'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('jsonfield.fields.JSONField', [], {'default': '{}', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'forks'", 'null': 'True', 'to': "orm['avocado.DataView']"}),
            'session': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'session_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'dataview+'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'avocado.revision': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'Revision'},
            'changes': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'data': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'session_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+revision'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'genome.chromosome': {
            'Meta': {'ordering': "['order']", 'object_name': 'Chromosome', 'db_table': "'chromosome'"},
            'code': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'})
        },
        'genome.genome': {
            'Meta': {'object_name': 'Genome', 'db_table': "'genome'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'released': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'genome.genotype': {
            'Meta': {'object_name': 'Genotype', 'db_table': "'genotype'"},
            'code': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'literature.pubmed': {
            'Meta': {'object_name': 'PubMed', 'db_table': "'pubmed'"},
            'pmid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'phenotypes.phenotype': {
            'Meta': {'object_name': 'Phenotype', 'db_table': "'phenotype'"},
            'articles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['literature.PubMed']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hpo_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'term': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1000'})
        },
        'samples.batch': {
            'Meta': {'unique_together': "(('project', 'name'),)", 'object_name': 'Batch', 'db_table': "'batch'"},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'investigator': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'batches'", 'to': "orm['samples.Project']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'samples.cohort': {
            'Meta': {'object_name': 'Cohort', 'db_table': "'cohort'"},
            'autocreated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'context': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['avocado.DataContext']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['samples.Project']", 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'samples': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['samples.Sample']", 'through': "orm['samples.CohortSample']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'samples.cohortsample': {
            'Meta': {'unique_together': "(('object_set', 'set_object'),)", 'object_name': 'CohortSample', 'db_table': "'cohort_sample'"},
            'added': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['samples.Cohort']", 'db_column': "'cohort_id'"}),
            'removed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'set_object': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['samples.Sample']", 'db_column': "'sample_id'"})
        },
        'samples.cohortvariant': {
            'Meta': {'unique_together': "(('variant', 'cohort'),)", 'object_name': 'CohortVariant', 'db_table': "'cohort_variant'"},
            'af': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_index': 'True'}),
            'cohort': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['samples.Cohort']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'variant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['variants.Variant']"})
        },
        'samples.person': {
            'Meta': {'object_name': 'Person', 'db_table': "'person'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'mrn': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'proband': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'relations': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['samples.Person']", 'through': "orm['samples.Relation']", 'symmetrical': 'False'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        'samples.project': {
            'Meta': {'unique_together': "(('name',),)", 'object_name': 'Project', 'db_table': "'project'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'samples.relation': {
            'Meta': {'ordering': "('person', '-generation')", 'object_name': 'Relation', 'db_table': "'relation'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'generation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'family'", 'to': "orm['samples.Person']"}),
            'relative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'relative_of'", 'to': "orm['samples.Person']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'samples.result': {
            'Meta': {'unique_together': "(('sample', 'variant'),)", 'object_name': 'Result', 'db_table': "'sample_result'"},
            'baseq_rank_sum': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coverage_alt': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'coverage_ref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'downsampling': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'fisher_strand': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'genotype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['genome.Genotype']", 'null': 'True', 'blank': 'True'}),
            'genotype_quality': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'haplotype_score': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'homopolymer_run': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_dbsnp': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'mq': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mq0': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mq_rank_sum': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'phred_scaled_likelihood': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'quality': ('django.db.models.fields.FloatField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'quality_by_depth': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'read_depth': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'read_pos_rank_sum': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sample': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['samples.Sample']"}),
            'spanning_deletions': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'strand_bias': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'variant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['variants.Variant']"})
        },
        'samples.sample': {
            'Meta': {'unique_together': "(('batch', 'name'),)", 'object_name': 'Sample', 'db_table': "'sample'"},
            'batch': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'samples'", 'to': "orm['samples.Batch']"}),
            'bio_sample': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'md5': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'samples'", 'null': 'True', 'to': "orm['samples.Person']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'samples'", 'to': "orm['samples.Project']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'version': ('django.db.models.fields.IntegerField', [], {})
        },
        'samples.samplerun': {
            'Meta': {'object_name': 'SampleRun', 'db_table': "'sample_run'"},
            'completed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'genome': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['genome.Genome']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sample': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['samples.Sample']"})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'variants.variant': {
            'Meta': {'unique_together': "(('chr', 'pos', 'ref', 'alt'),)", 'object_name': 'Variant', 'db_table': "'variant'"},
            'alt': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'articles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['literature.PubMed']", 'db_table': "'variant_pubmed'", 'symmetrical': 'False'}),
            'chr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['genome.Chromosome']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liftover': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'md5': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'phenotypes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['phenotypes.Phenotype']", 'through': "orm['variants.VariantPhenotype']", 'symmetrical': 'False'}),
            'pos': ('django.db.models.fields.IntegerField', [], {}),
            'ref': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'rsid': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['variants.VariantType']", 'null': 'True'})
        },
        'variants.variantphenotype': {
            'Meta': {'object_name': 'VariantPhenotype', 'db_table': "'variant_phenotype'"},
            'hgmd_id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phenotype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['phenotypes.Phenotype']"}),
            'variant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['variants.Variant']"})
        },
        'variants.varianttype': {
            'Meta': {'ordering': "['order']", 'object_name': 'VariantType', 'db_table': "'variant_type'"},
            'code': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['samples']

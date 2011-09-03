# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Deployment'
        db.create_table('epioprices_deployment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('storage_usage', self.gf('django.db.models.fields.FloatField')(default=2.0)),
            ('bandwidth_usage', self.gf('django.db.models.fields.FloatField')(default=5.0)),
        ))
        db.send_create_signal('epioprices', ['Deployment'])

        # Adding model 'Instance'
        db.create_table('epioprices_instance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('deployment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['epioprices.Deployment'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('instance_type', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('memory_usage', self.gf('django.db.models.fields.FloatField')(default=128)),
        ))
        db.send_create_signal('epioprices', ['Instance'])


    def backwards(self, orm):
        
        # Deleting model 'Deployment'
        db.delete_table('epioprices_deployment')

        # Deleting model 'Instance'
        db.delete_table('epioprices_instance')


    models = {
        'epioprices.deployment': {
            'Meta': {'object_name': 'Deployment'},
            'bandwidth_usage': ('django.db.models.fields.FloatField', [], {'default': '5.0'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'storage_usage': ('django.db.models.fields.FloatField', [], {'default': '2.0'})
        },
        'epioprices.instance': {
            'Meta': {'object_name': 'Instance'},
            'amount': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'deployment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['epioprices.Deployment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance_type': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'memory_usage': ('django.db.models.fields.FloatField', [], {'default': '128'})
        }
    }

    complete_apps = ['epioprices']

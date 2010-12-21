# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Service'
        db.create_table('cmsplugin_portafolio_service', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('cmsplugin_portafolio', ['Service'])

        # Adding model 'Client'
        db.create_table('cmsplugin_portafolio_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('cmsplugin_portafolio', ['Client'])

        # Adding model 'Proyect'
        db.create_table('cmsplugin_portafolio_proyect', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(related_name='proyectos', to=orm['cmsplugin_portafolio.Service'])),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(related_name='proyectos', to=orm['cmsplugin_portafolio.Client'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description_short', self.gf('django.db.models.fields.TextField')()),
            ('description_long', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('cmsplugin_portafolio', ['Proyect'])


    def backwards(self, orm):
        
        # Deleting model 'Service'
        db.delete_table('cmsplugin_portafolio_service')

        # Deleting model 'Client'
        db.delete_table('cmsplugin_portafolio_client')

        # Deleting model 'Proyect'
        db.delete_table('cmsplugin_portafolio_proyect')


    models = {
        'cmsplugin_portafolio.client': {
            'Meta': {'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'cmsplugin_portafolio.proyect': {
            'Meta': {'object_name': 'Proyect'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'proyectos'", 'to': "orm['cmsplugin_portafolio.Client']"}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'description_long': ('django.db.models.fields.TextField', [], {}),
            'description_short': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'proyectos'", 'to': "orm['cmsplugin_portafolio.Service']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'cmsplugin_portafolio.service': {
            'Meta': {'object_name': 'Service'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cmsplugin_portafolio']

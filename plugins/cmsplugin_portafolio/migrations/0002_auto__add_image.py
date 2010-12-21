# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Image'
        db.create_table('cmsplugin_portafolio_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('proyect', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['cmsplugin_portafolio.Proyect'])),
        ))
        db.send_create_signal('cmsplugin_portafolio', ['Image'])


    def backwards(self, orm):
        
        # Deleting model 'Image'
        db.delete_table('cmsplugin_portafolio_image')


    models = {
        'cmsplugin_portafolio.client': {
            'Meta': {'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'cmsplugin_portafolio.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'proyect': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['cmsplugin_portafolio.Proyect']"})
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
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'cmsplugin_portafolio.service': {
            'Meta': {'object_name': 'Service'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cmsplugin_portafolio']

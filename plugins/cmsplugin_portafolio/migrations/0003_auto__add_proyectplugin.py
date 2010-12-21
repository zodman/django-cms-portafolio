# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ProyectPlugin'
        db.create_table('cmsplugin_proyectplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('cmsplugin_portafolio', ['ProyectPlugin'])

        # Adding M2M table for field portafolio on 'ProyectPlugin'
        db.create_table('cmsplugin_portafolio_proyectplugin_portafolio', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyectplugin', models.ForeignKey(orm['cmsplugin_portafolio.proyectplugin'], null=False)),
            ('proyect', models.ForeignKey(orm['cmsplugin_portafolio.proyect'], null=False))
        ))
        db.create_unique('cmsplugin_portafolio_proyectplugin_portafolio', ['proyectplugin_id', 'proyect_id'])


    def backwards(self, orm):
        
        # Deleting model 'ProyectPlugin'
        db.delete_table('cmsplugin_proyectplugin')

        # Removing M2M table for field portafolio on 'ProyectPlugin'
        db.delete_table('cmsplugin_portafolio_proyectplugin_portafolio')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
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
        'cmsplugin_portafolio.proyectplugin': {
            'Meta': {'object_name': 'ProyectPlugin', 'db_table': "'cmsplugin_proyectplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'portafolio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cmsplugin_portafolio.Proyect']", 'symmetrical': 'False'})
        },
        'cmsplugin_portafolio.service': {
            'Meta': {'object_name': 'Service'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cmsplugin_portafolio']

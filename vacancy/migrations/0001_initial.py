# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Candidate'
        db.create_table('vacancy_candidate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('cv', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('opening', self.gf('django.db.models.fields.related.ForeignKey')(related_name='candidates', to=orm['vacancy.EnableOpening'])),
        ))
        db.send_create_signal('vacancy', ['Candidate'])

        # Adding model 'Require'
        db.create_table('vacancy_require', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('vacancy', ['Require'])

        # Adding model 'Opening'
        db.create_table('vacancy_opening', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('require', self.gf('django.db.models.fields.related.ForeignKey')(related_name='openings', to=orm['vacancy.Require'])),
        ))
        db.send_create_signal('vacancy', ['Opening'])

        # Adding model 'EnableOpening'
        db.create_table('vacancy_enableopening', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('opening', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vacancy.Opening'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('vacancy', ['EnableOpening'])


    def backwards(self, orm):
        
        # Deleting model 'Candidate'
        db.delete_table('vacancy_candidate')

        # Deleting model 'Require'
        db.delete_table('vacancy_require')

        # Deleting model 'Opening'
        db.delete_table('vacancy_opening')

        # Deleting model 'EnableOpening'
        db.delete_table('vacancy_enableopening')


    models = {
        'vacancy.candidate': {
            'Meta': {'object_name': 'Candidate'},
            'cv': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'opening': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'candidates'", 'to': "orm['vacancy.EnableOpening']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'vacancy.enableopening': {
            'Meta': {'object_name': 'EnableOpening'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opening': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vacancy.Opening']"}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'vacancy.opening': {
            'Meta': {'object_name': 'Opening'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'require': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'openings'", 'to': "orm['vacancy.Require']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'vacancy.require': {
            'Meta': {'object_name': 'Require'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['vacancy']

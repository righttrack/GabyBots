# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WebSource'
        db.create_table('scraping_websource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scraper', self.gf('gbots.util.fields.WeakForeignKey')(to=orm['dynamic_scraper.Scraper'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('scraper_runtime', self.gf('gbots.util.fields.WeakForeignKey')(to=orm['dynamic_scraper.SchedulerRuntime'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('pattern', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('scraping', ['WebSource'])

        # Adding model 'Anchor'
        db.create_table('scraping_anchor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('href', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal('scraping', ['Anchor'])

        # Adding model 'Image'
        db.create_table('scraping_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('src', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('alt', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('link', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scraping.Anchor'])),
        ))
        db.send_create_signal('scraping', ['Image'])

        # Adding model 'Section'
        db.create_table('scraping_section', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('scraping', ['Section'])

        # Adding model 'BaseItemModel'
        db.create_table('scraping_baseitemmodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('checker_runtime', self.gf('gbots.util.fields.WeakForeignKey')(to=orm['dynamic_scraper.SchedulerRuntime'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scraping.WebSource'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('scraping', ['BaseItemModel'])

        # Adding model 'Article'
        db.create_table('scraping_article', (
            ('baseitemmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['scraping.BaseItemModel'], unique=True, primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('sections', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scraping.Section'])),
            ('images', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scraping.Image'])),
            ('links', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scraping.Anchor'])),
        ))
        db.send_create_signal('scraping', ['Article'])


    def backwards(self, orm):
        # Deleting model 'WebSource'
        db.delete_table('scraping_websource')

        # Deleting model 'Anchor'
        db.delete_table('scraping_anchor')

        # Deleting model 'Image'
        db.delete_table('scraping_image')

        # Deleting model 'Section'
        db.delete_table('scraping_section')

        # Deleting model 'BaseItemModel'
        db.delete_table('scraping_baseitemmodel')

        # Deleting model 'Article'
        db.delete_table('scraping_article')


    models = {
        'dynamic_scraper.schedulerruntime': {
            'Meta': {'ordering': "['next_action_time']", 'object_name': 'SchedulerRuntime'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'next_action_factor': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'next_action_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'num_zero_actions': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'runtime_type': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'})
        },
        'dynamic_scraper.scrapedobjclass': {
            'Meta': {'ordering': "['name']", 'object_name': 'ScrapedObjClass'},
            'checker_scheduler_conf': ('django.db.models.fields.TextField', [], {'default': '\'"MIN_TIME": 1440,\\n"MAX_TIME": 10080,\\n"INITIAL_NEXT_ACTION_FACTOR": 1,\\n"ZERO_ACTIONS_FACTOR_CHANGE": 5,\\n"FACTOR_CHANGE_FACTOR": 1.3,\\n\''}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'scraper_scheduler_conf': ('django.db.models.fields.TextField', [], {'default': '\'"MIN_TIME": 15,\\n"MAX_TIME": 10080,\\n"INITIAL_NEXT_ACTION_FACTOR": 10,\\n"ZERO_ACTIONS_FACTOR_CHANGE": 20,\\n"FACTOR_CHANGE_FACTOR": 1.3,\\n\''})
        },
        'dynamic_scraper.scraper': {
            'Meta': {'ordering': "['name', 'scraped_obj_class']", 'object_name': 'Scraper'},
            'checker_ref_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'checker_type': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'checker_x_path': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'checker_x_path_result': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_type': ('django.db.models.fields.CharField', [], {'default': "'H'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_items_read': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_items_save': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pagination_append_str': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'pagination_on_start': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pagination_page_replace': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pagination_type': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'scraped_obj_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dynamic_scraper.ScrapedObjClass']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'})
        },
        'scraping.anchor': {
            'Meta': {'object_name': 'Anchor'},
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        'scraping.article': {
            'Meta': {'object_name': 'Article', '_ormbases': ['scraping.BaseItemModel']},
            'baseitemmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['scraping.BaseItemModel']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'images': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scraping.Image']"}),
            'links': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scraping.Anchor']"}),
            'sections': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scraping.Section']"})
        },
        'scraping.baseitemmodel': {
            'Meta': {'object_name': 'BaseItemModel'},
            'checker_runtime': ('gbots.util.fields.WeakForeignKey', [], {'to': "orm['dynamic_scraper.SchedulerRuntime']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scraping.WebSource']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'scraping.image': {
            'Meta': {'object_name': 'Image'},
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scraping.Anchor']"}),
            'src': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'scraping.section': {
            'Meta': {'object_name': 'Section'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'scraping.websource': {
            'Meta': {'object_name': 'WebSource'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pattern': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'scraper': ('gbots.util.fields.WeakForeignKey', [], {'to': "orm['dynamic_scraper.Scraper']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'scraper_runtime': ('gbots.util.fields.WeakForeignKey', [], {'to': "orm['dynamic_scraper.SchedulerRuntime']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['scraping']

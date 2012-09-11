from __future__ import absolute_import

import datetime
import logging
import imp
import sys

from django.db import models
from django.db import DatabaseError, transaction
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.importlib import import_module

from common.models import TranslatableLabelMixin, LiveObjectMixin
from smart_settings import SettingsNamespace
from project_setup.api import register_setup
from project_tools.api import register_tool
from statistics.api import register_statistics

#from .classes import AppBackup, StorageModuleBase, Setting

logger = logging.getLogger(__name__)


class App(TranslatableLabelMixin, LiveObjectMixin, models.Model):
    translatables = ['label', 'description', 'icon']

    #class UnableToRegister(Exception):
    #    pass
    
    name = models.CharField(max_length=64, verbose_name=_(u'name'), unique=True)
    dependencies = models.ManyToManyField('self', verbose_name=_(u'dependencies'), symmetrical=False, blank=True, null=True)
    #version
    #top_urls
    #namespace

    @classmethod
    @transaction.commit_on_success
    def register(cls, app_name):
        logger.debug('Trying to import: %s' % app_name)
        try:
            app_module = import_module(app_name)
        except ImportError:
            transaction.rollback
            logger.debug('import failed')
        else:
            logger.debug('Trying to import registry from: %s' % app_name)
            try:
                registration = import_module('%s.registry' % app_name)
            except ImportError as exception:
                transaction.rollback
                logger.debug('import failed; %s' % exception)
            else:
                if not getattr(registration, 'disabled', False):
                    try:
                        app, created = App.objects.get_or_create(name=app_name)
                    except DatabaseError:
                        transaction.rollback()
                        raise cls.UnableToRegister
                    else:
                        app.label = getattr(registration, 'label', app_name)
                        app.description = getattr(registration, 'description', u'')
                        app.dependencies.clear()
                        app.save()
                        app.icon = getattr(registration, 'icon', None)

                        for dependency_name in getattr(registration, 'dependencies', []):
                            dependency, created = App.objects.get_or_create(name=dependency_name)
                            app.dependencies.add(dependency)

                        settings = getattr(registration, 'settings', None)

                        if settings:
                            logger.debug('settings: %s' % settings)
                            settings_module = imp.new_module('settings')
                            setattr(app_module, 'settings', settings_module)
                            sys.modules['%s.settings' % app_name] = settings_module 
                            settings_namespace = SettingsNamespace(app_name, app.label, '%s.settings' % app_name)
                            for setting in settings:
                                settings_namespace.add_setting(**setting)
                              
                        for link in getattr(registration, 'setup_links', []):
                            logger.debug('setup link: %s' % link)
                            register_setup(link) 

                        for link in getattr(registration, 'tool_links', []):
                            logger.debug('tool link: %s' % link)
                            register_tool(link)
                            
                        for statistic in getattr(registration, 'statistics', []):
                            logger.debug('stattistic: %s' % statistic)
                            register_statistics(statistic)
           
    #def set_backup(self, *args, **kwargs):
    #    return AppBackup(self, *args, **kwargs)
       
    def __unicode__(self):
        return unicode(self.label)

    class Meta:
        ordering = ('name', )
        verbose_name = _(u'app')
        verbose_name_plural = _(u'apps')


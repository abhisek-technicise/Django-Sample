# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
'''
from .models import employee_Tables

def do_stuff(sender, **kwargs):
    mymodel = sender.get_model('employee_Tables')
    mymodel.objects.get() # etc...
'''
class EmpCrudConfig(AppConfig):
    name = 'emp_CRUD'
    '''
    def ready(self):
        post_migrate.connect(do_stuff, sender=self)
    '''

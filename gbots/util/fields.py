from django.db import models

__author__ = 'jeffmay'

class WeakForeignKey(models.ForeignKey):
    """
    Loosly couple this to a foreign table to prevent cascading deletes, invalid ids, and to permit missing ids.
    """
    def __init__(self, *args, **kwargs):
        kwargs.update(blank=True, null=True, on_delete=models.SET_NULL)
        super(WeakForeignKey, self).__init__(*args, **kwargs)

# Allow South to introspect these fields
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^gbots\.util\.fields\.WeakForeignKey"])

#class ListField(models.ForeignKey):
#    def __init__(self, factory):
#

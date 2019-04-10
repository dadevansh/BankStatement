# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from reader.models import StatEntry

admin.site.register(StatEntry)

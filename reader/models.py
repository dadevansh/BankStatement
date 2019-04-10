# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class StatEntry(models.Model):
    txn_date = models.CharField(max_length=50)
    val_date = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    ref_no = models.CharField(max_length=100)
    debit = models.CharField(max_length=20)
    credit = models.CharField(max_length=20)
    balance = models.CharField(max_length=20)
    user = models.CharField(max_length=30)

    def __str__(self):
        return self.description

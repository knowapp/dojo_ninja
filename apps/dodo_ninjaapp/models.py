# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    desc = models.TextField()
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "object: {}, {}, {}".format(self.name, self.city, self.state)


class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas", null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "object: {}, {}".format(self.first_name, self.last_name)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Business(models.Model):
	"""docstring for businesses"""
	name = models.CharField(max_length=255)
	description = models.TextField()
	established = models.DateField()

	def __str__(self):
		return self.name


		
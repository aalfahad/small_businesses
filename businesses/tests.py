# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
class BusinessModelTestCase(TestCase):
	#docstring for BusinessModelTestCaseTestCase
	def test_create(self):
		Business.objects.create(
			name = "Coded",
			description = "The first coding bootcamp in the middle east",
			established = "2015-7-26"
			)
from django.test import TestCase
from django.db import models

from ..models import Solicitation


class CoreModelsTest(TestCase):
    def setUp(self):
        self.obj = Solicitation()

    def test_instance(self):
        """Order should be an instance of Models"""
        self.assertIsInstance(self.obj, models.Model)

    def test_solicitation_attributes(self):
        attributes = ('phone', 'bond', 'departament', 'answerable',
                      'status', 'created_at', 'updated_at', 'slug')

        for attr in attributes:
            with self.subTest():
                message = '{} not found'.format(attr)
                self.assertTrue(hasattr(self.obj, attr), msg=message)

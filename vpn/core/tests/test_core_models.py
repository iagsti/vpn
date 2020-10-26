from django.test import TestCase
from django.db import models

from vpn.core.tests import mock
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

    def test_create_solicitation(self):
        requester_data = mock.make_user_data(login='77889911')
        answerable_data = mock.make_user_data(login='22334455')
        requester = mock.make_user(requester_data)
        answerable = mock.make_user(answerable_data)

        solicitation_data = mock.make_solicitation_data(
            requester, answerable)
        mock.make_solicitation(solicitation_data)

        self.assertTrue(Solicitation.objects.exists())

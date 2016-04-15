# -*- coding: utf-8 -*-
import json
import factory
from datetime import datetime
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status

from account.models import Account

User = get_user_model()


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account


class BaseTestCase(APITestCase):
    """Base configs for tests"""

    def setUp(self):
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'john-john')
        self.user.last_name = 'Lennon'
        self.user.save()
        self.account1 = AccountFactory(
            id=1, user=self.user, transaction='I', value=111.1111)
        self.account2 = AccountFactory(
            id=2, user=self.user, transaction='I', value=222.222)
        self.account3 = AccountFactory(
            id=3, user=self.user, transaction='E', value=333.333)
        self.account1.timestamp = datetime.strptime('2016-01-20', '%Y-%m-%d')
        self.account1.save()

        self.account2.timestamp = datetime.strptime('2016-03-20', '%Y-%m-%d')
        self.account2.save()

        self.account3.timestamp = datetime.strptime('2016-03-21', '%Y-%m-%d')
        self.account3.save()
        # self.client.login(username=self.user.username, password='john-john')

    def tearDown(self):
        Account.objects.all().delete()

    def test_initial(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Account.objects.count(), 3)

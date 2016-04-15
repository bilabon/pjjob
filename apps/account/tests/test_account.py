from django.core.urlresolvers import reverse
from rest_framework import status

from account.models import Account
from account.tests.base import BaseTestCase


class CheckResponceStatus(BaseTestCase):
    """Check responce statuses"""

    def test_status_account_range_api_url(self):
        '''Check status when user not logged in
        for reverse('account_range_api')
        '''
        response = self.client.get(reverse('account_range_api'))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

        response = self.client.get(
            reverse('account_range_api'),
            {'start': '2016-01-01', 'start': '2017-01-01'}
        )
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

        response = self.client.get(
            reverse('account_range_api'),
            {'start': 'qwertyu', 'start': 'oiuytr'}
        )
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

        response = self.client.get(
            reverse('account_range_api'),
            {'start': '2016-01-20', 'end': '2016-01-20', 'format': 'csv'}
        )
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_status_home_url(self):
        '''Check status when user not logged in for reverse('home')'''
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_status_account_range_api_url_logged_in(self):
        '''Check status when user logged in for reverse('account_range_api')
        '''
        self.client.login(username=self.user.username, password='john-john')
        response = self.client.get(reverse('account_range_api'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(
            reverse('account_range_api'),
            {'start': '2016-01-01', 'start': '2017-01-01'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(
            reverse('account_range_api'),
            {'start': 'qwertyu', 'start': 'oiuytr'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(
            reverse('account_range_api'),
            {'start': '2016-01-20', 'end': '2016-01-20', 'format': 'csv'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_status_home_url_logged_in(self):
        '''Check status when user logged in for reverse('home')'''
        self.client.login(username=self.user.username, password='john-john')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CheckAPIResponceData(BaseTestCase):
    '''Check count data in responce'''
    def test_account_range_api_url_data(self):
        self.client.login(username=self.user.username, password='john-john')
        response = self.client.get(reverse('account_range_api'))
        self.assertEqual(len(response.data), 2)

        response = self.client.get(
            reverse('account_range_api'),
            {'start': '2016-03-01', 'start': '2016-03-25'}
        )
        self.assertEqual(len(response.data), 2)

        response = self.client.get(
            reverse('account_range_api'),
            {'start': '2016-01-20', 'end': '2016-01-20'}
        )
        self.assertEqual(len(response.data), 1)


class CheckAPIResponceDataCsv(BaseTestCase):
    '''Check csv file in responce'''
    def test_account_range_api_url_data_csv(self):
        self.client.login(username=self.user.username, password='john-john')
        response = self.client.get(
            reverse('account_range_api'),
            {'start': '2016-01-20', 'end': '2016-01-20', 'format': 'csv'}
        )
        self.assertEqual(
            response.get('Content-Type'), 'text/csv; charset=utf-8')
        self.assertEqual(len(response.data), 1)

        response = self.client.get(
            reverse('account_range_api'),
            {'start': '2016-03-01', 'start': '2016-03-25', 'format': 'csv'}
        )
        self.assertEqual(len(response.data), 2)

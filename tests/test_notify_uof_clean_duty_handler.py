""""""
from django.test import SimpleTestCase
from django.test import Client
from django.urls import reverse
from django.http import JsonResponse
from uoffice.apis import NotifyUofCleanDutyHandler


class TestNotifyUofCleanDutyHandler(SimpleTestCase):

    def test_http_get(self):
        client = Client()
        response = client.get(reverse(NotifyUofCleanDutyHandler.ID))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response, JsonResponse))

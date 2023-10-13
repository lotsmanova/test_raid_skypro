from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from main.models import FrameworkModel


class MainTestCase(APITestCase):

    def setUp(self) -> None:
        self.framework = FrameworkModel.objects.create(
            name='Test name',
            language='Test language'
        )


    def test_list_framework(self):
        """ Тестирование отображения списка фреймворков """

        response = self.client.get(
            reverse('main:framework_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{'id': 2, 'name': 'Test name', 'language': 'Test language'}]
        )

    def test_filter_framework(self):
        response = self.client.get(
            '/frameworks/?language=Test language'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{'id': 1, 'name': 'Test name', 'language': 'Test language'}]
        )

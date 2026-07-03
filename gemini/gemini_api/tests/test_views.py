from unittest import TestCase
import pytest
from unittest.mock import patch
from movieReccomendationSystem.moviereccomendationsystem.gemini.gemini_api.tests.fixtures.factories import make_gemini_response, generate_payload
from rest_framework.test import APIClient
from rest_framework.response import Response
from rest_framework import status
pytestmark = pytest.mark.django_db


class APITestCase(TestCase):
    URL = "/api/generate/"
    def setUp(self):
        self.api_client = APIClient()

    def test_generate_text(self):
        with patch("gemini_api.views.GenerateTextView.post") as mock_cls:
            mock_cls.return_value = Response(
                {
                    'success': True,
                    'response': 'Why did the chicken cross the road?'
                },
                status=status.HTTP_200_OK

            )
            resp = self.api_client.post(
                self.URL,
                data=generate_payload(prompt="Tell me a joke?", temperature=0.9, max_tokens=256),
                format="json",
            )

            assert resp.status_code == 200
            assert resp.json()['response'] == 'Why did the chicken cross the road?'

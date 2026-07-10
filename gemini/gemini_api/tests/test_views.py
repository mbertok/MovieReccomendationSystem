from unittest import TestCase
from unittest.mock import patch

import pytest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient

from .fixtures.factories import generate_payload

pytestmark = pytest.mark.django_db


class APITestCase(TestCase):
    URL = "/api/generate/"

    def setUp(self):
        self.api_client = APIClient()

    def test_generate_text(self):
        with patch("gemini_api.views.GenerateTextView.post") as mock_cls:
            mock_cls.return_value = Response(
                {
                    "success": True,
                    "response": "Why did the chicken cross the road?",
                },
                status=status.HTTP_200_OK,
            )
            resp = self.api_client.post(
                self.URL,
                data=generate_payload(
                    prompt="Tell me a joke?", temperature=0.9, max_tokens=256
                ),
                format="json",
            )

            assert resp.status_code == 200
            assert resp.json()["response"] == "Why did the chicken cross the road?"

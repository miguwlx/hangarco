from unittest.mock import patch
from django.test import TestCase
from django.urls import reverse
from .services import DataServiceError


class AircraftSearchTests(TestCase):
    def test_home_loads(self):
        self.assertEqual(self.client.get(reverse("search")).status_code, 200)

    def test_short_query_shows_message(self):
        r = self.client.get(reverse("search"), {"q": "a"})
        self.assertContains(r, "al menos 2 caracteres")

    @patch("aircraft.views.search_aircraft", return_value=[])
    def test_no_results(self, _):
        r = self.client.get(reverse("search"), {"q": "zzzz"})
        self.assertContains(r, "No se encontraron")

    @patch("aircraft.views.search_aircraft", side_effect=DataServiceError)
    def test_api_failure(self, _):
        r = self.client.get(reverse("search"), {"q": "cessna"})
        self.assertContains(r, "No se pudo consultar")
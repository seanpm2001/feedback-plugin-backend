import json

from django.core.management import call_command
from django.test import TestCase, Client
from django.urls import reverse

from .utils import create_test_database


class EmptyChartViewTest(TestCase):
    def test_server_count_by_month(self):
        c = Client()

        response = c.get(reverse('server_count'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{}')



class ChartViewTest(TestCase):
    def test_server_count_by_month(self):
        c = Client()

        response = c.get(reverse('server_count'))
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content,
                         {
                             "title": "Server Count by Month",
                             "values": {
                                 "count": {
                                     "x": ["2022-01", "2022-02", "2022-03"],
                                     "y": [3, 4, 1]
                                 }},
                             "metadata": {
                                 "computed_start_date": "2022-01-01T00:31:55Z",
                                 "computed_end_date": "2022-03-06T19:21:42Z"
                             }})

        response = c.get(reverse('version_breakdown'))
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content,
                         {
                             "title": "Server Version Breakdown by Month",
                             "values": {
                                 "10.3": {
                                     "x": ["2022-1", "2022-2", "2022-3"],
                                     "y": [1, 1, 1]
                                 },
                                 "10.4": {
                                     "x": ["2022-1", "2022-2"],
                                     "y": [2, 2]
                                 },
                                 "10.1": {
                                     "x": ["2022-2"],
                                     "y": [1]
                                 }
                             },
                             "metadata": {
                                 "computed_start_date": "2022-01-01T00:31:55Z",
                                 "computed_end_date": "2022-03-06T19:21:42Z"
                             }})

    def setUp(self):
        create_test_database()
        call_command('compute_charts')

import unittest
#import testrequestpython.requests.get_status_code
from pythonprober import update_metrics, urllist
import responses
from prometheus_client import REGISTRY
class TestPythonProber(unittest.TestCase):
    @responses.activate
    def test_get_status_code_1(self):
        responses.add(responses.GET, 'https://httpstat.us/200', status=200)
        responses.add(responses.GET, 'https://httpstat.us/503', status=503)
        update_metrics()
        urlstatus1 = REGISTRY.get_sample_value('sample_external_url_up', {'url': 'https://httpstat.us/200'})
        urlstatus2 = REGISTRY.get_sample_value('sample_external_url_up', {'url': 'https://httpstat.us/503'})
        self.assertEqual(urlstatus1, 1)
        self.assertEqual(urlstatus2, 0)
    @responses.activate
    def test_get_status_code_2(self):
        responses.add(responses.GET, 'https://httpstat.us/200', status=404)
        responses.add(responses.GET, 'https://httpstat.us/503', status=200)
        update_metrics()
        urlstatus1 = REGISTRY.get_sample_value('sample_external_url_up', {'url': 'https://httpstat.us/200'})
        urlstatus2 = REGISTRY.get_sample_value('sample_external_url_up', {'url': 'https://httpstat.us/503'})
        self.assertEqual(urlstatus1, 0)
        self.assertEqual(urlstatus2, 1)
if __name__ == '__main__':
    unittest.main()

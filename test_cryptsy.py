import pytest
import urllib2

from Cryptsy import Api


@pytest.fixture
def api():
    return Api('KEY', 'SECRET')


@pytest.fixture
def mock_urlopen(monkeypatch):
    def _mock_urlopen(request):
        """ Mock urllib to return the url so we can check if the url is
        constructed correctly. """
        class MockRequest:
            def read(self):
                return '{"url": "%s"}' % request._Request__original

        return MockRequest()

    monkeypatch.setattr(urllib2, 'urlopen', _mock_urlopen)


def test_cryptsy_init():
    """ The Cryptsy class constructor should accept the API Key and the Secret
    in the constructor and set it on the instance. """
    instance = Api('API Key', 'Secret')
    assert instance.API_KEY == 'API Key'
    assert instance.SECRET == 'Secret'


class TestPublicApiCall:
    """ Some requests are done to the "public" API of cryptsy. """

    def test_method_should_be_added_in_the_url(self, mock_urlopen, api):
        rv = api._public_api_query('testmethod')
        assert rv['url'] == 'http://pubapi.cryptsy.com/api.php?method=testmethod'

    def test_marketid_should_be_added_as_get_parameter(self, mock_urlopen,
                                                       api):
        rv = api._public_api_query('testmethod', marketid=10)
        assert rv['url'] == 'http://pubapi.cryptsy.com/api.php?method=testmethod&marketid=10'

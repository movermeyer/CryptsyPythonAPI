import pytest
import urllib2

from mock import Mock

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


@pytest.fixture
def mock_create_order(api):
    """ Mock the create order so we can check if the correct ordertype is
    used. """
    api._create_order = Mock()


def test_buy(mock_create_order, api):
    """ The buy method should call the _create_order method with the ordertyp
    as 'Buy'. """
    api.buy(26, 10, 0.0000001)
    api._create_order.assert_called_with(26, 'Buy', 10, 0.0000001)


def test_sell(mock_create_order, api):
    """ The sell method should call the _create_order method with the ordertyp
    as 'Sell'. """
    rv = api.sell(26, 10, 0.0000001)
    api._create_order.assert_called_with(26, 'Sell', 10, 0.0000001)


def test_generate_new_address_without_parameters(api):
    """ generate_new_address should raise a ValueError when no parameters are
    provided. """
    with pytest.raises(ValueError):
        api.generate_new_address()


@pytest.fixture
def api_query_mock(api):
    api._api_query = Mock()
    return api._api_query


@pytest.fixture
def public_api_query_mock(api):
    api._public_api_query = Mock()
    return api._public_api_query


def test_generate_new_address_currencycode(api, api_query_mock):
    """ Should add currencycode as request data if provided. """
    api.generate_new_address(currencycode=10)
    api_query_mock.assert_called_with('generatenewaddress', request_data={
        'currencycode': 10
    })


def test_generate_new_address_currencyid(api, api_query_mock):
    """ Should add currencyid as request data if provided. """
    api.generate_new_address(currencyid=10)
    api_query_mock.assert_called_with('generatenewaddress', request_data={
        'currencyid': 10
    })


def test_market_data_old(api, public_api_query_mock):
    """ Should use the old marketdata method if v2 is not set to True. """
    api.market_data()
    public_api_query_mock.assert_called_with('marketdata')


def test_market_data_v2(api, public_api_query_mock):
    """ Should use the old marketdata method if v2 is not set to True. """
    api.market_data(v2=True)
    public_api_query_mock.assert_called_with('marketdatav2')

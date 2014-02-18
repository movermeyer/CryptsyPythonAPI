from Cryptsy import Cryptsy as API


def test_cryptsy_init():
    """ The Cryptsy class constructor should accept the API Key and the Secret
    in the constructor and set it on the instance. """
    instance = API('API Key', 'Secret')
    assert instance.APIKey == 'API Key'
    assert instance.Secret == 'Secret'

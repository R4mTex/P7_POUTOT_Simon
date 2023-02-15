import mock
from GrandPyApp.scripts.python.geocoder_api import Geocoder


"""
class MockResponse:
 
    @staticmethod
    def json():
        return {}

def test_geocoder_api(mocker):
    sut = Geocoder(query='')
    mocker.patch('requests.get', return_value = MockResponse())
 
    expected_value = {}
    assert sut.geocoder_api_request() == expected_value
"""


@mock.patch("GrandPyApp.scripts.python.geocoder_api.requests.get")
def test_geocoder_api_requests_get(mock_requests_get):
    sut = Geocoder(query='')
  
    mock_requests_get.return_value = mock.Mock(name='mock response', **{'status_code': 200, 'json.return_value': {}})

    assert sut.geocoder_api_request() == {}
    mock_requests_get.assert_called_once_with('https://maps.googleapis.com/maps/api/geocode/json?address=&key=AIzaSyAVtCfvLbfgSm8528irK1sEq5SpSA0zcKY')


@mock.patch("GrandPyApp.scripts.python.geocoder_api.requests.get")
def test_get_information_from_the_request(mock_requests_get):
    sut = Geocoder(query='')
    
    mock_requests_get.return_value = mock.Mock(name='mock response', **{'status_code': 200, 'json.return_value': {'status': 'OK', 'results': ''}})

    assert sut.get_information_from_the_request() == mock_requests_get.return_value
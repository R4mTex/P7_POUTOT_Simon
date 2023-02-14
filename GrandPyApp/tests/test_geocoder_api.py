from ..scripts.python.geocoder_api import Geocoder

def test_geocoder_api_request_mock_function(monkeypatch):

    def mockreturn():
        return 100

    monkeypatch.setattr(Geocoder, 'geocoder_api_request', mockreturn)

    expected_value = 100
    assert Geocoder.geocoder_api_request_mock_function() == expected_value

def test_should_get_information_from_the_request():
    sut = Geocoder('paris')
    expected_value = {
        'long_name': 'Paris',
        'status': 'OK',
        'lat': 48.856614,
        'lng': 2.3522219,
        'place_id': ['ChIJD7fiBh9u5kcRYJSMaMOCCwQ']
    }
    assert sut.get_information_from_the_request() == expected_value

def test_should_just_return_value_status():
    sut = Geocoder('fsztfdxt')
    expected_value = {
        'status' : 'ZERO_RESULTS'
    }
    assert sut.get_information_from_the_request() == expected_value

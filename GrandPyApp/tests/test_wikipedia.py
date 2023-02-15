import mock
from GrandPyApp.scripts.python.wikipedia import Wikipedia


"""
class MockResponse:
 
    @staticmethod
    def page(query):
        return {}

def test_wikipedia_api(mocker):
 
    mocker.patch('wikipediaapi.Wikipedia', return_value = MockResponse())
 
    expected_value = 'Une erreur est survenue'
    assert Wikipedia.wiki_page('paris') == expected_value
"""


@mock.patch("GrandPyApp.scripts.python.wikipedia.wikipediaapi.Wikipedia")
def test_Wikipedia_api(mock_wikipediaapi_Wikipedia):
    sut = Wikipedia
    
    mock_wikipediaapi_Wikipedia.return_value = mock.Mock(name='mock response', **{'status_code': 200,})

    assert sut.wiki_page('') == None

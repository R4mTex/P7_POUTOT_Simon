import mock
from GrandPyApp.scripts.python.wikipedia import Wikipedia


@mock.patch("GrandPyApp.scripts.python.wikipedia.wikipediaapi.Wikipedia")
def test_Wikipedia_api(mock_wikipediaapi_Wikipedia):
    sut = Wikipedia

    mock_wikipediaapi_Wikipedia.return_value = mock.Mock(name='mock response',**{'status_code': 200})

    assert sut.wiki_page('') is None

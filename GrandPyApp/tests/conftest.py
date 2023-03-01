import pytest


from ..views import app


@pytest.fixture()
def application():
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture()
def client(application):
    return application.test_client()


@pytest.fixture()
def runner(application):
    return application.test_cli_runner()

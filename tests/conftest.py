import pytest
from testapps.echo.echoapp import EchoApp


@pytest.fixture
def echoapp() -> EchoApp:
    app = EchoApp()
    return app

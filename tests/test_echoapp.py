import contextlib
import io
import re

import pytest


def test_echoapp_displays_help(echoapp) -> None:
    echoapp.setup()

    with io.StringIO() as buffer:
        with contextlib.redirect_stderr(buffer), pytest.raises(SystemExit) as e:
            echoapp.run()

            assert e.type is SystemExit
            assert e.value.code == 2

        output = buffer.getvalue()
        assert re.match("^usage:", output) is not None

    with io.StringIO() as buffer:
        with contextlib.redirect_stdout(buffer), pytest.raises(SystemExit) as e:
            echoapp.run(flags=["--help"])

            assert e.type is SystemExit
            assert e.value.code == 0

        output = buffer.getvalue()
        assert re.match("^usage:", output) is not None


def test_echoapp_echoes(echoapp) -> None:
    echoapp.setup()

    with io.StringIO() as buffer:
        with contextlib.redirect_stdout(buffer), pytest.raises(SystemExit) as e:
            echoapp.run(flags=["echo", "hi"])

            assert e.type is SystemExit
            assert e.value.code == 0

        output = buffer.getvalue()
        assert re.match("^hi$", output) is not None


def test_echoapp_shouts(echoapp) -> None:
    echoapp.setup()

    with io.StringIO() as buffer:
        with contextlib.redirect_stdout(buffer), pytest.raises(SystemExit) as e:
            echoapp.run(flags=["--shout", "echo", "hi"])

            assert e.type is SystemExit
            assert e.value.code == 0

        output = buffer.getvalue()
        assert re.match("^HI$", output) is not None

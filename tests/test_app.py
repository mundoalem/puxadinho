import contextlib
import io
import pytest
import re

#
# PRE-SETUP
#


def test_app_name_is_not_empty_pre_setup(app) -> None:
    assert app.name != ""


def test_app_description_is_not_empty_pre_setup(app) -> None:
    assert app.description != ""


def test_app_flags_is_not_empty_pre_setup(app) -> None:
    assert len(app.flags) > 0


def test_app_config_path_is_not_empty_pre_setup(app) -> None:
    assert app.config_path != ""


def test_app_subcommands_is_not_empty_pre_setup(app) -> None:
    assert len(app.subcommands) > 0


def test_app_children_is_empty_pre_setup(app) -> None:
    assert len(app.children) == 0


def test_app_parent_is_empty_pre_setup(app) -> None:
    assert app.parent is None


def test_app_parser_is_not_empty_pre_setup(app) -> None:
    assert app.parser is not None


def test_app_subparser_is_not_empty_pre_setup(app) -> None:
    assert app.subparser is not None


#
# POST-SETUP
#


def test_app_children_is_not_empty_post_setup(app) -> None:
    app.setup()
    assert len(app.children) > 0


#
# RUN
#


def test_app_displays_help(app) -> None:
    app.setup()

    with io.StringIO() as buffer:
        with contextlib.redirect_stderr(buffer):
            with pytest.raises(SystemExit) as e:
                app.run()

                assert e.type == SystemExit
                assert e.value.code == 2

        output = buffer.getvalue()
        assert re.match("^usage:", output) is not None

    with io.StringIO() as buffer:
        with contextlib.redirect_stdout(buffer):
            with pytest.raises(SystemExit) as e:
                app.run(flags=["--help"])

                assert e.type == SystemExit
                assert e.value.code == 0

        output = buffer.getvalue()
        assert re.match("^usage:", output) is not None


def test_app_invert_feature(app) -> None:
    app.setup()

    message = "Example"

    with io.StringIO() as buffer:
        with contextlib.redirect_stdout(buffer):
            with pytest.raises(SystemExit) as e:
                app.run(flags=["say", "invert", message])

                assert e.type == SystemExit
                assert e.value.code == 0

        output = buffer.getvalue()
        assert output == "elpmaxE\n"

    with io.StringIO() as buffer:
        with contextlib.redirect_stdout(buffer):
            with pytest.raises(SystemExit) as e:
                app.run(flags=["say", "--lowercase", "invert", message])

                assert e.type == SystemExit
                assert e.value.code == 0

        output = buffer.getvalue()
        assert output == "elpmaxe\n"

    with io.StringIO() as buffer:
        with contextlib.redirect_stdout(buffer):
            with pytest.raises(SystemExit) as e:
                app.run(flags=["say", "--uppercase", "invert", message])

                assert e.type == SystemExit
                assert e.value.code == 0

        output = buffer.getvalue()
        assert output == "ELPMAXE\n"


def test_app_repeat_feature(app) -> None:
    app.setup()

    message = "Example"

    with io.StringIO() as buffer:
        with contextlib.redirect_stdout(buffer):
            with pytest.raises(SystemExit) as e:
                app.run(flags=["say", "repeat", message])

                assert e.type == SystemExit
                assert e.value.code == 0

        output = buffer.getvalue()
        assert output == "Example\n"

    with io.StringIO() as buffer:
        with contextlib.redirect_stdout(buffer):
            with pytest.raises(SystemExit) as e:
                app.run(flags=["say", "--lowercase", "repeat", message])

                assert e.type == SystemExit
                assert e.value.code == 0

        output = buffer.getvalue()
        assert output == "example\n"

    with io.StringIO() as buffer:
        with contextlib.redirect_stdout(buffer):
            with pytest.raises(SystemExit) as e:
                app.run(flags=["say", "--uppercase", "repeat", message])

                assert e.type == SystemExit
                assert e.value.code == 0

        output = buffer.getvalue()
        assert output == "EXAMPLE\n"

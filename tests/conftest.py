import pytest

from src.core.app import App
from src.core.command import Command
from src.core.context import Context
from src.core.exceptions import AppError
from src.core.result import Result


class EchoAppContext(Context):
    debug: bool = False
    lowercase: bool = False
    message: str = ""
    uppercase: bool = False


class InvertCommand(Command):
    name = "invert"
    description = "Invert Command"

    flags = [
        (
            ["message"],
            {"help": "The message to be inverted"},
        ),
    ]

    def run(self, context: EchoAppContext) -> Result:
        result = Result()
        message = context.message

        if not message:
            raise AppError("No message has been provided.")

        if context.lowercase:
            message = message.lower()

        if context.uppercase:
            message = message.upper()

        result.output = message[::-1]
        return result


class RepeatCommand(Command):
    name = "repeat"
    description = "Repeat Command"

    flags = [
        (
            ["message"],
            {"help": "The message to be repeated"},
        ),
    ]

    def run(self, context: EchoAppContext) -> Result:
        result = Result()
        message = context.message

        if not message:
            raise AppError("No message has been provided.")

        if context.lowercase:
            message = message.lower()

        if context.uppercase:
            message = message.upper()

        result.output = message
        return result


class SayCommand(Command):
    name = "say"
    description = "Say Command"

    flags = [
        (
            ["-l", "--lowercase"],
            {
                "action": "store_true",
                "default": False,
                "help": "Transform the message to lower case",
            },
        ),
        (
            ["-u", "--uppercase"],
            {
                "action": "store_true",
                "default": False,
                "help": "Transform the message to upper case",
            },
        ),
    ]

    subcommands = [
        InvertCommand,
        RepeatCommand,
    ]


class EchoApp(App):
    name = "echo"
    description = "Echo application"
    config_path = "echo.toml"

    flags = [
        (
            ["-d", "--debug"],
            {
                "action": "store_true",
                "default": False,
                "help": "Run in debug mode",
            },
        ),
    ]

    subcommands = [
        SayCommand,
    ]


@pytest.fixture
def app() -> EchoApp:
    app = EchoApp()
    return app

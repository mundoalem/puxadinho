from teeny.app import App
from teeny.command import Command
from teeny.context import Context
from teeny.result import Result


class EchoAppContext(Context):
    shout: bool = False
    message: str = "Hello, World!"


class EchoCommand(Command):
    name = "echo"

    flags = [
        (
            ["message"],
            {
                "help": "Message to be echoed",
            },
        ),
    ]

    def run(self, context: EchoAppContext) -> Result:
        result = Result()
        result.output = (
            context.message if not context.shout else context.message.upper()
        )

        return result


class EchoApp(App):
    name = "echo"

    flags = [
        (
            ["-s", "--shout"],
            {
                "action": "store_true",
                "default": False,
                "help": "Param App",
            },
        ),
    ]

    subcommands = [
        EchoCommand,
    ]

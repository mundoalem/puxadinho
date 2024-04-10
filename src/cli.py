from .core.app import App
from .core.command import Command
from .core.context import Context
from .core.result import Result


class CloudSelectAppContext(Context):
    debug: bool
    uppercase: bool


class S3Command(Command):
    name = "s3"
    description = "AWS S3 Command"

    flags = [
        (
            ["-u", "--uppercase"],
            {
                "action": "store_true",
                "default": False,
                "help": "Capitalise",
            },
        ),
    ]

    def run(self, context: CloudSelectAppContext) -> Result:
        result = Result()
        result.output = (
            self.description if not context.uppercase else self.description.upper()
        )
        return result


class AwsCommand(Command):
    name = "aws"
    description = "AWS Command"

    subcommands = [
        S3Command,
    ]

    def run(self, context: CloudSelectAppContext) -> Result:
        result = Result()
        result.output = self.description + (" debug" if context.debug else "")
        return result


class AzureCommand(Command):
    name = "azure"
    description = "Azure Command"

    def run(self, context: CloudSelectAppContext) -> Result:
        result = Result()
        result.output = self.description + (" debug" if context.debug else "")
        return result


class CloudSelectApp(App):
    name = "cloudselect"
    description = "Cloud select application"

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
        AwsCommand,
        AzureCommand,
    ]


def run() -> None:
    app = CloudSelectApp()
    app.setup()
    app.run()

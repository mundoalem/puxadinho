import argparse

from .command import Command
from .context import Context
from .exceptions import NotFoundError
from .result import Result
from .types import Flag
from .view import View


class App(Command):
    name: str
    description: str
    flags: list[Flag]
    subcommands: list[type[Command]]

    def __init__(self) -> None:
        if not getattr(self, "name", None):
            raise NotFoundError("Application name was not found")

        if not getattr(self, "description", None):
            raise NotFoundError("Application description was not found")

        if not getattr(self, "flags", None):
            self.flags = []

        if not getattr(self, "subcommands", None):
            self.subcommands = []

        self.args = None
        self.children = []
        self.parser = argparse.ArgumentParser(
            prog=self.name,
            description=self.description,
        )

        self.subparser = self.parser.add_subparsers()
        self.parser.set_defaults(runfunc=self._default)

    def _default(self, _: Context) -> Result:
        return Result()

    def run(self) -> None:
        args = vars(self.parser.parse_args())
        runfunc = args["runfunc"]

        del args["runfunc"]

        context = Context.from_dict(variables=args)
        result = runfunc(context)

        View.as_text(result)
        exit(result.exit_code)

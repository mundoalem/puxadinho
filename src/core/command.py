from __future__ import annotations

from .context import Context
from .exceptions import NotFoundError
from .result import Result
from .types import Flag, Subparser


class Command:
    name: str
    description: str
    flags: list[Flag]
    subcommands: list[type[Command]]

    def __init__(self, parent: Command) -> None:
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
        self.parent = None
        self.parser = parent.subparser.add_parser(
            name=self.name,
            description=self.description,
        )

        self.subparser = self.parser.add_subparsers()
        self.parser.set_defaults(runfunc=self.run)

    @property
    def children(self) -> list[Command]:
        return self._children

    @children.setter
    def children(self, value: list[Command]) -> None:
        self._children = value

    @property
    def parent(self) -> Command:
        return self._parent

    @parent.setter
    def parent(self, value: Command) -> None:
        self._parent = value

    @property
    def parser(self) -> Subparser:
        return self._parser

    @parser.setter
    def parser(self, value: Subparser) -> None:
        self._parser = value

    @property
    def subparser(self) -> Subparser:
        return self._subparser

    @subparser.setter
    def subparser(self, value: Subparser) -> None:
        self._subparser = value

    def run(self, context: Context) -> Result:
        return Result()

    def setup(self) -> None:
        for flag in self.flags:
            self.parser.add_argument(*flag[0], **flag[1])

        for cls in self.subcommands:
            subcommand = cls(parent=self)
            subcommand.setup()
            self.children.append(subcommand)

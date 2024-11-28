import sys
import traceback

from .result import Result


class View:
    @staticmethod
    def as_text(result: Result) -> None:
        if result.output:
            print(result.output, file=sys.stdout)

        if result.error:
            traceback.print_exception(result.error, file=sys.stderr)

from __future__ import annotations

from copy import deepcopy
from typing import Any


class Context:
    @classmethod
    def from_dict(cls, variables: dict[str, Any], context: Context = None) -> Context:
        context = cls() if not context else deepcopy(context)

        for key, value in variables.items():
            match value:
                case bool() | int() | float() | str() | list():
                    setattr(context, key, value)
                case dict():
                    subcontext = Context()

                    Context.from_dict(variables=value, context=subcontext)
                    setattr(context, key, subcontext)
                case _:
                    continue

        return context


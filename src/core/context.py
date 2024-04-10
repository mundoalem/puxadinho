from __future__ import annotations

from typing import Any


class Context:
    @staticmethod
    def from_dict(variables: dict[str, Any]) -> Context:
        context = Context()

        for name, value in variables.items():
            setattr(context, name, value)

        return context

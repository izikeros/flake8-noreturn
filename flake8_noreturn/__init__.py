from __future__ import annotations

import ast
from collections.abc import Generator
from importlib.metadata import version
from typing import Any
from typing import NoReturn


class NoReturnChecker:
    """
    A flake8 plugin to check return None (-> None:).
    """

    name = "flake8-return"
    version = version("flake8-noreturn")

    def __init__(self, tree: ast.AST) -> NoReturn:
        self.tree = tree

    message_NR001 = "NR001 Using -> None."

    def run(self) -> Generator[tuple[int, int, str, type[Any]], None, None]:
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef) and node.returns is not None:
                # check if node has attribute id
                if not hasattr(node.returns, "id"):
                    if hasattr(node.returns, "value"):
                        if not hasattr(node.returns.value, "id"):
                            yield (
                                node.lineno,
                                node.col_offset,
                                self.message_NR001,
                                type(self),
                            )

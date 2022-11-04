from __future__ import annotations

import re
import sys
from textwrap import dedent

import pytest

if sys.version_info >= (3, 8):
    from importlib.metadata import version
else:
    from importlib_metadata import version

message_NR001 = "NR001 Using -> None."


@pytest.mark.skip(reason="Version not implemented yet")
def test_version(flake8_path):
    result = flake8_path.run_flake8(["--version"])
    version_regex = r"flake8-noreturn:( )*" + version("flake8-noreturn")
    unwrapped = "".join(result.out_lines)
    assert re.search(version_regex, unwrapped)


def test_NR001_pass_variable_declaration_None(flake8_path):
    (flake8_path / "example.py").write_text("foo: None = None\n")
    result = flake8_path.run_flake8()
    assert result.out_lines == []


def test_NR001_pass_variable_declaration_int(flake8_path):
    (flake8_path / "example.py").write_text("foo: int = 1\n")
    result = flake8_path.run_flake8()
    assert result.out_lines == []


def test_NR001_pass_function(flake8_path):
    (flake8_path / "example.py").write_text(
        dedent(
            """\
            def foo():
                pass
            """
        )
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == []


def test_NR001_pass_class_variable_declaration(flake8_path):
    (flake8_path / "example.py").write_text(
        dedent(
            """\
            class Foo:
                bar: int
            """
        )
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == []


def test_NR001_pass_function_keyword_arguments(flake8_path):
    (flake8_path / "example.py").write_text(
        dedent(
            """\
            def foo(x: None = 1):
                return x
            """
        )
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == []


def test_NR001_pass_function_return_no_annotation(flake8_path):
    (flake8_path / "example.py").write_text(
        dedent(
            """\
            def foo():
                return 2
            """
        )
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == []


def test_NR001_pass_function_return_with_annotation(flake8_path):
    (flake8_path / "example.py").write_text(
        dedent(
            """\
            def foo() -> int:
                return 2
            """
        )
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == []


def test_NR001_pass_function_return_tuple(flake8_path):
    (flake8_path / "example.py").write_text(
        dedent(
            """\
            def foo() -> tuple[int, None]:
                return 2, None
            """
        )
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == []


def test_NR001_pass_function_return_union(flake8_path):
    (flake8_path / "example.py").write_text(
        dedent(
            """\
            from typing import Union


            def foo() -> Union[int, None]:
                return 2, None
            """
        )
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == []


def test_NR001_fail_function_return_None_annotation(flake8_path):
    (flake8_path / "example.py").write_text(
        dedent(
            """\
            def foo() -> None:
                pass
            """
        )
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == [f"./example.py:1:1: {message_NR001}"]


def test_NR001_pass_function_return_None_annotation(flake8_path):
    (flake8_path / "example.py").write_text(
        dedent(
            """\
            from typing import NoReturn


            def foo() -> NoReturn:
                pass
            """
        )
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == []


def test_NR001_fail_method_return_None_annotation(flake8_path):
    (flake8_path / "example.py").write_text(
        dedent(
            """\
            class Foo:
                def bar(self) -> None:
                    pass
            """
        )
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == [f"./example.py:2:5: {message_NR001}"]


def test_NR001_pass_method_return_NoReturn_annotation(flake8_path):
    (flake8_path / "example.py").write_text(
        dedent(
            """\
            from typing import NoReturn


            class Foo:
                def bar(self) -> NoReturn:
                    pass
            """
        )
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == []

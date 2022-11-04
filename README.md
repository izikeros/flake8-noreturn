# flake8-noreturn
![](https://img.shields.io/pypi/v/flake8-noreturn.svg)
![](https://img.shields.io/pypi/pyversions/flake8-noreturn.svg)
![](https://img.shields.io/pypi/l/flake8-noreturn.svg)
![](https://img.shields.io/pypi/dm/flake8-noreturn.svg)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/izikeros/flake8-noreturn/main.svg)](https://results.pre-commit.ci/latest/github/izikeros/trend_classifier/main)
[![Maintainability](https://api.codeclimate.com/v1/badges/081a20bb8a5201cd8faf/maintainability)](https://codeclimate.com/github/izikeros/flake8-noreturn/maintainability)

Flake8 plugin to check for using `-> None:` type hint for return type. Helps to replace them with `-> NoRetun` type hint from typing.

**Why to use `NoReturn` type hint?**

Using `NoReturn` type hint:
- is more explicit and helps to avoid confusion with `None` value,
- helps to avoid bugs when using `None` as a default value for function arguments.
- helps mypy to detect unreachable code
-
## Installation
Use pip to install the package:
```sh
$ pip3 install flake8-noreturn
```

## Usage

```sh
$ flake8 .
```

to select only `flake8-noreturn` errors:

```sh
$ flake8 --select NR .
```

## Rules
Currently, the plugin checks implements only one rule:

`NR001 Using -> None.`
Indicates usage of `-> None:` type hint for return type.

Examples:
```python
def foo() -> None:
    pass
```
will raise NR001.

```python
from typing import NoReturn

def foo() -> NoReturn:
    pass
```
will not raise NR001.

```python
def foo() -> tuple[int, None]:
    return 2, None
```
will not raise NR001.

## Related Projects

There is a [flake8-no-types](https://github.com/adamchainz/flake8-no-types) which was a heavy inspiration for this project.

## Credits

Thank you [adamchainz](https://github.com/adamchainz) for the inspiring [article](https://adamj.eu/tech/2021/05/20/python-type-hints-whats-the-point-of-noreturn/) and the [flake8-no-types](https://github.com/adamchainz/flake8-no-types) which helped me to create this plugin.

## License

[MIT](https://izikeros.mit-license.org/) © [Krystian Safjan](https://safjan.com).

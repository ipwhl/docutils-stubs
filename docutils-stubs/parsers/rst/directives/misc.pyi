# Stubs for docutils.parsers.rst.directives.misc (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils.nodes import Node
from docutils.parsers.rst import Directive
from typing import Any, Callable, Dict, List, Pattern, Tuple

__docformat__: str

class Include(Directive):
    required_arguments: int = ...
    optional_arguments: int = ...
    final_argument_whitespace: bool = ...
    option_spec: Dict[str, Callable[[str], Any]] = ...
    standard_include_path: str = ...
    def run(self) -> List[Node]: ...

class Raw(Directive):
    required_arguments: int = ...
    optional_arguments: int = ...
    final_argument_whitespace: bool = ...
    option_spec: Dict[str, Callable[[str], Any]] = ...
    has_content: bool = ...
    def run(self) -> List[Node]: ...

class Replace(Directive):
    has_content: bool = ...
    def run(self) -> List[Node]: ...

class Unicode(Directive):
    required_arguments: int = ...
    optional_arguments: int = ...
    final_argument_whitespace: bool = ...
    option_spec: Dict[str, Callable[[str], Any]] = ...
    comment_pattern: Pattern = ...
    def run(self) -> List[Node]: ...

class Class(Directive):
    required_arguments: int = ...
    optional_arguments: int = ...
    final_argument_whitespace: bool = ...
    has_content: bool = ...
    def run(self) -> List[Node]: ...

class Role(Directive):
    has_content: bool = ...
    argument_pattern: Pattern = ...
    def run(self) -> List[Node]: ...

class DefaultRole(Directive):
    optional_arguments: int = ...
    final_argument_whitespace: bool = ...
    def run(self) -> List[Node]: ...

class Title(Directive):
    required_arguments: int = ...
    optional_arguments: int = ...
    final_argument_whitespace: bool = ...
    def run(self) -> List[Node]: ...

class Date(Directive):
    has_content: bool = ...
    def run(self) -> List[Node]: ...

class TestDirective(Directive):
    optional_arguments: int = ...
    final_argument_whitespace: bool = ...
    option_spec: Dict[str, Callable[[str], Any]] = ...
    has_content: bool = ...
    def run(self) -> List[Node]: ...
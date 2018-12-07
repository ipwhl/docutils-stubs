# Stubs for docutils.parsers.rst.directives.tables (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import csv
from docutils.statemachine import StringList
from docutils.nodes import Node, system_message, table, title
from docutils.parsers.rst import Directive
from typing import Any, Callable, Dict, List, Tuple, TypeVar

N_co = TypeVar('N_co', bound=Node, covariant=True)

__docformat__: str

def align(argument: str) -> str: ...

class Table(Directive):
    optional_arguments: int = ...
    final_argument_whitespace: bool = ...
    option_spec: Dict[str, Callable[[str], Any]] = ...
    has_content: bool = ...
    def make_title(self) -> Tuple[title, List[system_message]]: ...
    def process_header_option(self) -> Tuple[List[Node], int]: ...
    def check_table_dimensions(self, rows: List[List[N_co]], header_rows: int, stub_columns: int) -> None: ...
    @property
    def widths(self) -> str: ...
    def get_column_widths(self, max_cols: int) -> List[int]: ...
    def extend_short_rows_with_empty_cells(self, columns: int, parts: Tuple[List[N_co], List[N_co]]) -> None: ...

class RSTTable(Table):
    def run(self) -> List[Node]: ...

class CSVTable(Table):
    option_spec: Dict[str, Callable[[str], Any]] = ...
    class DocutilsDialect(csv.Dialect):
        delimiter: str = ...
        quotechar: str = ...
        doublequote: bool = ...
        skipinitialspace: bool = ...
        strict: bool = ...
        lineterminator: str = ...
        quoting: Any = ...
        escapechar: str = ...
        def __init__(self, options: Dict[str, Any]) -> None: ...
    class HeaderDialect(csv.Dialect):
        delimiter: str = ...
        quotechar: str = ...
        escapechar: str = ...
        doublequote: bool = ...
        skipinitialspace: bool = ...
        strict: bool = ...
        lineterminator: str = ...
        quoting: Any = ...
    def check_requirements(self) -> None: ...
    def run(self) -> List[Node]: ...
    def get_csv_data(self) -> Tuple[List[str], str]: ...
    decode_from_csv: Callable[[str], str] = ...
    encode_for_csv: Callable[[str], str] = ...
    def parse_csv_data_into_rows(self, csv_data: List[str], dialect: Any, source: str) -> Tuple[List[Tuple[int, int, int, StringList]], int]: ...

class ListTable(Table):
    option_spec: Dict[str, Callable[[str], Any]] = ...
    def run(self) -> List[Node]: ...
    def check_list_content(self, node: Node) -> Tuple[int, List[int]]: ...
    def build_table_from_list(self, table_data: List[List[N_co]], col_widths: List[int], header_rows: int, stub_columns: int) -> table: ...

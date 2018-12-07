# Stubs for docutils.core (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Dict, List, Optional, Tuple, Type
from docutils import SettingsSpec
from docutils import nodes
from docutils.frontend import OptionParser, Values
from docutils.io import Input, Output
from docutils.parsers import Parser
from docutils.readers import Reader
from docutils.writers import Writer

__docformat__: str

class Publisher:
    document: nodes.document = ...
    reader: Optional[Reader] = ...
    parser: Optional[Parser] = ...
    writer: Optional[Writer] = ...
    source: Optional[Input] = ...
    source_class: Type[Input] = ...
    destination: Optional[Output] = ...
    destination_class: Type[Output] = ...
    settings: Values = ...
    def __init__(self, reader: Optional[Reader] = ..., parser: Optional[Parser] = ..., writer: Optional[Writer] = ..., source: Optional[Input] = ..., source_class: Type[Input] = ..., destination: Optional[Output] = ..., destination_class: Type[Output] = ..., settings: Optional[Values] = ...) -> None: ...
    def set_reader(self, reader_name: str, parser: Parser, parser_name: str) -> None: ...
    def set_writer(self, writer_name: str) -> None: ...
    def set_components(self, reader_name: str, parser_name: str, writer_name: str) -> None: ...
    def setup_option_parser(self, usage: Optional[Any] = ..., description: Optional[Any] = ..., settings_spec: Optional[SettingsSpec] = ..., config_section: Optional[str] = ..., **defaults) -> OptionParser: ...
    def get_settings(self, usage: Optional[Any] = ..., description: Optional[Any] = ..., settings_spec: Optional[SettingsSpec] = ..., config_section: Optional[str] = ..., **defaults) -> Values: ...
    def process_programmatic_settings(self, settings_spec: SettingsSpec, settings_overrides, config_section: str) -> None: ...
    def process_command_line(self, argv: Optional[List[str]] = ..., usage: Optional[Any] = ..., description: Optional[Any] = ..., settings_spec: Optional[SettingsSpec] = ..., config_section: Optional[str] = ..., **defaults) -> None: ...
    def set_io(self, source_path: Optional[str] = ..., destination_path: Optional[str] = ...) -> None: ...
    def set_source(self, source: Optional[Any] = ..., source_path: Optional[str] = ...) -> None: ...
    def set_destination(self, destination: Optional[Any] = ..., destination_path: Optional[str] = ...) -> None: ...
    def apply_transforms(self) -> None: ...
    def publish(self, argv: Optional[List[str]] = ..., usage: Optional[Any] = ..., description: Optional[Any] = ..., settings_spec: Optional[SettingsSpec] = ..., settings_overrides: Optional[Any] = ..., config_section: Optional[str] = ..., enable_exit_status: bool = ...) -> Any: ...
    def debugging_dumps(self) -> None: ...
    def report_Exception(self, error: Exception) -> None: ...
    def report_SystemMessage(self, error: Exception) -> None: ...
    def report_UnicodeError(self, error: Exception) -> None: ...

default_usage: str
default_description: str

def publish_cmdline(reader: Optional[Reader] = ..., reader_name: str = ..., parser: Optional[Parser] = ..., parser_name: str = ..., writer: Optional[Writer] = ..., writer_name: str = ..., settings: Optional[Values] = ..., settings_spec: Optional[SettingsSpec] = ..., settings_overrides: Optional[Any] = ..., config_section: Optional[str] = ..., enable_exit_status: bool = ..., argv: Optional[List[str]] = ..., usage: Any = ..., description: Any = ...) -> Any: ...
def publish_file(source: Optional[Input] = ..., source_path: Optional[str] = ..., destination: Optional[Output] = ..., destination_path: Optional[str] = ..., reader: Optional[Reader] = ..., reader_name: str = ..., parser: Optional[Parser] = ..., parser_name: str = ..., writer: Optional[Writer] = ..., writer_name: str = ..., settings: Optional[Values] = ..., settings_spec: Optional[SettingsSpec] = ..., settings_overrides: Optional[Any] = ..., config_section: Optional[str] = ..., enable_exit_status: bool = ...) -> Any: ...
def publish_string(source: str, source_path: Optional[str] = ..., destination_path: Optional[str] = ..., reader: Optional[Reader] = ..., reader_name: str = ..., parser: Optional[Parser] = ..., parser_name: str = ..., writer: Optional[Writer] = ..., writer_name: str = ..., settings: Optional[Values] = ..., settings_spec: Optional[SettingsSpec] = ..., settings_overrides: Optional[Any] = ..., config_section: Optional[str] = ..., enable_exit_status: bool = ...) -> Any: ...
def publish_parts(source: Input, source_path: Optional[str] = ..., source_class: Type[Input] = ..., destination_path: Optional[str] = ..., reader: Optional[Reader] = ..., reader_name: str = ..., parser: Optional[Parser] = ..., parser_name: str = ..., writer: Optional[Writer] = ..., writer_name: str = ..., settings: Optional[Values] = ..., settings_spec: Optional[SettingsSpec] = ..., settings_overrides: Optional[Any] = ..., config_section: Optional[str] = ..., enable_exit_status: bool = ...) -> Dict[str, Any]: ...
def publish_doctree(source: str, source_path: Optional[str] = ..., source_class: Type[Input] = ..., reader: Optional[Reader] = ..., reader_name: str = ..., parser: Optional[Parser] = ..., parser_name: str = ..., settings: Optional[Values] = ..., settings_spec: Optional[SettingsSpec] = ..., settings_overrides: Optional[Any] = ..., config_section: Optional[str] = ..., enable_exit_status: bool = ...) -> nodes.document: ...
def publish_from_doctree(document: nodes.document, destination_path: Optional[str] = ..., writer: Optional[Writer] = ..., writer_name: str = ..., settings: Optional[Values] = ..., settings_spec: Optional[SettingsSpec] = ..., settings_overrides: Optional[Any] = ..., config_section: Optional[str] = ..., enable_exit_status: bool = ...) -> Any: ...
def publish_cmdline_to_binary(reader: Optional[Reader] = ..., reader_name: str = ..., parser: Optional[Parser] = ..., parser_name: str = ..., writer: Optional[Writer] = ..., writer_name: str = ..., settings: Optional[Values] = ..., settings_spec: Optional[SettingsSpec] = ..., settings_overrides: Optional[Any] = ..., config_section: Optional[str] = ..., enable_exit_status: bool = ..., argv: Optional[Any] = ..., usage: Any = ..., description: Any = ..., destination: Optional[Any] = ..., destination_class: Any = ...) -> Any: ...
def publish_programmatically(source_class: Type[Input], source: Any, source_path: str, destination_class: Type[Output], destination: Any, destination_path: str, reader: Reader, reader_name: str, parser: Parser, parser_name: str, writer: Writer, writer_name: str, settings: Values, settings_spec: SettingsSpec, settings_overrides: Any, config_section: str, enable_exit_status: bool) -> Tuple[Any, Publisher]: ...

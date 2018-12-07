# Stubs for docutils.parsers.rst.states (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils import ApplicationError, DataError
from docutils import nodes
from docutils.parsers.rst import Directive, states, tableparser
from docutils.statemachine import StateMachine, StateMachineWS, StateWS, StringList
from docutils.utils import Reporter
from types import ModuleType
from typing import Any, Callable, Dict, List, Match, MutableSequence, Optional, Pattern, Sequence, Tuple, Type, Union

BasicDefinition = Tuple[str, str, str, List[Pattern]]
DefinitionParts = Tuple[str, str, str, List[Union[Pattern, BasicDefinition]]]
DefinitionType = Tuple[str, str, str, List[Union[Pattern, DefinitionParts]]]

__docformat__: str

class MarkupError(DataError): ...
class UnknownInterpretedRoleError(DataError): ...
class InterpretedRoleNotImplementedError(DataError): ...
class ParserError(ApplicationError): ...
class MarkupMismatch(Exception): ...

class Struct:
    def __init__(self, **keywordargs) -> None: ...

class RSTStateMachine(StateMachineWS):
    language: ModuleType = ...
    match_titles: bool = ...
    memo: Struct = ...
    document: nodes.document = ...
    reporter: Reporter = ...
    node: nodes.Node = ...
    def run(self, input_lines: Union[List[str], StringList], document: nodes.document, input_offset: int = ..., match_titles: bool = ..., inliner: Optional[states.Inliner] = ...) -> None: ...  # type: ignore

class NestedStateMachine(StateMachineWS):
    match_titles: bool = ...
    memo: Struct = ...
    document: nodes.document = ...
    reporter: Reporter = ...
    language: ModuleType = ...
    node: nodes.Node = ...
    def run(self, input_lines: Union[List[str], StringList], input_offset: int, memo: Struct, node: nodes.Node, match_titles: bool = ...) -> List[Any]: ...    # type: ignore

class RSTState(StateWS):
    nested_sm: Type[StateMachine] = ...
    nested_sm_cache: List[StateMachine] = ...
    nested_sm_kwargs: Dict[str, Any] = ...
    def __init__(self, state_machine: StateMachine, debug: bool = ...) -> None: ...
    memo: Struct = ...
    reporter: Reporter = ...
    inliner: states.Inliner = ...
    document: nodes.document = ...
    parent: nodes.Node = ...
    def runtime_init(self) -> None: ...
    def goto_line(self, abs_line_offset: int) -> None: ...
    def no_match(self, context, transitions: Tuple[List[str], Dict[str, Tuple[Pattern, Callable, str]]]) -> Tuple[Any, str, List]: ...
    def bof(self, context) -> Tuple[List, List]: ...
    def nested_parse(self, block: StringList, input_offset: int, node: nodes.Node, match_titles: bool = ..., state_machine_class: Optional[Type[StateMachine]] = ..., state_machine_kwargs: Optional[Dict[str, Any]] = ...) -> int: ...
    def nested_list_parse(self, block, input_offset, node, initial_state, blank_finish, blank_finish_state: Optional[Any] = ..., extra_settings: Any = ..., match_titles: bool = ..., state_machine_class: Optional[Any] = ..., state_machine_kwargs: Optional[Any] = ...) -> Tuple[int, bool]: ...
    def section(self, title: str, source: str, style: str, lineno: int, messages: List[str]) -> None: ...
    def check_subsection(self, source: str, style: str, lineno: int) -> int: ...
    def title_inconsistent(self, sourcetext: str, lineno: int) -> nodes.system_message: ...
    def new_subsection(self, title: str, lineno: int, messages: List[nodes.system_message]) -> None: ...
    def paragraph(self, lines: List[str], lineno: int) -> Tuple[List[nodes.Node], int]: ...
    def inline_text(self, text: str, lineno: int) -> Tuple[List[nodes.Node], List[nodes.system_message]]: ...
    def unindent_warning(self, node_name: str) -> nodes.system_message: ...

def build_regexp(definition: DefinitionType, compile: bool = ...) -> Pattern: ...

class Inliner:
    implicit_dispatch: List[Tuple[Pattern, Callable]] = ...
    def __init__(self) -> None: ...
    start_string_prefix: str = ...
    end_string_suffix: str = ...
    parts: DefinitionType = ...
    patterns: Any = ...
    def init_customizations(self, settings: Any) -> None: ...
    reporter: Reporter = ...
    document: nodes.document = ...
    language: ModuleType = ...
    parent: nodes.Element = ...
    def parse(self, text: str, lineno: int, memo: Any, parent: nodes.Element) -> Tuple[List[nodes.Node], List[nodes.system_message]]: ...
    non_whitespace_before: str = ...
    non_whitespace_escape_before: str = ...
    non_unescaped_whitespace_escape_before: str = ...
    non_whitespace_after: str = ...
    simplename: str = ...
    uric: str = ...
    uri_end_delim: str = ...
    urilast: str = ...
    uri_end: str = ...
    emailc: str = ...
    email_pattern: str = ...
    def quoted_start(self, match: Match) -> bool: ...
    def inline_obj(self, match: Match, lineno: int, end_pattern: Pattern, nodeclass: nodes.TextElement, restore_backslashes: bool = ...) -> Tuple[str, List[nodes.problematic], str, List[nodes.system_message], str]: ...
    def problematic(self, text: str, rawsource: str, message: nodes.system_message) -> nodes.problematic: ...
    def emphasis(self, match: Match, lineno: int) -> Tuple[str, List[nodes.problematic], str, List[nodes.system_message]]: ...
    def strong(self, match: Match, lineno: int) -> Tuple[str, List[nodes.problematic], str, List[nodes.system_message]]: ...
    def interpreted_or_phrase_ref(self, match: Match, lineno: int) -> Tuple[str, List[nodes.problematic], str, List[nodes.system_message]]: ...
    def phrase_ref(self, before: str, after: str, rawsource: str, escaped: str, text: str) -> Tuple[str, List[nodes.Node], str, List[nodes.Node]]: ...
    def adjust_uri(self, uri: str) -> str: ...
    def interpreted(self, rawsource: str, text: str, role: str, lineno: int) -> Tuple[List[nodes.Node], List[nodes.system_message]]: ...
    def literal(self, match: Match, lineno: int) -> Tuple[str, List[nodes.problematic], str, List[nodes.system_message]]: ...
    def inline_internal_target(self, match: Match, lineno: int) -> Tuple[str, List[nodes.problematic], str, List[nodes.system_message]]: ...
    def substitution_reference(self, match: Match, lineno: int) -> Tuple[str, List[nodes.problematic], str, List[nodes.system_message]]: ...
    def footnote_reference(self, match: Match, lineno: int) -> Tuple[str, List[nodes.problematic], str, List[nodes.system_message]]: ...
    def reference(self, match: Match, lineno: int, anonymous: bool = ...) -> Tuple[str, List[nodes.problematic], str, List[nodes.system_message]]: ...
    def anonymous_reference(self, match: Match, lineno: int) -> Tuple[str, List[nodes.problematic], str, List[nodes.system_message]]: ...
    def standalone_uri(self, match: Match, lineno: int) -> List[Tuple[str, List[nodes.problematic], str, List[nodes.system_message]]]: ...
    def pep_reference(self, match: Match, lineno: int) -> List[Tuple[str, List[nodes.problematic], str, List[nodes.system_message]]]: ...
    rfc_url: str = ...
    def rfc_reference(self, match: Match, lineno: int) -> List[Tuple[str, List[nodes.problematic], str, List[nodes.system_message]]]: ...
    def implicit_inline(self, text: str, lineno: int) -> List[nodes.Text]: ...
    dispatch: Dict[str, Callable[[Match, int], Tuple[str, List[nodes.problematic], str, List[nodes.system_message]]]] = ...

class Body(RSTState):
    double_width_pad_char: str = ...
    enum: Any = ...
    grid_table_top_pat: Pattern = ...
    simple_table_top_pat: Pattern = ...
    simple_table_border_pat: Pattern = ...
    pats: Dict[str, str] = ...
    patterns: Dict[str, Union[str, Pattern]] = ...
    initial_transitions: Union[Sequence[str], Sequence[Tuple[str, str]]] = ...
    def indent(self, match: Match, context: Any, next_state: str) -> Tuple[Any, str, List[Any]]: ...
    def block_quote(self, indented: StringList, line_offset: int) -> List[nodes.Element]: ...
    attribution_pattern: Pattern = ...
    def split_attribution(self, indented: StringList, line_offset: int) -> Tuple[StringList, Optional[StringList], Optional[int], Optional[StringList], Optional[int]]: ...
    def check_attribution(self, indented: StringList, attribution_start: int) -> Tuple[Optional[int], Optional[int]]: ...
    def parse_attribution(self, indented: StringList, line_offset: int) -> Tuple[nodes.attribution, List[nodes.system_message]]: ...
    def bullet(self, match: Match, context: Any, next_state: str) -> Optional[Tuple[List[Any], str, List[Any]]]: ...
    def list_item(self, indent: int) -> Tuple[nodes.list_item, bool]: ...
    def enumerator(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...
    def parse_enumerator(self, match: Match, expected_sequence: Optional[Any] = ...) -> Tuple[str, str, str, Optional[str]]: ...
    def is_enumerated_list_item(self, ordinal: Optional[int], sequence: str, format: str) -> Optional[int]: ...
    def make_enumerator(self, ordinal: int, sequence: str, format: str) -> Optional[Tuple[str, str]]: ...
    def field_marker(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...
    def field(self, match: Match) -> Tuple[nodes.field, bool]: ...
    def parse_field_marker(self, match: Match) -> str: ...
    def parse_field_body(self, indented: StringList, offset, node) -> None: ...
    def option_marker(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...
    def option_list_item(self, match: Match) -> Tuple[nodes.option_list_item, bool]: ...
    def parse_option_marker(self, match: Match) -> List[Union[nodes.option, nodes.option_argument]]: ...
    def doctest(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...
    def line_block(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...
    def line_block_line(self, match: Match, lineno: int) -> Tuple[nodes.line, List[nodes.system_message], bool]: ...
    def nest_line_block_lines(self, block: nodes.line_block) -> None: ...
    def nest_line_block_segment(self, block: nodes.line_block) -> None: ...
    def grid_table_top(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...
    def simple_table_top(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...
    def table_top(self, match: Match, context: Any, next_state: str, isolate_function: Callable[[], Union[Tuple[List[Any], List[nodes.system_message], bool], Tuple[StringList, List[nodes.system_message], bool]]], parser_class: Union[Type[tableparser.GridTableParser], Type[tableparser.SimpleTableParser]]) -> Tuple[List[Any], str, List[Any]]: ...
    def table(self, isolate_function: Callable[[], Tuple[Union[List[Any], StringList], List[nodes.system_message], bool]], parser_class: Union[Type[tableparser.GridTableParser], Type[tableparser.SimpleTableParser]]) -> Tuple[List[nodes.Node], bool]: ...
    def isolate_grid_table(self) -> Union[Tuple[List[Any], List[nodes.system_message], bool], Tuple[StringList, List[nodes.system_message], bool]]: ...
    def isolate_simple_table(self) -> Union[Tuple[List[Any], List[nodes.system_message], bool], Tuple[StringList, List[nodes.system_message], bool]]: ...
    def malformed_table(self, block: StringList, detail: str = ..., offset: int = ...) -> List[nodes.system_message]: ...
    def build_table(self, tabledata: Tuple[List[int], List[List[Tuple[int, int, int, StringList]]], List[List[Tuple[int, int, int, StringList]]]], tableline: int, stub_columns: int = ..., widths: Union[None, str, List[int]] = ...) -> nodes.table: ...
    def build_table_row(self, rowdata: List[Tuple[int, int, int, StringList]], tableline: int) -> nodes.row: ...
    explicit: states.Struct = ...
    def footnote(self, match: Match) -> Tuple[List[nodes.footnote], bool]: ...
    def citation(self, match: Match) -> Tuple[List[nodes.citation], bool]: ...
    def hyperlink_target(self, match: Match) -> Union[Tuple[List[nodes.target], bool], Tuple[List[str], bool]]: ...
    def make_target(self, block: List[str], block_text: str, lineno: int, target_name: str) -> Union[nodes.target, str]: ...
    def parse_target(self, block: List[str], block_text: str, lineno: int) -> Tuple[str, str]: ...
    def is_reference(self, reference: str) -> Optional[str]: ...
    def add_target(self, targetname: str, refuri: Optional[str], target: nodes.target, lineno: int) -> None: ...
    def substitution_def(self, match: Match) -> Union[Tuple[List[nodes.system_message], bool], Tuple[List[nodes.substitution_definition], bool]]: ...
    def disallowed_inside_substitution_definitions(self, node: nodes.Node) -> int: ...
    def directive(self, match: Match, **option_presets: Any) -> Union[Tuple[List[nodes.system_message], bool], Tuple[List[nodes.literal_block], bool], Tuple[List[nodes.system_message], bool]]: ...
    def run_directive(self, directive: Type[Directive], match: Match, type_name: str, option_presets: Dict[str, Any]) -> Union[Tuple[List[nodes.system_message], bool], Tuple[List[nodes.literal_block], bool]]: ...
    def parse_directive_block(self, indented: StringList, line_offset: int, directive: Directive, option_presets: Dict[str, Any]) -> Tuple[List[str], Dict[str, Any], StringList, int]: ...
    def parse_directive_options(self, option_presets: Dict[str, Any], option_spec: Dict[str, Callable[[str], str]], arg_block: Union[StringList, List[Any]]) -> Tuple[Dict[str, Any], StringList]: ...
    def parse_directive_arguments(self, directive: Directive, arg_block: Union[StringList, List[Any]]) -> List[str]: ...
    def parse_extension_options(self, option_spec: Dict[str, Callable[[str], str]], datalines: Union[StringList, List[Any]]) -> Tuple[int, Union[str, Dict[str, Any]]]: ...
    def unknown_directive(self, type_name: str) -> Tuple[List[nodes.system_message], bool]: ...
    def comment(self, match: Match) -> Tuple[List[nodes.comment], bool]: ...
    def explicit_markup(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...
    def explicit_construct(self, match: Match) -> Union[Tuple[List[nodes.footnote], bool], Tuple[List[nodes.citation], bool], Tuple[List[nodes.target], bool], Tuple[List[str], bool], Tuple[List[nodes.system_message], bool], Tuple[List[nodes.substitution_definition], bool], Tuple[List[nodes.literal_block], bool], Tuple[List[Union[nodes.comment, nodes.system_message]], bool]]: ...
    def explicit_list(self, blank_finish: bool) -> None: ...
    def anonymous(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...
    def anonymous_target(self, match: Match) -> Tuple[List[Union[nodes.target, str]], bool]: ...
    def line(self, match: Match, context: Any, next_state: str) -> Tuple[List[str], str, List[Any]]: ...
    def text(self, match: Match, context: Any, next_state: str) -> Optional[Tuple[List[str], str, List[Any]]]: ...

class RFC2822Body(Body):
    patterns: Dict[str, Union[str, Pattern]] = ...
    initial_transitions: Sequence[Tuple[str, str]] = ...
    def rfc2822(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...
    def rfc2822_field(self, match: Match) -> Tuple[nodes.field, bool]: ...

class SpecializedBody(Body):
    def invalid_input(self, match: Optional[Match] = ..., context: Optional[Any] = ..., next_state: Optional[str] = ...) -> None: ...
    # Description quoted below is taken from the docstring of SpecializedBody::
    #
    #     All transition methods are disabled (redefined as `invalid_input`).
    #     Override individual methods in subclasses to re-enable.
    #
    # Considering this purpose, we do not type following methods.
    #
    # indent
    # bullet
    # enumerator
    # field_marker
    # option_marker
    # doctest
    # line_block
    # grid_table_top
    # simple_table_top
    # explicit_markup
    # anonymous
    # line
    # text

class BulletList(SpecializedBody):
    blank_finish: bool = ...
    def bullet(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...

class DefinitionList(SpecializedBody):
    def text(self, match: Match, context: Any, next_state: str) -> Tuple[List[str], str, List[Any]]: ...

class EnumeratedList(SpecializedBody):
    auto: int = ...
    blank_finish: bool = ...
    lastordinal: int = ...
    def enumerator(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...

class FieldList(SpecializedBody):
    blank_finish: bool = ...
    def field_marker(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...

class OptionList(SpecializedBody):
    blank_finish: bool = ...
    def option_marker(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...

class RFC2822List(SpecializedBody, RFC2822Body):
    patterns: Dict[str, Union[str, Pattern]] = ...
    initial_transitions: List[Tuple[str, str]] = ...
    blank_finish: bool = ...
    def rfc2822(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...
    # blank

class ExtensionOptions(FieldList):
    def parse_field_body(self, indented: StringList, offset: int, node: nodes.Node) -> None: ...

class LineBlock(SpecializedBody):
    # blank
    blank_finish: bool = ...
    def line_block(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...

class Explicit(SpecializedBody):
    blank_finish: bool = ...
    def explicit_markup(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...
    def anonymous(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...
    # blank

class SubstitutionDef(Body):
    patterns: Dict[str, Union[str, Pattern]] = ...
    initial_transitions: List[str] = ...
    blank_finish: bool = ...
    def embedded_directive(self, match: Match, context: Any, next_state: str) -> None: ...
    def text(self, match: Match, context: Any, next_state: str) -> None: ...

class Text(RSTState):
    patterns: Dict[str, Union[str, Pattern]] = ...
    initial_transitions: List[Tuple[str, str]] = ...
    def blank(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...
    def eof(self, context: Any) -> List[Any]: ...
    def indent(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...
    def underline(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...
    def text(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...
    def literal_block(self) -> Union[List[nodes.Node], List[Union[nodes.literal_block, nodes.system_message]]]: ...
    def quoted_literal_block(self) -> List[nodes.Node]: ...
    def definition_list_item(self, termline: MutableSequence[str]) -> Tuple[nodes.definition_list_item, bool]: ...
    classifier_delimiter: Pattern = ...
    def term(self, lines: MutableSequence[str], lineno: int) -> Tuple[List[Union[nodes.term, nodes.classifier]], List[nodes.system_message]]: ...

class SpecializedText(Text):
    def eof(self, context: Any) -> List[Any]: ...
    def invalid_input(self, match: Optional[Match] = ..., context: Optional[Any] = ..., next_state: Optional[str] = ...): ...
    # Description quoted below is taken from the docstring of SpecializedBody::
    #
    #    All transition methods are disabled. Override individual methods in
    #    subclasses to re-enable.
    #
    # Considering this purpose, we do not type following methods.
    #
    # blank
    # indent
    # underline
    # text

class Definition(SpecializedText):
    def eof(self, context: Any) -> List[Any]: ...
    blank_finish: bool = ...
    def indent(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...

class Line(SpecializedText):
    eofcheck: int = ...
    def eof(self, context: Any) -> List[Any]: ...
    def blank(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...
    def text(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...
    # indent
    def underline(self, match: Match, context: Any, next_state: str) -> Tuple[List[Any], str, List[Any]]: ...
    def short_overline(self, context: Any, blocktext: str, lineno: int, lines: int = ...) -> None: ...
    def state_correction(self, context: Any, lines: int = ...) -> None: ...

class QuotedLiteralBlock(RSTState):
    patterns: Dict[str, Union[str, Pattern]] = ...
    initial_transitions: Tuple[str, str] = ...
    messages: List[nodes.system_message] = ...
    initial_lineno: Optional[int] = ...
    def __init__(self, state_machine: StateMachine, debug: bool = ...) -> None: ...
    def blank(self, match: Match, context: Any, next_state: str) -> Tuple[Any, str, List[Any]]: ...
    def eof(self, context: Any) -> List[Any]: ...
    def indent(self, match: Match, context: Any, next_state: str) -> None: ...
    def initial_quoted(self, match: Match, context: Any, next_state: str) -> Tuple[List[str], str, List[Any]]: ...
    def quoted(self, match: Match, context: Any, next_state: str) -> Tuple[Any, str, List[Any]]: ...
    def text(self, match: Match, context: Any, next_state: str) -> None: ...

state_classes: Sequence[Type[RSTState]]

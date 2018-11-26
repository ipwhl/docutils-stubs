# Stubs for docutils.nodes (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils import SettingsSpec
from docutils import nodes
from docutils.transforms import Transformer, Transform
from docutils.utils import Reporter

from typing import Any, Callable, Dict, Iterable, Iterator, List, Optional, overload, Tuple, Type, TypeVar

__docformat__: str

N_co = TypeVar('N_co', bound=nodes.Node, covariant=True)
_N = TypeVar('_N', bound=nodes.Node)

class Node:
    parent: nodes.Element = ...
    document: nodes.document = ...
    source: str = ...
    line: int = ...
    def __bool__(self) -> bool: ...
    def asdom(self, dom: Optional[Any] = ...) -> Any: ...
    def pformat(self, indent: str = ..., level: int = ...) -> str: ...
    def copy(self) -> nodes.Node: ...
    def deepcopy(self) -> nodes.Node: ...
    def setup_child(self, child: nodes.Node) -> None: ...
    def walk(self, visitor: nodes.NodeVisitor) -> bool: ...
    def walkabout(self, visitor: nodes.NodeVisitor) -> bool: ...

    @overload
    def traverse(self, condition: Type[_N] = ..., include_self: bool = ..., descend: bool = ..., siblings: bool = ..., ascend: bool = ...) -> List[_N]: ...
    @overload  # NOQA: F811
    def traverse(self, condition: Callable[[nodes.Node], bool] = ..., include_self: bool = ..., descend: bool = ..., siblings: bool = ..., ascend: bool = ...) -> List[_N]: ...

    def next_node(self, condition: Optional[Any] = ..., include_self: bool = ..., descend: bool = ..., siblings: bool = ..., ascend: bool = ...) -> nodes.Node: ...

def ensure_str(s: str) -> str: ...

class Text(Node, str):
    tagname: str = ...
    children: Tuple[nodes.Node, ...] = ...
    rawsource: str = ...
    def __new__(cls, data: str, rawsource: Optional[str] = ...): ...
    def __init__(self, data: str, rawsource: str = ...) -> None: ...
    def shortrepr(self, maxlen: int = ...) -> str: ...
    def astext(self) -> str: ...
    def copy(self) -> nodes.Text: ...
    def deepcopy(self) -> nodes.Text: ...
    def pformat(self, indent: str = ..., level: int = ...) -> str: ...
    def rstrip(self, chars: Optional[str] = ...) -> str: ...
    def lstrip(self, chars: Optional[str] = ...) -> str: ...

_E = TypeVar('_E', bound=nodes.Element)

class Element(Node):
    basic_attributes: Tuple[str, ...] = ...
    local_attributes: Tuple[str, ...] = ...
    list_attributes: Tuple[str, ...] = ...
    known_attributes: Tuple[str, ...] = ...
    tagname: str = ...
    child_text_separator: str = ...
    rawsource: str = ...
    children: List[nodes.Node] = ...
    attributes: Dict[str, Any] = ...
    def __init__(self, rawsource: str = ..., *children: nodes.Node, **attributes: Any) -> None: ...
    def shortrepr(self) -> str: ...
    def __unicode__(self) -> str: ...
    def starttag(self, quoteattr: Optional[Callable[[str], str]] = ...) -> str: ...
    def endtag(self) -> str: ...
    def emptytag(self) -> str: ...
    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, key: str) -> Any: ...
    @overload  # NOQA: F811
    def __getitem__(self, key: int) -> nodes.Node: ...
    @overload  # NOQA: F811
    def __getitem__(self, key: slice) -> List[N_co]: ...

    def __setitem__(self, key: Any, item: Any) -> Any: ...
    def __delitem__(self, key: Any) -> Any: ...
    def __add__(self, other: List[N_co]) -> List[N_co]: ...
    def __radd__(self, other: List[N_co]) -> List[N_co]: ...
    def __iadd__(self: _E, other: Any) -> _E: ...  # type: ignore
    def astext(self) -> str: ...
    def non_default_attributes(self) -> Dict[str, Any]: ...
    def attlist(self) -> List[Tuple[str, Any]]: ...
    def get(self, key: str, failobj: Optional[Any] = ...) -> Any: ...
    def hasattr(self, attr: str) -> bool: ...
    def delattr(self, attr: str) -> None: ...
    def setdefault(self, key: str, failobj: Optional[Any] = ...) -> Any: ...
    def has_key(self, attr: str) -> bool: ...
    def __contains__(self, attr: str) -> bool: ...
    def get_language_code(self, fallback: str = ...) -> str: ...
    def append(self, item: nodes.Node) -> None: ...
    def extend(self, item: Iterable[nodes.Node]) -> None: ...
    def insert(self, index: int, item: Any) -> None: ...
    def pop(self, i: int = ...) -> nodes.Node: ...
    def remove(self, item: nodes.Node) -> None: ...
    def index(self, item: nodes.Node) -> int: ...
    def is_not_default(self, key: str) -> int: ...
    def update_basic_atts(self, dict_: Any) -> None: ...
    def append_attr_list(self, attr: str, values: List) -> None: ...
    def coerce_append_attr_list(self, attr: str, value) -> None: ...
    def replace_attr(self, attr: str, value: Any, force: bool = ...) -> None: ...
    def copy_attr_convert(self, attr: str, value: Any, replace: bool = ...) -> None: ...
    def copy_attr_coerce(self, attr: str, value: Any, replace: bool) -> None: ...
    def copy_attr_concatenate(self, attr: str, value: Any, replace: bool) -> None: ...
    def copy_attr_consistent(self, attr: str, value: Any, replace: bool) -> None: ...
    def update_all_atts(self, dict_, update_fun: Callable[[str, Any, bool], None] = ..., replace: bool = ..., and_source: bool = ...) -> None: ...
    def update_all_atts_consistantly(self, dict_: Any, replace: bool = ..., and_source: bool = ...) -> None: ...
    def update_all_atts_concatenating(self, dict_: Any, replace: bool = ..., and_source: bool = ...) -> None: ...
    def update_all_atts_coercion(self, dict_: Any, replace: bool = ..., and_source: bool = ...) -> None: ...
    def update_all_atts_convert(self, dict_: Any, and_source: bool = ...) -> None: ...
    def clear(self) -> None: ...
    def replace(self, old: nodes.Node, new: Any) -> None: ...
    def replace_self(self, new: Any) -> None: ...
    def first_child_matching_class(self, childclass: Any, start: int = ..., end: int = ...) -> int: ...
    def first_child_not_matching_class(self, childclass: Any, start: int = ..., end: int = ...) -> int: ...
    def pformat(self, indent: str = ..., level: int = ...) -> str: ...
    def copy(self) -> nodes.Element: ...
    def deepcopy(self) -> nodes.Element: ...
    def set_class(self, name: str) -> None: ...
    referenced: int = ...
    def note_referenced_by(self, name: Optional[str] = ..., id: Optional[str] = ...) -> None: ...
    @classmethod
    def is_not_list_attribute(cls, attr: str) -> bool: ...
    @classmethod
    def is_not_known_attribute(cls, attr: str) -> bool: ...

    # dummy atribute to indicate to mypy that Element is Iterable
    def __iter__(self) -> Iterator[nodes.Node]: ...

class TextElement(Element):
    child_text_separator: str = ...
    def __init__(self, rawsource: str = ..., text: str = ..., *children: nodes.Node, **attributes: Any) -> None: ...

class FixedTextElement(TextElement):
    def __init__(self, rawsource: str = ..., text: str = ..., *children: nodes.Node, **attributes: Any) -> None: ...

class Resolvable:
    resolved: int = ...

class BackLinkable:
    def add_backref(self, refid: str) -> None: ...

class Root: ...
class Titular: ...
class PreBibliographic: ...
class Bibliographic: ...
class Decorative(PreBibliographic): ...
class Structural: ...
class Body: ...
class General(Body): ...
class Sequential(Body): ...
class Admonition(Body): ...
class Special(Body): ...
class Invisible(PreBibliographic): ...
class Part: ...
class Inline: ...
class Referential(Resolvable): ...

class Targetable(Resolvable):
    referenced: int = ...
    indirect_reference_name: str = ...

class Labeled: ...

class document(Root, Structural, Element):
    current_source: str = ...
    current_line: str = ...
    settings: SettingsSpec = ...
    reporter: Reporter = ...
    indirect_targets: List[nodes.target] = ...
    substitution_defs: Dict[str, nodes.substitution_definition] = ...
    substitution_names: Dict[str, str] = ...
    refnames: Dict[str, List[nodes.Node]] = ...
    refids: Dict[str, List[nodes.Node]] = ...
    nameids: Dict[str, str] = ...
    nametypes: Dict[str, bool] = ...
    ids: Dict[str, nodes.Node] = ...
    footnote_refs: Dict[str, nodes.footnote_reference] = ...
    citation_refs: Dict[str, nodes.citation_reference] = ...
    autofootnotes: List[nodes.Node] = ...
    autofootnote_refs: List[nodes.footnote_reference] = ...
    symbol_footnotes: List[nodes.footnote] = ...
    symbol_footnote_refs: List[nodes.footnote_reference] = ...
    footnotes: List[nodes.footnote] = ...
    citations: List[nodes.citation] = ...
    autofootnote_start: int = ...
    symbol_footnote_start: int = ...
    id_start: int = ...
    parse_messages: List[nodes.system_message] = ...
    transform_messages: List[nodes.system_message] = ...
    transformer: Transformer = ...
    decoration: nodes.decoration = ...
    document: nodes.document = ...
    def __init__(self, settings: SettingsSpec, reporter: Reporter, *args: nodes.Node, **kwargs: Any) -> None: ...
    def asdom(self, dom: Optional[Any] = ...) -> Any: ...
    def set_id(self, node: nodes.Node, msgnode: Optional[nodes.Node] = ...) -> str: ...
    def set_name_id_map(self, node: nodes.Node, id: str, msgnode: Optional[nodes.Node] = ..., explicit: Optional[bool] = ...) -> None: ...
    def set_duplicate_name_id(self, node: nodes.Node, id: str, name: str, msgnode: nodes.Node, explicit: bool) -> None: ...
    def has_name(self, name: str) -> bool: ...
    def note_implicit_target(self, target: nodes.Node, msgnode: Optional[nodes.Node] = ...) -> None: ...
    def note_explicit_target(self, target: nodes.Node, msgnode: Optional[nodes.Node] = ...) -> None: ...
    def note_refname(self, node: nodes.Node) -> None: ...
    def note_refid(self, node: nodes.Node) -> None: ...
    def note_indirect_target(self, target: nodes.target) -> None: ...
    def note_anonymous_target(self, target: nodes.target) -> None: ...
    def note_autofootnote(self, footnote: nodes.footnote) -> None: ...
    def note_autofootnote_ref(self, ref: nodes.footnote_reference) -> None: ...
    def note_symbol_footnote(self, footnote: nodes.footnote) -> None: ...
    def note_symbol_footnote_ref(self, ref: nodes.footnote_reference) -> None: ...
    def note_footnote(self, footnote: nodes.footnote) -> None: ...
    def note_footnote_ref(self, ref: nodes.footnote_reference) -> None: ...
    def note_citation(self, citation: nodes.citation) -> None: ...
    def note_citation_ref(self, ref: nodes.citation_reference) -> None: ...
    def note_substitution_def(self, subdef: nodes.substitution_definition, def_name: str, msgnode: Optional[nodes.Node] = ...) -> None: ...
    def note_substitution_ref(self, subref: nodes.substitution_reference, refname: str) -> None: ...
    def note_pending(self, pending: nodes.pending, priority: Optional[int] = ...) -> None: ...
    def note_parse_message(self, message: nodes.system_message) -> None: ...
    def note_transform_message(self, message: nodes.system_message) -> None: ...
    def note_source(self, source: str, offset: int) -> None: ...
    def copy(self) -> nodes.document: ...
    def get_decoration(self) -> nodes.decoration: ...

class title(Titular, PreBibliographic, TextElement): ...
class subtitle(Titular, PreBibliographic, TextElement): ...
class rubric(Titular, TextElement): ...
class docinfo(Bibliographic, Element): ...
class author(Bibliographic, TextElement): ...
class authors(Bibliographic, Element): ...
class organization(Bibliographic, TextElement): ...
class address(Bibliographic, FixedTextElement): ...
class contact(Bibliographic, TextElement): ...
class version(Bibliographic, TextElement): ...
class revision(Bibliographic, TextElement): ...
class status(Bibliographic, TextElement): ...
class date(Bibliographic, TextElement): ...
class copyright(Bibliographic, TextElement): ...

class decoration(Decorative, Element):
    def get_header(self) -> nodes.header: ...
    def get_footer(self) -> nodes.footer: ...

class header(Decorative, Element): ...
class footer(Decorative, Element): ...
class section(Structural, Element): ...
class topic(Structural, Element): ...
class sidebar(Structural, Element): ...
class transition(Structural, Element): ...
class paragraph(General, TextElement): ...
class compound(General, Element): ...
class container(General, Element): ...
class bullet_list(Sequential, Element): ...
class enumerated_list(Sequential, Element): ...
class list_item(Part, Element): ...
class definition_list(Sequential, Element): ...
class definition_list_item(Part, Element): ...
class term(Part, TextElement): ...
class classifier(Part, TextElement): ...
class definition(Part, Element): ...
class field_list(Sequential, Element): ...
class field(Part, Element): ...
class field_name(Part, TextElement): ...
class field_body(Part, Element): ...

class option(Part, Element):
    child_text_separator: str = ...

class option_argument(Part, TextElement):
    def astext(self) -> str: ...

class option_group(Part, Element):
    child_text_separator: str = ...

class option_list(Sequential, Element): ...

class option_list_item(Part, Element):
    child_text_separator: str = ...

class option_string(Part, TextElement): ...
class description(Part, Element): ...
class literal_block(General, FixedTextElement): ...
class doctest_block(General, FixedTextElement): ...
class math_block(General, FixedTextElement): ...
class line_block(General, Element): ...

class line(Part, TextElement):
    indent: Any = ...

class block_quote(General, Element): ...
class attribution(Part, TextElement): ...
class attention(Admonition, Element): ...
class caution(Admonition, Element): ...
class danger(Admonition, Element): ...
class error(Admonition, Element): ...
class important(Admonition, Element): ...
class note(Admonition, Element): ...
class tip(Admonition, Element): ...
class hint(Admonition, Element): ...
class warning(Admonition, Element): ...
class admonition(Admonition, Element): ...
class comment(Special, Invisible, FixedTextElement): ...
class substitution_definition(Special, Invisible, TextElement): ...
class target(Special, Invisible, Inline, TextElement, Targetable): ...
class footnote(General, BackLinkable, Element, Labeled, Targetable): ...
class citation(General, BackLinkable, Element, Labeled, Targetable): ...
class label(Part, TextElement): ...
class figure(General, Element): ...
class caption(Part, TextElement): ...
class legend(Part, Element): ...
class table(General, Element): ...
class tgroup(Part, Element): ...
class colspec(Part, Element): ...
class thead(Part, Element): ...
class tbody(Part, Element): ...
class row(Part, Element): ...
class entry(Part, Element): ...

class system_message(Special, BackLinkable, PreBibliographic, Element):
    def __init__(self, message: Optional[str] = ..., *children: nodes.Node, **attributes: Any) -> None: ...
    def astext(self) -> str: ...

class pending(Special, Invisible, Element):
    transform: Transform = ...
    details: Dict = ...
    def __init__(self, transform: Transform, details: Optional[Dict] = ..., rawsource: str = ..., *children: nodes.Node, **attributes: Any) -> None: ...
    def pformat(self, indent: str = ..., level: int = ...) -> str: ...
    def copy(self) -> nodes.system_message: ...

class raw(Special, Inline, PreBibliographic, FixedTextElement): ...
class emphasis(Inline, TextElement): ...
class strong(Inline, TextElement): ...
class literal(Inline, TextElement): ...
class reference(General, Inline, Referential, TextElement): ...
class footnote_reference(Inline, Referential, TextElement): ...
class citation_reference(Inline, Referential, TextElement): ...
class substitution_reference(Inline, TextElement): ...
class title_reference(Inline, TextElement): ...
class abbreviation(Inline, TextElement): ...
class acronym(Inline, TextElement): ...
class superscript(Inline, TextElement): ...
class subscript(Inline, TextElement): ...
class math(Inline, TextElement): ...

class image(General, Inline, Element):
    def astext(self) -> str: ...

class inline(Inline, TextElement): ...
class problematic(Inline, TextElement): ...
class generated(Inline, TextElement): ...

node_class_names: List[str] = ...

class NodeVisitor:
    optional: Tuple[str, ...] = ...
    document: nodes.document = ...
    def __init__(self, document: nodes.document) -> None: ...
    def dispatch_visit(self, node: nodes.Node) -> Any: ...
    def dispatch_departure(self, node: nodes.Node) -> Any: ...
    def unknown_visit(self, node: nodes.Node) -> Any: ...
    def unknown_departure(self, node: nodes.Node) -> Any: ...

class SparseNodeVisitor(NodeVisitor): ...

class GenericNodeVisitor(NodeVisitor):
    def default_visit(self, node: nodes.Node) -> Any: ...
    def default_departure(self, node: nodes.Node) -> Any: ...

class TreeCopyVisitor(GenericNodeVisitor):
    parent_stack: List[nodes.Node] = ...
    parent: List[nodes.Node] = ...
    def __init__(self, document: nodes.document) -> None: ...
    def get_tree_copy(self) -> nodes.Node: ...
    def default_visit(self, node: nodes.Node) -> None: ...
    def default_departure(self, node: nodes.Node) -> None: ...

class TreePruningException(Exception): ...
class SkipChildren(TreePruningException): ...
class SkipSiblings(TreePruningException): ...
class SkipNode(TreePruningException): ...
class SkipDeparture(TreePruningException): ...
class NodeFound(TreePruningException): ...
class StopTraversal(TreePruningException): ...

def make_id(string: str) -> str: ...
def dupname(node: nodes.Node, name: str) -> None: ...
def fully_normalize_name(name: str) -> str: ...
def whitespace_normalize_name(name: str) -> str: ...
def serial_escape(value: str) -> str: ...
def pseudo_quoteattr(value: str) -> str: ...

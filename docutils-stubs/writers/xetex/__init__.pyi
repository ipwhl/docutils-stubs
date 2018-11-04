# Stubs for docutils.writers.xetex (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils import nodes
from docutils.writers import latex2e
from typing import Any, Dict, List, Sequence, Tuple, Type

__docformat__: str

class Writer(latex2e.Writer):
    supported: Tuple[str, ...] = ...
    default_template: str = ...
    default_preamble: str = ...
    config_section: str = ...
    config_section_dependencies: Sequence[str] = ...
    settings_spec: Tuple[str, Any, Tuple[Tuple[str, List[str], Dict[str, Any]], ...]] = ...
    translator_class: Type[XeLaTeXTranslator] = ...
    def __init__(self) -> None: ...

class Babel(latex2e.Babel):
    language_codes: Dict[str, str] = ...
    language_code: str = ...
    reporter: Any = ...
    language: str = ...
    otherlanguages: Dict[str, Any] = ...
    warn_msg: str = ...
    quote_index: int = ...
    quotes: Tuple[str, str] = ...
    literal_double_quote: str = ...
    def __init__(self, language_code: str, reporter: Any) -> None: ...
    def __call__(self): ...

class XeLaTeXTranslator(latex2e.LaTeXTranslator):
    is_xetex: bool = ...
    def __init__(self, document: nodes.document) -> None: ...
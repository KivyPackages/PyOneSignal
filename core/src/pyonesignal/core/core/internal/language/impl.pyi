from typing import Any, ClassVar, overload
from user.internal.properties.PropertiesModelStore import PropertiesModelStore

class LanguageContext:
    def __init__(self, p0: PropertiesModelStore) -> None: ...
    def setLanguage(self, p0: str) -> None: ...
    def getLanguage(self) -> str: ...

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class DefaultConstructorMarker:
    """Forward declaration for ``kotlin.jvm.internal.DefaultConstructorMarker``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.internal.DefaultConstructorMarker')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/internal/DefaultConstructorMarker/
    """
    ...

class LanguageProviderDevice:
    Companion: ClassVar[Any]
    def __init__(self) -> None: ...
    def getLanguage(self) -> str: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...


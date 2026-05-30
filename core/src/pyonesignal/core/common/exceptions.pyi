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

class BackendException:
    @overload
    def __init__(self, p0: int, p1: str, p2: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: str, p2: int, p3: int, p4: DefaultConstructorMarker) -> None: ...
    def getStatusCode(self) -> int: ...
    def getResponse(self) -> str: ...
    def getRetryAfterSeconds(self) -> int: ...

from typing import Any, ClassVar, overload

class MainThreadException:
    def __init__(self, p0: str) -> None: ...


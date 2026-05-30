from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Continuation:
    """Forward declaration for ``kotlin.coroutines.Continuation``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.coroutines.Continuation')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/coroutines/Continuation/
    """
    ...

class INotificationBackendService:
    def updateNotificationAsReceived(self, p0: str, p1: str, p2: str, p3: Any, p4: Continuation) -> Any: ...
    def updateNotificationAsOpened(self, p0: str, p1: str, p2: str, p3: Any, p4: Continuation) -> Any: ...


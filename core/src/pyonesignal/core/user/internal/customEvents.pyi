from typing import Any, ClassVar, overload
from user.internal.customEvents.impl.CustomEventMetadata import CustomEventMetadata

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

class ICustomEventBackendService:
    def sendCustomEvent(self, p0: str, p1: str, p2: str, p3: int, p4: str, p5: str, p6: CustomEventMetadata, p7: str, p8: Continuation) -> Any: ...

    class DefaultImpls:
        @staticmethod
        def sendCustomEvent$default(p0: "ICustomEventBackendService", p1: str, p2: str, p3: str, p4: int, p5: str, p6: str, p7: CustomEventMetadata, p8: str, p9: Continuation, p10: int, p11: Any) -> Any: ...

from typing import Any, ClassVar, overload

class ICustomEventController:
    def sendCustomEvent(self, p0: str, p1: dict) -> None: ...


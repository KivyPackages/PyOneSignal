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

class INotificationRestoreProcessor:
    def process(self, p0: Continuation) -> Any: ...
    def processNotification(self, p0: Any, p1: int, p2: Continuation) -> Any: ...

    class DefaultImpls:
        @staticmethod
        def processNotification$default(p0: "INotificationRestoreProcessor", p1: Any, p2: int, p3: Continuation, p4: int, p5: Any) -> Any: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context

class INotificationRestoreWorkManager:
    def beginEnqueueingWork(self, p0: Context, p1: bool) -> None: ...


from typing import Any, ClassVar, overload
from pyonesignal.core.internal.application.IApplicationService import IApplicationService
from pyonesignal.core.internal.config.ConfigModelStore import ConfigModelStore
from pyonesignal.core.internal.time.ITime import ITime

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
class Method:
    """Forward declaration for ``java.lang.reflect.Method``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.reflect.Method')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/Method.html
    """
    ...

class FirebaseAnalyticsTracker:
    Companion: ClassVar[Any]
    def __init__(self, p0: IApplicationService, p1: ConfigModelStore, p2: ITime) -> None: ...
    def trackInfluenceOpenEvent(self) -> None: ...
    def trackOpenedEvent(self, p0: str, p1: str) -> None: ...
    def trackReceivedEvent(self, p0: str, p1: str) -> None: ...
    @staticmethod
    def access$setFirebaseAnalyticsClass$cp(p0: type) -> None: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...
        @staticmethod
        def access$getTrackMethod(p0: Any, p1: type) -> Method: ...
        @staticmethod
        def access$getInstanceMethod(p0: Any, p1: type) -> Method: ...
        def canTrack(self) -> bool: ...

from typing import Any, ClassVar, overload

class NoAnalyticsTracker:
    def __init__(self) -> None: ...
    def trackInfluenceOpenEvent(self) -> None: ...
    def trackOpenedEvent(self, p0: str, p1: str) -> None: ...
    def trackReceivedEvent(self, p0: str, p1: str) -> None: ...


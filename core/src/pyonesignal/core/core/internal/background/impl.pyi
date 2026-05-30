from typing import Any, ClassVar, overload
from core.internal.application.IApplicationService import IApplicationService
from core.internal.time.ITime import ITime

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
class Job:
    """Forward declaration for ``kotlinx.coroutines.Job``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlinx.coroutines.Job')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlinx/coroutines/Job/
    """
    ...
class DefaultConstructorMarker:
    """Forward declaration for ``kotlin.jvm.internal.DefaultConstructorMarker``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.internal.DefaultConstructorMarker')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/internal/DefaultConstructorMarker/
    """
    ...

class BackgroundManager:
    Companion: ClassVar[Any]
    def __init__(self, p0: IApplicationService, p1: ITime, p2: list) -> None: ...
    def start(self) -> None: ...
    def setNeedsJobReschedule(self, p0: bool) -> None: ...
    def cancelRunBackgroundServices(self) -> bool: ...
    def runBackgroundServices(self, p0: Continuation) -> Any: ...
    def getNeedsJobReschedule(self) -> bool: ...
    @staticmethod
    def access$cancelSyncTask(p0: "BackgroundManager") -> None: ...
    @staticmethod
    def access$scheduleBackground(p0: "BackgroundManager") -> None: ...
    @staticmethod
    def access$setBackgroundSyncJob$p(p0: "BackgroundManager", p1: Job) -> None: ...
    @staticmethod
    def access$getLock$p(p0: "BackgroundManager") -> Any: ...
    @staticmethod
    def access$get_backgroundServices$p(p0: "BackgroundManager") -> list: ...
    @staticmethod
    def access$setNextScheduledSyncTimeMs$p(p0: "BackgroundManager", p1: int) -> None: ...
    def onFocus(self, p0: bool) -> None: ...
    def onUnfocused(self) -> None: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...


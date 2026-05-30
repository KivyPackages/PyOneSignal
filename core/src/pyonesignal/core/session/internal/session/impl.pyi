from typing import Any, ClassVar, overload
from core.internal.config.ConfigModelStore import ConfigModelStore
from core.internal.operations.IOperationRepo import IOperationRepo
from session.internal.outcomes.IOutcomeEventsController import IOutcomeEventsController
from session.internal.session.ISessionService import ISessionService
from user.internal.identity.IdentityModelStore import IdentityModelStore
from user.internal.properties.PropertiesModelStore import PropertiesModelStore

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

class SessionListener:
    Companion: ClassVar[Any]
    SECONDS_IN_A_DAY: ClassVar[int]
    def __init__(self, p0: IOperationRepo, p1: ISessionService, p2: ConfigModelStore, p3: IdentityModelStore, p4: PropertiesModelStore, p5: IOutcomeEventsController) -> None: ...
    def start(self) -> None: ...
    def onSessionStarted(self) -> None: ...
    def onSessionActive(self) -> None: ...
    def onSessionEnded(self, p0: int) -> None: ...
    @staticmethod
    def access$get_outcomeEventsController$p(p0: "SessionListener") -> IOutcomeEventsController: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

from typing import Any, ClassVar, overload
from core.internal.application.IApplicationService import IApplicationService
from core.internal.config.ConfigModelStore import ConfigModelStore
from core.internal.time.ITime import ITime
from session.internal.session.ISessionLifecycleHandler import ISessionLifecycleHandler
from session.internal.session.SessionModelStore import SessionModelStore

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

class SessionService:
    def __init__(self, p0: IApplicationService, p1: ConfigModelStore, p2: SessionModelStore, p3: ITime) -> None: ...
    def start(self) -> None: ...
    def getHasSubscribers(self) -> bool: ...
    @overload
    def subscribe(self, p0: Any) -> None: ...
    @overload
    def subscribe(self, p0: ISessionLifecycleHandler) -> None: ...
    @overload
    def unsubscribe(self, p0: Any) -> None: ...
    @overload
    def unsubscribe(self, p0: ISessionLifecycleHandler) -> None: ...
    def bootstrap(self) -> None: ...
    def getStartTime(self) -> int: ...
    def onFocus(self, p0: bool) -> None: ...
    def onUnfocused(self) -> None: ...
    def backgroundRun(self, p0: Continuation) -> Any: ...
    def getScheduleBackgroundRunIn(self) -> int: ...
    @staticmethod
    def access$handleOnFocus(p0: "SessionService", p1: bool, p2: int) -> None: ...
    @staticmethod
    def access$handleOnUnfocused(p0: "SessionService", p1: int) -> None: ...


from typing import Any, ClassVar, overload
from notifications.internal.badges.IBadgeCountUpdater import IBadgeCountUpdater
from notifications.internal.data.INotificationRepository import INotificationRepository
from notifications.internal.generation.INotificationGenerationWorkManager import INotificationGenerationWorkManager
from pyonesignal.core.internal.application.IApplicationService import IApplicationService

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
class DefaultConstructorMarker:
    """Forward declaration for ``kotlin.jvm.internal.DefaultConstructorMarker``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.internal.DefaultConstructorMarker')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/internal/DefaultConstructorMarker/
    """
    ...

class NotificationRestoreProcessor:
    Companion: ClassVar[Any]
    DEFAULT_TTL_IF_NOT_IN_PAYLOAD: ClassVar[int]
    def __init__(self, p0: IApplicationService, p1: INotificationGenerationWorkManager, p2: INotificationRepository, p3: IBadgeCountUpdater) -> None: ...
    def process(self, p0: Continuation) -> Any: ...
    def processNotification(self, p0: Any, p1: int, p2: Continuation) -> Any: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from androidx.work.WorkerParameters import WorkerParameters

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
class Continuation:
    """Forward declaration for ``kotlin.coroutines.Continuation``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.coroutines.Continuation')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/coroutines/Continuation/
    """
    ...

class NotificationRestoreWorkManager:
    Companion: ClassVar[Any]
    def __init__(self) -> None: ...
    def beginEnqueueingWork(self, p0: Context, p1: bool) -> None: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

    class NotificationRestoreWorker:
        def __init__(self, p0: Context, p1: WorkerParameters) -> None: ...
        def doWork(self, p0: Continuation) -> Any: ...


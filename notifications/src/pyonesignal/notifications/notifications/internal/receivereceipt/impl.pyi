from typing import Any, ClassVar, overload
from notifications.internal.backend.INotificationBackendService import INotificationBackendService
from pyonesignal.core.internal.device.IDeviceService import IDeviceService

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

class ReceiveReceiptProcessor:
    def __init__(self, p0: IDeviceService, p1: INotificationBackendService) -> None: ...
    def sendReceiveReceipt(self, p0: str, p1: str, p2: str, p3: Continuation) -> Any: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from androidx.work.WorkerParameters import WorkerParameters
from pyonesignal.core.internal.application.IApplicationService import IApplicationService
from pyonesignal.core.internal.config.ConfigModelStore import ConfigModelStore

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class ISubscriptionManager:
    """Forward declaration for ``com.onesignal.user.internal.subscriptions.ISubscriptionManager``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.user.internal.subscriptions.ISubscriptionManager')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
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
class Continuation:
    """Forward declaration for ``kotlin.coroutines.Continuation``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.coroutines.Continuation')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/coroutines/Continuation/
    """
    ...

class ReceiveReceiptWorkManager:
    Companion: ClassVar[Any]
    def __init__(self, p0: IApplicationService, p1: ConfigModelStore, p2: ISubscriptionManager) -> None: ...
    def enqueueReceiveReceipt(self, p0: str) -> None: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

    class ReceiveReceiptWorker:
        def __init__(self, p0: Context, p1: WorkerParameters) -> None: ...
        def doWork(self, p0: Continuation) -> Any: ...


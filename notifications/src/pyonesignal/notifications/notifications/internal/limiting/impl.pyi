from typing import Any, ClassVar, overload
from notifications.internal.data.INotificationRepository import INotificationRepository
from notifications.internal.summary.INotificationSummaryManager import INotificationSummaryManager
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

class NotificationLimitManager:
    def __init__(self, p0: INotificationRepository, p1: IApplicationService, p2: INotificationSummaryManager) -> None: ...
    def clearOldestOverLimit(self, p0: int, p1: Continuation) -> Any: ...
    @staticmethod
    def access$clearOldestOverLimitStandard(p0: "NotificationLimitManager", p1: int, p2: Continuation) -> Any: ...


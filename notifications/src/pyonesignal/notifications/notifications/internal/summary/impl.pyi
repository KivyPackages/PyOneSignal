from typing import Any, ClassVar, overload
from notifications.internal.data.INotificationRepository import INotificationRepository
from notifications.internal.display.ISummaryNotificationDisplayer import ISummaryNotificationDisplayer
from notifications.internal.restoration.INotificationRestoreProcessor import INotificationRestoreProcessor
from pyonesignal.core.internal.application.IApplicationService import IApplicationService
from pyonesignal.core.internal.config.ConfigModelStore import ConfigModelStore
from pyonesignal.core.internal.time.ITime import ITime

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

class NotificationSummaryManager:
    def __init__(self, p0: IApplicationService, p1: INotificationRepository, p2: ISummaryNotificationDisplayer, p3: ConfigModelStore, p4: INotificationRestoreProcessor, p5: ITime) -> None: ...
    def updatePossibleDependentSummaryOnDismiss(self, p0: int, p1: Continuation) -> Any: ...
    def updateSummaryNotificationAfterChildRemoved(self, p0: str, p1: bool, p2: Continuation) -> Any: ...
    def clearNotificationOnSummaryClick(self, p0: str, p1: Continuation) -> Any: ...
    @staticmethod
    def access$restoreSummary(p0: "NotificationSummaryManager", p1: str, p2: Continuation) -> Any: ...
    @staticmethod
    def access$internalUpdateSummaryNotificationAfterChildRemoved(p0: "NotificationSummaryManager", p1: str, p2: bool, p3: Continuation) -> Any: ...


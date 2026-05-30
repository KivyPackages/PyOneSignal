from typing import Any, ClassVar, overload
from android.content.Context import Context
from notifications.internal.Notification import Notification
from notifications.internal.common.NotificationGenerationJob import NotificationGenerationJob
from notifications.internal.data.INotificationRepository import INotificationRepository
from notifications.internal.display.INotificationDisplayer import INotificationDisplayer
from notifications.internal.lifecycle.INotificationLifecycleService import INotificationLifecycleService
from notifications.internal.summary.INotificationSummaryManager import INotificationSummaryManager
from pyonesignal.core.internal.application.IApplicationService import IApplicationService
from pyonesignal.core.internal.config.ConfigModelStore import ConfigModelStore
from pyonesignal.core.internal.time.ITime import ITime

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class JSONObject:
    """Forward declaration for ``org.json.JSONObject``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONObject')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
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

class NotificationGenerationProcessor:
    def __init__(self, p0: IApplicationService, p1: INotificationDisplayer, p2: ConfigModelStore, p3: INotificationRepository, p4: INotificationSummaryManager, p5: INotificationLifecycleService, p6: ITime) -> None: ...
    def processNotificationData(self, p0: Context, p1: int, p2: JSONObject, p3: bool, p4: int, p5: Continuation) -> Any: ...
    @staticmethod
    def access$get_lifecycleService$p(p0: "NotificationGenerationProcessor") -> INotificationLifecycleService: ...
    @staticmethod
    def access$processHandlerResponse(p0: "NotificationGenerationProcessor", p1: NotificationGenerationJob, p2: bool, p3: bool, p4: Continuation) -> Any: ...
    @staticmethod
    def access$isDuplicateNotification(p0: "NotificationGenerationProcessor", p1: Notification, p2: Continuation) -> Any: ...
    @staticmethod
    def access$postProcessNotification(p0: "NotificationGenerationProcessor", p1: NotificationGenerationJob, p2: bool, p3: bool, p4: Continuation) -> Any: ...
    @staticmethod
    def access$saveNotification(p0: "NotificationGenerationProcessor", p1: NotificationGenerationJob, p2: bool, p3: Continuation) -> Any: ...
    @staticmethod
    def access$markNotificationAsDismissed(p0: "NotificationGenerationProcessor", p1: NotificationGenerationJob, p2: Continuation) -> Any: ...
    @staticmethod
    def access$processCollapseKey(p0: "NotificationGenerationProcessor", p1: NotificationGenerationJob, p2: Continuation) -> Any: ...
    def getCustomJSONObject(self, p0: JSONObject) -> JSONObject: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from androidx.work.WorkerParameters import WorkerParameters

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class JSONObject:
    """Forward declaration for ``org.json.JSONObject``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONObject')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...
class ConcurrentHashMap:
    """Forward declaration for ``java.util.concurrent.ConcurrentHashMap``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.util.concurrent.ConcurrentHashMap')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentHashMap.html
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

class NotificationGenerationWorkManager:
    Companion: ClassVar[Any]
    def __init__(self) -> None: ...
    def beginEnqueueingWork(self, p0: Context, p1: str, p2: int, p3: JSONObject, p4: int, p5: bool, p6: bool) -> bool: ...
    @staticmethod
    def access$getNotificationIds$cp() -> ConcurrentHashMap: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...
        def addNotificationIdProcessed(self, p0: str) -> bool: ...
        def removeNotificationIdProcessed(self, p0: str) -> None: ...

    class NotificationGenerationWorker:
        def __init__(self, p0: Context, p1: WorkerParameters) -> None: ...
        def doWork(self, p0: Continuation) -> Any: ...


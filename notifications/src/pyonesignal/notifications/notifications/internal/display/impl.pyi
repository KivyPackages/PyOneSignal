from typing import Any, ClassVar, overload
from android.app.PendingIntent import PendingIntent
from android.content.Context import Context
from android.content.Intent import Intent

class IntentGeneratorForAttachingToNotifications:
    def __init__(self, p0: Context) -> None: ...
    def getContext(self) -> Context: ...
    def getNewActionPendingIntent(self, p0: int, p1: Intent) -> PendingIntent: ...
    def getNewBaseIntent(self, p0: int) -> Intent: ...

from typing import Any, ClassVar, overload
from android.app.Notification import Notification
from android.app.PendingIntent import PendingIntent
from android.content.Intent import Intent
from android.graphics.Bitmap import Bitmap
from notifications.internal.channels.INotificationChannelManager import INotificationChannelManager
from notifications.internal.common.NotificationGenerationJob import NotificationGenerationJob
from notifications.internal.display.impl.IntentGeneratorForAttachingToNotifications import IntentGeneratorForAttachingToNotifications
from pyonesignal.core.internal.application.IApplicationService import IApplicationService

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

class NotificationDisplayBuilder:
    def __init__(self, p0: IApplicationService, p1: INotificationChannelManager) -> None: ...
    def getTitle(self, p0: JSONObject) -> str: ...
    def getDefaultLargeIcon(self) -> Bitmap: ...
    def getDefaultSmallIconId(self) -> int: ...
    def getGroupAlertBehavior(self) -> int: ...
    def getNewDismissActionPendingIntent(self, p0: int, p1: Intent) -> PendingIntent: ...
    def getNewBaseDismissIntent(self, p0: int) -> Intent: ...
    def getBaseOneSignalNotificationBuilder(self, p0: NotificationGenerationJob) -> Any: ...
    def removeNotifyOptions(self, p0: Any) -> None: ...
    def addXiaomiSettings(self, p0: Any, p1: Notification) -> None: ...
    def addNotificationActionButtons(self, p0: JSONObject, p1: IntentGeneratorForAttachingToNotifications, p2: Any, p3: int, p4: str) -> None: ...

    class OneSignalNotificationBuilder:
        def __init__(self) -> None: ...
        def getCompatBuilder(self) -> Any: ...
        def setCompatBuilder(self, p0: Any) -> None: ...
        def getHasLargeIcon(self) -> bool: ...
        def setHasLargeIcon(self, p0: bool) -> None: ...

from typing import Any, ClassVar, overload
from notifications.internal.common.NotificationGenerationJob import NotificationGenerationJob
from notifications.internal.display.INotificationDisplayBuilder import INotificationDisplayBuilder
from notifications.internal.display.ISummaryNotificationDisplayer import ISummaryNotificationDisplayer
from notifications.internal.limiting.INotificationLimitManager import INotificationLimitManager
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
class Unit:
    """Forward declaration for ``kotlin.Unit``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.Unit')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/Unit/
    """
    ...

class NotificationDisplayer:
    def __init__(self, p0: IApplicationService, p1: INotificationLimitManager, p2: ISummaryNotificationDisplayer, p3: INotificationDisplayBuilder) -> None: ...
    def displayNotification(self, p0: NotificationGenerationJob, p1: Continuation) -> Any: ...
    def isRunningOnMainThreadCheck(self) -> Unit: ...
    @staticmethod
    def access$showNotification(p0: "NotificationDisplayer", p1: NotificationGenerationJob, p2: Continuation) -> Any: ...

from typing import Any, ClassVar, overload
from android.app.Notification import Notification
from notifications.internal.common.NotificationGenerationJob import NotificationGenerationJob
from notifications.internal.data.INotificationRepository import INotificationRepository
from notifications.internal.display.INotificationDisplayBuilder import INotificationDisplayBuilder
from notifications.internal.display.impl.IntentGeneratorForAttachingToNotifications import IntentGeneratorForAttachingToNotifications
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
class JSONObject:
    """Forward declaration for ``org.json.JSONObject``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONObject')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class SummaryNotificationDisplayer:
    def __init__(self, p0: IApplicationService, p1: INotificationRepository, p2: INotificationDisplayBuilder) -> None: ...
    def createSummaryNotification(self, p0: NotificationGenerationJob, p1: Any, p2: int, p3: Continuation) -> Any: ...
    def updateSummaryNotification(self, p0: NotificationGenerationJob, p1: Continuation) -> Any: ...
    def createGenericPendingIntentsForGroup(self, p0: Any, p1: IntentGeneratorForAttachingToNotifications, p2: JSONObject, p3: str, p4: int) -> None: ...
    def createSingleNotificationBeforeSummaryBuilder(self, p0: NotificationGenerationJob, p1: Any) -> Notification: ...
    def createGrouplessSummaryNotification(self, p0: NotificationGenerationJob, p1: IntentGeneratorForAttachingToNotifications, p2: int, p3: int, p4: Continuation) -> Any: ...


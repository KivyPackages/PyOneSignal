from typing import Any, ClassVar, overload
from android.app.Notification import Notification
from android.app.PendingIntent import PendingIntent
from android.content.Intent import Intent
from android.graphics.Bitmap import Bitmap
from notifications.internal.common.NotificationGenerationJob import NotificationGenerationJob
from notifications.internal.display.impl.IntentGeneratorForAttachingToNotifications import IntentGeneratorForAttachingToNotifications

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

class INotificationDisplayBuilder:
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

from typing import Any, ClassVar, overload
from notifications.internal.common.NotificationGenerationJob import NotificationGenerationJob

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

class INotificationDisplayer:
    def displayNotification(self, p0: NotificationGenerationJob, p1: Continuation) -> Any: ...

from typing import Any, ClassVar, overload
from android.app.Notification import Notification
from notifications.internal.common.NotificationGenerationJob import NotificationGenerationJob
from notifications.internal.display.impl.IntentGeneratorForAttachingToNotifications import IntentGeneratorForAttachingToNotifications

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

class ISummaryNotificationDisplayer:
    def createSingleNotificationBeforeSummaryBuilder(self, p0: NotificationGenerationJob, p1: Any) -> Notification: ...
    def updateSummaryNotification(self, p0: NotificationGenerationJob, p1: Continuation) -> Any: ...
    def createGenericPendingIntentsForGroup(self, p0: Any, p1: IntentGeneratorForAttachingToNotifications, p2: JSONObject, p3: str, p4: int) -> None: ...
    def createGrouplessSummaryNotification(self, p0: NotificationGenerationJob, p1: IntentGeneratorForAttachingToNotifications, p2: int, p3: int, p4: Continuation) -> Any: ...
    def createSummaryNotification(self, p0: NotificationGenerationJob, p1: Any, p2: int, p3: Continuation) -> Any: ...


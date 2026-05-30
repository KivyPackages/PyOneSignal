from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class JSONArray:
    """Forward declaration for ``org.json.JSONArray``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONArray')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
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

class NotificationIntentExtras:
    def __init__(self, p0: JSONArray, p1: JSONObject) -> None: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def copy(self, p0: JSONArray, p1: JSONObject) -> "NotificationIntentExtras": ...
    def getJsonData(self) -> JSONObject: ...
    def setJsonData(self, p0: JSONObject) -> None: ...
    def getDataArray(self) -> JSONArray: ...
    def setDataArray(self, p0: JSONArray) -> None: ...
    def component1(self) -> JSONArray: ...
    def component2(self) -> JSONObject: ...
    @staticmethod
    def copy$default(p0: "NotificationIntentExtras", p1: JSONArray, p2: JSONObject, p3: int, p4: Any) -> "NotificationIntentExtras": ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.content.Intent import Intent
from notifications.internal.data.INotificationRepository import INotificationRepository
from notifications.internal.lifecycle.INotificationLifecycleService import INotificationLifecycleService
from notifications.internal.summary.INotificationSummaryManager import INotificationSummaryManager
from pyonesignal.core.internal.config.ConfigModelStore import ConfigModelStore

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
class JSONArray:
    """Forward declaration for ``org.json.JSONArray``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONArray')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class NotificationOpenedProcessor:
    def __init__(self, p0: INotificationSummaryManager, p1: INotificationRepository, p2: ConfigModelStore, p3: INotificationLifecycleService) -> None: ...
    def processFromContext(self, p0: Context, p1: Intent, p2: Continuation) -> Any: ...
    @staticmethod
    def access$processIntent(p0: "NotificationOpenedProcessor", p1: Context, p2: Intent, p3: Continuation) -> Any: ...
    @staticmethod
    def access$processToOpenIntent(p0: "NotificationOpenedProcessor", p1: Context, p2: Intent, p3: str, p4: Continuation) -> Any: ...
    @staticmethod
    def access$addChildNotifications(p0: "NotificationOpenedProcessor", p1: JSONArray, p2: str, p3: Continuation) -> Any: ...
    @staticmethod
    def access$markNotificationsConsumed(p0: "NotificationOpenedProcessor", p1: Context, p2: Intent, p3: bool, p4: Continuation) -> Any: ...
    @staticmethod
    def access$clearStatusBarNotifications(p0: "NotificationOpenedProcessor", p1: Context, p2: str, p3: Continuation) -> Any: ...

from typing import Any, ClassVar, overload
from android.app.Activity import Activity
from android.content.Intent import Intent
from notifications.internal.lifecycle.INotificationLifecycleService import INotificationLifecycleService

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

class NotificationOpenedProcessorHMS:
    def __init__(self, p0: INotificationLifecycleService) -> None: ...
    @staticmethod
    def access$handleProcessJsonOpenData(p0: "NotificationOpenedProcessorHMS", p1: Activity, p2: JSONObject, p3: Continuation) -> Any: ...
    def handleHMSNotificationOpenIntent(self, p0: Activity, p1: Intent, p2: Continuation) -> Any: ...


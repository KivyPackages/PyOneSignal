from typing import Any, ClassVar, overload
from android.app.Activity import Activity

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

class INotificationLifecycleCallback:
    def canReceiveNotification(self, p0: JSONObject, p1: Continuation) -> Any: ...
    def canOpenNotification(self, p0: Activity, p1: JSONObject, p2: Continuation) -> Any: ...

from typing import Any, ClassVar, overload
from android.app.Activity import Activity
from notifications.internal.common.NotificationGenerationJob import NotificationGenerationJob
from notifications.internal.lifecycle.INotificationLifecycleCallback import INotificationLifecycleCallback

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
class INotificationReceivedEvent:
    """Forward declaration for ``com.onesignal.notifications.INotificationReceivedEvent``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.notifications.INotificationReceivedEvent')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...
class INotificationWillDisplayEvent:
    """Forward declaration for ``com.onesignal.notifications.INotificationWillDisplayEvent``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.notifications.INotificationWillDisplayEvent')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
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
class INotificationLifecycleListener:
    """Forward declaration for ``com.onesignal.notifications.INotificationLifecycleListener``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.notifications.INotificationLifecycleListener')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...
class INotificationClickListener:
    """Forward declaration for ``com.onesignal.notifications.INotificationClickListener``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.notifications.INotificationClickListener')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class INotificationLifecycleService:
    def setInternalNotificationLifecycleCallback(self, p0: INotificationLifecycleCallback) -> None: ...
    def canReceiveNotification(self, p0: JSONObject, p1: Continuation) -> Any: ...
    def notificationReceived(self, p0: NotificationGenerationJob, p1: Continuation) -> Any: ...
    def externalRemoteNotificationReceived(self, p0: INotificationReceivedEvent) -> None: ...
    def externalNotificationWillShowInForeground(self, p0: INotificationWillDisplayEvent) -> None: ...
    def canOpenNotification(self, p0: Activity, p1: JSONObject, p2: Continuation) -> Any: ...
    def notificationOpened(self, p0: Activity, p1: JSONArray, p2: Continuation) -> Any: ...
    def addExternalForegroundLifecycleListener(self, p0: INotificationLifecycleListener) -> None: ...
    def removeExternalForegroundLifecycleListener(self, p0: INotificationLifecycleListener) -> None: ...
    def addExternalClickListener(self, p0: INotificationClickListener) -> None: ...
    def removeExternalClickListener(self, p0: INotificationClickListener) -> None: ...


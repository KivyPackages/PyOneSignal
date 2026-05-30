from typing import Any, ClassVar, overload
from android.app.Activity import Activity
from android.content.Context import Context
from notifications.internal.analytics.IAnalyticsTracker import IAnalyticsTracker
from notifications.internal.backend.INotificationBackendService import INotificationBackendService
from notifications.internal.common.NotificationGenerationJob import NotificationGenerationJob
from notifications.internal.lifecycle.INotificationLifecycleCallback import INotificationLifecycleCallback
from notifications.internal.receivereceipt.IReceiveReceiptWorkManager import IReceiveReceiptWorkManager
from pyonesignal.core.internal.application.IApplicationService import IApplicationService
from pyonesignal.core.internal.config.ConfigModelStore import ConfigModelStore
from pyonesignal.core.internal.device.IDeviceService import IDeviceService
from pyonesignal.core.internal.time.ITime import ITime

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class IInfluenceManager:
    """Forward declaration for ``com.onesignal.session.internal.influence.IInfluenceManager``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.session.internal.influence.IInfluenceManager')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...
class ISubscriptionManager:
    """Forward declaration for ``com.onesignal.user.internal.subscriptions.ISubscriptionManager``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.user.internal.subscriptions.ISubscriptionManager')`` proxy; this empty class exists
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
class JSONObject:
    """Forward declaration for ``org.json.JSONObject``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONObject')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
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
class DefaultConstructorMarker:
    """Forward declaration for ``kotlin.jvm.internal.DefaultConstructorMarker``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.internal.DefaultConstructorMarker')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/internal/DefaultConstructorMarker/
    """
    ...

class NotificationLifecycleService:
    Companion: ClassVar[Any]
    def __init__(self, p0: IApplicationService, p1: ITime, p2: ConfigModelStore, p3: IInfluenceManager, p4: ISubscriptionManager, p5: IDeviceService, p6: INotificationBackendService, p7: IReceiveReceiptWorkManager, p8: IAnalyticsTracker) -> None: ...
    def setupNotificationServiceExtension(self, p0: Context) -> None: ...
    @staticmethod
    def access$confirmNotificationOpened(p0: "NotificationLifecycleService", p1: str, p2: str, p3: str, p4: Any, p5: Continuation) -> Any: ...
    def setInternalNotificationLifecycleCallback(self, p0: INotificationLifecycleCallback) -> None: ...
    def canReceiveNotification(self, p0: JSONObject, p1: Continuation) -> Any: ...
    def notificationReceived(self, p0: NotificationGenerationJob, p1: Continuation) -> Any: ...
    def externalRemoteNotificationReceived(self, p0: INotificationReceivedEvent) -> None: ...
    def externalNotificationWillShowInForeground(self, p0: INotificationWillDisplayEvent) -> None: ...
    def canOpenNotification(self, p0: Activity, p1: JSONObject, p2: Continuation) -> Any: ...
    def notificationOpened(self, p0: Activity, p1: JSONArray, p2: Continuation) -> Any: ...
    def openDestinationActivity(self, p0: Activity, p1: JSONArray, p2: Continuation) -> Any: ...
    def addExternalForegroundLifecycleListener(self, p0: INotificationLifecycleListener) -> None: ...
    def removeExternalForegroundLifecycleListener(self, p0: INotificationLifecycleListener) -> None: ...
    def addExternalClickListener(self, p0: INotificationClickListener) -> None: ...
    def removeExternalClickListener(self, p0: INotificationClickListener) -> None: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...


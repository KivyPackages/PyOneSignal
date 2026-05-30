from typing import Any, ClassVar, overload
from android.content.Context import Context

class NavigateToAndroidSettingsForNotifications:
    INSTANCE: ClassVar["NavigateToAndroidSettingsForNotifications"]
    def show(self, p0: Context) -> None: ...

from typing import Any, ClassVar, overload
from notifications.internal.permissions.INotificationPermissionChangedHandler import INotificationPermissionChangedHandler
from pyonesignal.core.internal.application.IApplicationService import IApplicationService
from pyonesignal.core.internal.config.ConfigModelStore import ConfigModelStore
from pyonesignal.core.internal.permissions.IRequestPermissionService import IRequestPermissionService
from pyonesignal.core.internal.preferences.IPreferencesService import IPreferencesService
from pyonesignal.core.threading.Waiter import Waiter

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

class NotificationPermissionController:
    Companion: ClassVar[Any]
    def __init__(self, p0: IApplicationService, p1: IRequestPermissionService, p2: IApplicationService, p3: IPreferencesService, p4: ConfigModelStore) -> None: ...
    @overload
    def subscribe(self, p0: Any) -> None: ...
    @overload
    def subscribe(self, p0: INotificationPermissionChangedHandler) -> None: ...
    def getCanRequestPermission(self) -> bool: ...
    @overload
    def unsubscribe(self, p0: Any) -> None: ...
    @overload
    def unsubscribe(self, p0: INotificationPermissionChangedHandler) -> None: ...
    def getSupportsNativePrompt(self) -> bool: ...
    def onAccept(self) -> None: ...
    def onReject(self, p0: bool) -> None: ...
    @staticmethod
    def access$setPollingWaitInterval$p(p0: "NotificationPermissionController", p1: int) -> None: ...
    @staticmethod
    def access$get_configModelStore$p(p0: "NotificationPermissionController") -> ConfigModelStore: ...
    @staticmethod
    def access$getPollingWaiter$p(p0: "NotificationPermissionController") -> Waiter: ...
    @staticmethod
    def access$pollForPermission(p0: "NotificationPermissionController", p1: Continuation) -> Any: ...
    @staticmethod
    def access$permissionPromptCompleted(p0: "NotificationPermissionController", p1: bool) -> None: ...
    def prompt(self, p0: bool, p1: Continuation) -> Any: ...
    def getHasSubscribers(self) -> bool: ...
    @staticmethod
    def access$get_applicationService$p(p0: "NotificationPermissionController") -> IApplicationService: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...


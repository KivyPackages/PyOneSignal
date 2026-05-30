from typing import Any, ClassVar, overload
from notifications.INotificationClickListener import INotificationClickListener
from notifications.INotificationLifecycleListener import INotificationLifecycleListener
from notifications.IPermissionObserver import IPermissionObserver

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Void:
    """Forward declaration for ``java.lang.Void``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.Void')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html
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
class DefaultConstructorMarker:
    """Forward declaration for ``kotlin.jvm.internal.DefaultConstructorMarker``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.internal.DefaultConstructorMarker')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/internal/DefaultConstructorMarker/
    """
    ...
class Exception:
    """Forward declaration for ``java.lang.Exception``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.Exception')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/Exception.html
    """
    ...

class MisconfiguredNotificationsManager:
    Companion: ClassVar[Any]
    def __init__(self) -> None: ...
    @overload
    def getCanRequestPermission(self) -> Void: ...
    @overload
    def getCanRequestPermission(self) -> bool: ...
    def requestPermission(self, p0: bool, p1: Continuation) -> Any: ...
    @overload
    def removeNotification(self, p0: int) -> Void: ...
    @overload
    def removeNotification(self, p0: int) -> None: ...
    @overload
    def removeGroupedNotifications(self, p0: str) -> None: ...
    @overload
    def removeGroupedNotifications(self, p0: str) -> Void: ...
    @overload
    def clearAllNotifications(self) -> None: ...
    @overload
    def clearAllNotifications(self) -> Void: ...
    @overload
    def addPermissionObserver(self, p0: IPermissionObserver) -> None: ...
    @overload
    def addPermissionObserver(self, p0: IPermissionObserver) -> Void: ...
    @overload
    def removePermissionObserver(self, p0: IPermissionObserver) -> None: ...
    @overload
    def removePermissionObserver(self, p0: IPermissionObserver) -> Void: ...
    @overload
    def addForegroundLifecycleListener(self, p0: INotificationLifecycleListener) -> None: ...
    @overload
    def addForegroundLifecycleListener(self, p0: INotificationLifecycleListener) -> Void: ...
    @overload
    def removeForegroundLifecycleListener(self, p0: INotificationLifecycleListener) -> None: ...
    @overload
    def removeForegroundLifecycleListener(self, p0: INotificationLifecycleListener) -> Void: ...
    @overload
    def addClickListener(self, p0: INotificationClickListener) -> Void: ...
    @overload
    def addClickListener(self, p0: INotificationClickListener) -> None: ...
    @overload
    def removeClickListener(self, p0: INotificationClickListener) -> Void: ...
    @overload
    def removeClickListener(self, p0: INotificationClickListener) -> None: ...
    @overload
    def getPermission(self) -> bool: ...
    @overload
    def getPermission(self) -> Void: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...
        @staticmethod
        def access$getEXCEPTION(p0: Any) -> Exception: ...


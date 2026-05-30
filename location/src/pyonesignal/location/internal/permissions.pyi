from typing import Any, ClassVar, overload

class ILocationPermissionChangedHandler:
    def onLocationPermissionChanged(self, p0: bool) -> None: ...

from typing import Any, ClassVar, overload
from internal.permissions.ILocationPermissionChangedHandler import ILocationPermissionChangedHandler
from pyonesignal.core.events.EventProducer import EventProducer
from pyonesignal.core.internal.application.IApplicationService import IApplicationService
from pyonesignal.core.internal.permissions.IRequestPermissionService import IRequestPermissionService
from pyonesignal.core.threading.WaiterWithValue import WaiterWithValue

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

class LocationPermissionController:
    Companion: ClassVar[Any]
    def __init__(self, p0: IRequestPermissionService, p1: IApplicationService) -> None: ...
    def start(self) -> None: ...
    @overload
    def subscribe(self, p0: ILocationPermissionChangedHandler) -> None: ...
    @overload
    def subscribe(self, p0: Any) -> None: ...
    def prompt(self, p0: bool, p1: str, p2: Continuation) -> Any: ...
    @staticmethod
    def access$get_applicationService$p(p0: "LocationPermissionController") -> IApplicationService: ...
    def onAccept(self) -> None: ...
    def onReject(self, p0: bool) -> None: ...
    @staticmethod
    def access$getCurrPermission$p(p0: "LocationPermissionController") -> str: ...
    @staticmethod
    def access$getWaiter$p(p0: "LocationPermissionController") -> WaiterWithValue: ...
    @staticmethod
    def access$getEvents$p(p0: "LocationPermissionController") -> EventProducer: ...
    def getHasSubscribers(self) -> bool: ...
    @overload
    def unsubscribe(self, p0: ILocationPermissionChangedHandler) -> None: ...
    @overload
    def unsubscribe(self, p0: Any) -> None: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context

class NavigateToAndroidSettingsForLocation:
    INSTANCE: ClassVar["NavigateToAndroidSettingsForLocation"]
    def show(self, p0: Context) -> None: ...


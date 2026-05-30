from typing import Any, ClassVar, overload
from internal.capture.ILocationCapturer import ILocationCapturer
from internal.preferences.ILocationPreferencesService import ILocationPreferencesService
from pyonesignal.core.internal.application.IApplicationService import IApplicationService
from pyonesignal.core.internal.time.ITime import ITime

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class ILocationManager:
    """Forward declaration for ``com.onesignal.location.ILocationManager``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.location.ILocationManager')`` proxy; this empty class exists
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

class LocationBackgroundService:
    def __init__(self, p0: IApplicationService, p1: ILocationManager, p2: ILocationPreferencesService, p3: ILocationCapturer, p4: ITime) -> None: ...
    def getScheduleBackgroundRunIn(self) -> int: ...
    def backgroundRun(self, p0: Continuation) -> Any: ...


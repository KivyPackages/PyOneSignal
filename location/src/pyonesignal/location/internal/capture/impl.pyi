from typing import Any, ClassVar, overload
from android.location.Location import Location
from internal.controller.ILocationController import ILocationController
from internal.preferences.ILocationPreferencesService import ILocationPreferencesService
from pyonesignal.core.internal.application.IApplicationService import IApplicationService
from pyonesignal.core.internal.time.ITime import ITime

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class PropertiesModelStore:
    """Forward declaration for ``com.onesignal.user.internal.properties.PropertiesModelStore``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.user.internal.properties.PropertiesModelStore')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class LocationCapturer:
    def __init__(self, p0: IApplicationService, p1: ITime, p2: ILocationPreferencesService, p3: PropertiesModelStore, p4: ILocationController) -> None: ...
    def getLocationCoarse(self) -> bool: ...
    def setLocationCoarse(self, p0: bool) -> None: ...
    def captureLastLocation(self) -> None: ...
    def onLocationChanged(self, p0: Location) -> None: ...


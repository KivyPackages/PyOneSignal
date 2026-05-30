from typing import Any, ClassVar, overload
from android.location.Location import Location

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class GoogleApiClient:
    """Forward declaration for ``com.google.android.gms.common.api.GoogleApiClient``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.google.android.gms.common.api.GoogleApiClient')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developers.google.com/android/reference/com/google/android/gms/common/api/GoogleApiClient
    """
    ...
class LocationListener:
    """Forward declaration for ``com.google.android.gms.location.LocationListener``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.google.android.gms.location.LocationListener')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developers.google.com/android/reference/com/google/android/gms/location/LocationListener
    """
    ...
class LocationRequest:
    """Forward declaration for ``com.google.android.gms.location.LocationRequest``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.google.android.gms.location.LocationRequest')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest
    """
    ...

class FusedLocationApiWrapperImpl:
    def __init__(self) -> None: ...
    def getLastLocation(self, p0: GoogleApiClient) -> Location: ...
    def cancelLocationUpdates(self, p0: GoogleApiClient, p1: LocationListener) -> None: ...
    def requestLocationUpdates(self, p0: GoogleApiClient, p1: LocationRequest, p2: LocationListener) -> None: ...

from typing import Any, ClassVar, overload
from android.location.Location import Location
from internal.controller.ILocationUpdatedHandler import ILocationUpdatedHandler
from internal.controller.impl.GoogleApiClientCompatProxy import GoogleApiClientCompatProxy
from internal.controller.impl.IFusedLocationApiWrapper import IFusedLocationApiWrapper
from pyonesignal.core.events.EventProducer import EventProducer
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
class Mutex:
    """Forward declaration for ``kotlinx.coroutines.sync.Mutex``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlinx.coroutines.sync.Mutex')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlinx/coroutines/sync/Mutex/
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
class GoogleApiClient:
    """Forward declaration for ``com.google.android.gms.common.api.GoogleApiClient``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.google.android.gms.common.api.GoogleApiClient')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developers.google.com/android/reference/com/google/android/gms/common/api/GoogleApiClient
    """
    ...

class GmsLocationController:
    Companion: ClassVar[Any]
    def __init__(self, p0: IApplicationService, p1: IFusedLocationApiWrapper) -> None: ...
    def start(self, p0: Continuation) -> Any: ...
    def stop(self, p0: Continuation) -> Any: ...
    @overload
    def subscribe(self, p0: Any) -> None: ...
    @overload
    def subscribe(self, p0: ILocationUpdatedHandler) -> None: ...
    @staticmethod
    def access$get_applicationService$p(p0: "GmsLocationController") -> IApplicationService: ...
    def getLastLocation(self) -> Location: ...
    def getHasSubscribers(self) -> bool: ...
    @overload
    def unsubscribe(self, p0: ILocationUpdatedHandler) -> None: ...
    @overload
    def unsubscribe(self, p0: Any) -> None: ...
    @staticmethod
    def access$getStartStopMutex$p(p0: "GmsLocationController") -> Mutex: ...
    @staticmethod
    def access$getGoogleApiClient$p(p0: "GmsLocationController") -> GoogleApiClientCompatProxy: ...
    @staticmethod
    def access$getLastLocation$p(p0: "GmsLocationController") -> Location: ...
    @staticmethod
    def access$getEvent$p(p0: "GmsLocationController") -> EventProducer: ...
    @staticmethod
    def access$setLocationAndFire(p0: "GmsLocationController", p1: Location) -> None: ...
    @staticmethod
    def access$getLocationHandlerThread$p(p0: "GmsLocationController") -> Any: ...
    @staticmethod
    def access$get_fusedLocationApiWrapper$p(p0: "GmsLocationController") -> IFusedLocationApiWrapper: ...
    @staticmethod
    def access$setLocationUpdateListener$p(p0: "GmsLocationController", p1: Any) -> None: ...
    @staticmethod
    def access$setGoogleApiClient$p(p0: "GmsLocationController", p1: GoogleApiClientCompatProxy) -> None: ...
    @staticmethod
    def access$getAPI_FALLBACK_TIME$cp() -> int: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...
        def getAPI_FALLBACK_TIME(self) -> int: ...

    class LocationUpdateListener:
        def __init__(self, p0: IApplicationService, p1: "GmsLocationController", p2: GoogleApiClient, p3: IFusedLocationApiWrapper) -> None: ...
        def onFocus(self, p0: bool) -> None: ...
        def onUnfocused(self) -> None: ...
        def close(self) -> None: ...
        def onLocationChanged(self, p0: Location) -> None: ...

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class GoogleApiClient:
    """Forward declaration for ``com.google.android.gms.common.api.GoogleApiClient``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.google.android.gms.common.api.GoogleApiClient')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developers.google.com/android/reference/com/google/android/gms/common/api/GoogleApiClient
    """
    ...
class ConnectionResult:
    """Forward declaration for ``com.google.android.gms.common.ConnectionResult``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.google.android.gms.common.ConnectionResult')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developers.google.com/android/reference/com/google/android/gms/common/ConnectionResult
    """
    ...

class GoogleApiClientCompatProxy:
    def __init__(self, p0: GoogleApiClient) -> None: ...
    def connect(self) -> None: ...
    def blockingConnect(self) -> ConnectionResult: ...
    def disconnect(self) -> None: ...
    def getRealInstance(self) -> GoogleApiClient: ...

from typing import Any, ClassVar, overload
from android.location.Location import Location
from android.os.Handler import Handler
from internal.controller.ILocationUpdatedHandler import ILocationUpdatedHandler
from pyonesignal.core.events.EventProducer import EventProducer
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
class Mutex:
    """Forward declaration for ``kotlinx.coroutines.sync.Mutex``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlinx.coroutines.sync.Mutex')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlinx/coroutines/sync/Mutex/
    """
    ...
class FusedLocationProviderClient:
    """Forward declaration for ``com.huawei.hms.location.FusedLocationProviderClient``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.huawei.hms.location.FusedLocationProviderClient')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...
class LocationResult:
    """Forward declaration for ``com.huawei.hms.location.LocationResult``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.huawei.hms.location.LocationResult')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class HmsLocationController:
    def __init__(self, p0: IApplicationService) -> None: ...
    def start(self, p0: Continuation) -> Any: ...
    def stop(self, p0: Continuation) -> Any: ...
    @overload
    def subscribe(self, p0: ILocationUpdatedHandler) -> None: ...
    @overload
    def subscribe(self, p0: Any) -> None: ...
    @staticmethod
    def access$get_applicationService$p(p0: "HmsLocationController") -> IApplicationService: ...
    def getLastLocation(self) -> Location: ...
    def getHasSubscribers(self) -> bool: ...
    @overload
    def unsubscribe(self, p0: ILocationUpdatedHandler) -> None: ...
    @overload
    def unsubscribe(self, p0: Any) -> None: ...
    @staticmethod
    def access$getStartStopMutex$p(p0: "HmsLocationController") -> Mutex: ...
    @staticmethod
    def access$getLastLocation$p(p0: "HmsLocationController") -> Location: ...
    @staticmethod
    def access$getEvent$p(p0: "HmsLocationController") -> EventProducer: ...
    @staticmethod
    def access$getLocationHandlerThread$p(p0: "HmsLocationController") -> Any: ...
    @staticmethod
    def access$setLocationUpdateListener$p(p0: "HmsLocationController", p1: Any) -> None: ...
    @staticmethod
    def access$setLastLocation$p(p0: "HmsLocationController", p1: Location) -> None: ...
    @staticmethod
    def access$getHmsFusedLocationClient$p(p0: "HmsLocationController") -> FusedLocationProviderClient: ...
    @staticmethod
    def access$setHmsFusedLocationClient$p(p0: "HmsLocationController", p1: FusedLocationProviderClient) -> None: ...

    class LocationHandlerThread:
        MIN_PRIORITY: ClassVar[int]
        NORM_PRIORITY: ClassVar[int]
        MAX_PRIORITY: ClassVar[int]
        def __init__(self) -> None: ...
        def getMHandler(self) -> Handler: ...
        def setMHandler(self, p0: Handler) -> None: ...

    class LocationUpdateListener:
        def __init__(self, p0: "HmsLocationController", p1: IApplicationService, p2: FusedLocationProviderClient) -> None: ...
        def onFocus(self, p0: bool) -> None: ...
        def onUnfocused(self) -> None: ...
        def close(self) -> None: ...
        def onLocationResult(self, p0: LocationResult) -> None: ...

from typing import Any, ClassVar, overload
from android.location.Location import Location

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class GoogleApiClient:
    """Forward declaration for ``com.google.android.gms.common.api.GoogleApiClient``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.google.android.gms.common.api.GoogleApiClient')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developers.google.com/android/reference/com/google/android/gms/common/api/GoogleApiClient
    """
    ...
class LocationListener:
    """Forward declaration for ``com.google.android.gms.location.LocationListener``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.google.android.gms.location.LocationListener')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developers.google.com/android/reference/com/google/android/gms/location/LocationListener
    """
    ...
class LocationRequest:
    """Forward declaration for ``com.google.android.gms.location.LocationRequest``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.google.android.gms.location.LocationRequest')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest
    """
    ...

class IFusedLocationApiWrapper:
    def getLastLocation(self, p0: GoogleApiClient) -> Location: ...
    def cancelLocationUpdates(self, p0: GoogleApiClient, p1: LocationListener) -> None: ...
    def requestLocationUpdates(self, p0: GoogleApiClient, p1: LocationRequest, p2: LocationListener) -> None: ...

from typing import Any, ClassVar, overload
from android.location.Location import Location
from internal.controller.ILocationUpdatedHandler import ILocationUpdatedHandler

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

class NullLocationController:
    def __init__(self) -> None: ...
    def start(self, p0: Continuation) -> Any: ...
    def stop(self, p0: Continuation) -> Any: ...
    @overload
    def subscribe(self, p0: Any) -> None: ...
    @overload
    def subscribe(self, p0: ILocationUpdatedHandler) -> None: ...
    def getLastLocation(self) -> Location: ...
    def getHasSubscribers(self) -> bool: ...
    @overload
    def unsubscribe(self, p0: Any) -> None: ...
    @overload
    def unsubscribe(self, p0: ILocationUpdatedHandler) -> None: ...


from typing import Any, ClassVar, overload
from internal.hydrators.InAppHydrator import InAppHydrator
from pyonesignal.core.consistency.RywData import RywData
from pyonesignal.core.internal.device.IDeviceService import IDeviceService
from pyonesignal.core.internal.http.IHttpClient import IHttpClient

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
class Function0:
    """Forward declaration for ``kotlin.jvm.functions.Function0``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.functions.Function0')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/functions/Function0/
    """
    ...

class InAppBackendService:
    def __init__(self, p0: IHttpClient, p1: IDeviceService, p2: InAppHydrator) -> None: ...
    def getIAMData(self, p0: str, p1: str, p2: str, p3: Continuation) -> Any: ...
    def getIAMPreviewData(self, p0: str, p1: str, p2: Continuation) -> Any: ...
    def sendIAMImpression(self, p0: str, p1: str, p2: str, p3: str, p4: Continuation) -> Any: ...
    @staticmethod
    def access$get_deviceService$p(p0: "InAppBackendService") -> IDeviceService: ...
    @staticmethod
    def access$attemptFetchWithRetries(p0: "InAppBackendService", p1: str, p2: RywData, p3: Function0, p4: str, p5: Continuation) -> Any: ...
    @staticmethod
    def access$fetchInAppMessagesWithoutRywToken(p0: "InAppBackendService", p1: str, p2: Function0, p3: str, p4: Continuation) -> Any: ...
    def listInAppMessages(self, p0: str, p1: str, p2: RywData, p3: Function0, p4: Continuation) -> Any: ...
    def listInAppMessagesIv(self, p0: str, p1: str, p2: str, p3: str, p4: RywData, p5: Function0, p6: str, p7: Continuation) -> Any: ...
    def sendIAMPageImpression(self, p0: str, p1: str, p2: str, p3: str, p4: str, p5: Continuation) -> Any: ...
    def sendIAMClick(self, p0: str, p1: str, p2: str, p3: str, p4: str, p5: bool, p6: Continuation) -> Any: ...

from typing import Any, ClassVar, overload

class InAppBackendServiceKt:
    ...


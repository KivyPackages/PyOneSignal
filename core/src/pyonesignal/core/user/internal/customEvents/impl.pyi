from typing import Any, ClassVar, overload
from core.internal.http.IHttpClient import IHttpClient
from user.internal.customEvents.impl.CustomEventMetadata import CustomEventMetadata

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

class CustomEventBackendService:
    def __init__(self, p0: IHttpClient) -> None: ...
    def sendCustomEvent(self, p0: str, p1: str, p2: str, p3: int, p4: str, p5: str, p6: CustomEventMetadata, p7: str, p8: Continuation) -> Any: ...

from typing import Any, ClassVar, overload
from core.internal.config.ConfigModelStore import ConfigModelStore
from core.internal.operations.IOperationRepo import IOperationRepo
from core.internal.time.ITime import ITime
from user.internal.identity.IdentityModelStore import IdentityModelStore

class CustomEventController:
    def __init__(self, p0: IdentityModelStore, p1: ConfigModelStore, p2: ITime, p3: IOperationRepo) -> None: ...
    def sendCustomEvent(self, p0: str, p1: dict) -> None: ...

from typing import Any, ClassVar, overload

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
class DefaultConstructorMarker:
    """Forward declaration for ``kotlin.jvm.internal.DefaultConstructorMarker``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.internal.DefaultConstructorMarker')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/internal/DefaultConstructorMarker/
    """
    ...

class CustomEventMetadata:
    Companion: ClassVar[Any]
    def __init__(self, p0: str, p1: str, p2: str, p3: str, p4: str, p5: str) -> None: ...
    def toString(self) -> str: ...
    def getType(self) -> str: ...
    def toJSONObject(self) -> JSONObject: ...
    def getAppVersion(self) -> str: ...
    def getDeviceModel(self) -> str: ...
    def getDeviceType(self) -> str: ...
    def getSdk(self) -> str: ...
    def getDeviceOS(self) -> str: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...


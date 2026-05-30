from typing import Any, ClassVar, overload

class CacheKeys:
    INSTANCE: ClassVar["CacheKeys"]
    GET_TAGS: ClassVar[str]
    REMOTE_PARAMS: ClassVar[str]

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Throwable:
    """Forward declaration for ``java.lang.Throwable``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.Throwable')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html
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

class HttpResponse:
    @overload
    def __init__(self, p0: int, p1: str, p2: Throwable, p3: int, p4: int, p5: int, p6: DefaultConstructorMarker) -> None: ...
    @overload
    def __init__(self, p0: int, p1: str, p2: Throwable, p3: int, p4: int) -> None: ...
    def getThrowable(self) -> Throwable: ...
    def isSuccess(self) -> bool: ...
    def isClientError(self) -> bool: ...
    def getPayload(self) -> str: ...
    def getStatusCode(self) -> int: ...
    def getRetryAfterSeconds(self) -> int: ...
    def getRetryLimit(self) -> int: ...

from typing import Any, ClassVar, overload
from core.internal.http.impl.OptionalHeaders import OptionalHeaders

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

class IHttpClient:
    def patch(self, p0: str, p1: JSONObject, p2: OptionalHeaders, p3: Continuation) -> Any: ...
    def get(self, p0: str, p1: OptionalHeaders, p2: Continuation) -> Any: ...
    def put(self, p0: str, p1: JSONObject, p2: OptionalHeaders, p3: Continuation) -> Any: ...
    def delete(self, p0: str, p1: OptionalHeaders, p2: Continuation) -> Any: ...
    def post(self, p0: str, p1: JSONObject, p2: OptionalHeaders, p3: Continuation) -> Any: ...

    class DefaultImpls:
        @staticmethod
        def put$default(p0: "IHttpClient", p1: str, p2: JSONObject, p3: OptionalHeaders, p4: Continuation, p5: int, p6: Any) -> Any: ...
        @staticmethod
        def patch$default(p0: "IHttpClient", p1: str, p2: JSONObject, p3: OptionalHeaders, p4: Continuation, p5: int, p6: Any) -> Any: ...
        @staticmethod
        def post$default(p0: "IHttpClient", p1: str, p2: JSONObject, p3: OptionalHeaders, p4: Continuation, p5: int, p6: Any) -> Any: ...
        @staticmethod
        def delete$default(p0: "IHttpClient", p1: str, p2: OptionalHeaders, p3: Continuation, p4: int, p5: Any) -> Any: ...
        @staticmethod
        def get$default(p0: "IHttpClient", p1: str, p2: OptionalHeaders, p3: Continuation, p4: int, p5: Any) -> Any: ...

from typing import Any, ClassVar, overload

class OneSignalService:
    INSTANCE: ClassVar["OneSignalService"]
    ONESIGNAL_API_BASE_URL: ClassVar[str]


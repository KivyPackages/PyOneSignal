from typing import Any, ClassVar, overload
from core.internal.config.ConfigModelStore import ConfigModelStore
from core.internal.device.IInstallIdService import IInstallIdService
from core.internal.http.impl.IHttpConnectionFactory import IHttpConnectionFactory
from core.internal.http.impl.OptionalHeaders import OptionalHeaders
from core.internal.preferences.IPreferencesService import IPreferencesService
from core.internal.time.ITime import ITime

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
class URL:
    """Forward declaration for ``java.net.URL``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.net.URL')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/net/URL.html
    """
    ...
class HttpURLConnection:
    """Forward declaration for ``java.net.HttpURLConnection``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.net.HttpURLConnection')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/net/HttpURLConnection.html
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

class HttpClient:
    Companion: ClassVar[Any]
    def __init__(self, p0: IHttpConnectionFactory, p1: IPreferencesService, p2: ConfigModelStore, p3: ITime, p4: IInstallIdService) -> None: ...
    def patch(self, p0: str, p1: JSONObject, p2: OptionalHeaders, p3: Continuation) -> Any: ...
    def get(self, p0: str, p1: OptionalHeaders, p2: Continuation) -> Any: ...
    def put(self, p0: str, p1: JSONObject, p2: OptionalHeaders, p3: Continuation) -> Any: ...
    def delete(self, p0: str, p1: OptionalHeaders, p2: Continuation) -> Any: ...
    def post(self, p0: str, p1: JSONObject, p2: OptionalHeaders, p3: Continuation) -> Any: ...
    @staticmethod
    def access$get_prefs$p(p0: "HttpClient") -> IPreferencesService: ...
    @staticmethod
    def access$makeRequest(p0: "HttpClient", p1: str, p2: str, p3: JSONObject, p4: int, p5: OptionalHeaders, p6: Continuation) -> Any: ...
    @staticmethod
    def access$makeRequestIODispatcher(p0: "HttpClient", p1: str, p2: str, p3: JSONObject, p4: int, p5: OptionalHeaders, p6: Continuation) -> Any: ...
    @staticmethod
    def access$get_connectionFactory$p(p0: "HttpClient") -> IHttpConnectionFactory: ...
    @staticmethod
    def access$get_installIdService$p(p0: "HttpClient") -> IInstallIdService: ...
    @staticmethod
    def access$logHTTPSent(p0: "HttpClient", p1: str, p2: URL, p3: JSONObject, p4: dict) -> None: ...
    @staticmethod
    def access$retryAfterFromResponse(p0: "HttpClient", p1: HttpURLConnection) -> int: ...
    @staticmethod
    def access$retryLimitFromResponse(p0: "HttpClient", p1: HttpURLConnection) -> int: ...
    @staticmethod
    def access$get_time$p(p0: "HttpClient") -> ITime: ...
    @staticmethod
    def access$getDelayNewRequestsUntil$p(p0: "HttpClient") -> int: ...
    @staticmethod
    def access$setDelayNewRequestsUntil$p(p0: "HttpClient", p1: int) -> None: ...
    @staticmethod
    def access$get_configModelStore$p(p0: "HttpClient") -> ConfigModelStore: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

from typing import Any, ClassVar, overload

class HttpClientKt:
    HTTP_SDK_VERSION_HEADER_KEY: ClassVar[str]
    @staticmethod
    def getHTTP_SDK_VERSION_HEADER_VALUE() -> str: ...

from typing import Any, ClassVar, overload
from core.internal.config.ConfigModelStore import ConfigModelStore

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class HttpURLConnection:
    """Forward declaration for ``java.net.HttpURLConnection``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.net.HttpURLConnection')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/net/HttpURLConnection.html
    """
    ...

class HttpConnectionFactory:
    def __init__(self, p0: ConfigModelStore) -> None: ...
    def newHttpURLConnection(self, p0: str) -> HttpURLConnection: ...

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class HttpURLConnection:
    """Forward declaration for ``java.net.HttpURLConnection``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.net.HttpURLConnection')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/net/HttpURLConnection.html
    """
    ...

class IHttpConnectionFactory:
    def newHttpURLConnection(self, p0: str) -> HttpURLConnection: ...

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class DefaultConstructorMarker:
    """Forward declaration for ``kotlin.jvm.internal.DefaultConstructorMarker``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.internal.DefaultConstructorMarker')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/internal/DefaultConstructorMarker/
    """
    ...

class OptionalHeaders:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: str, p1: str, p2: int, p3: int, p4: str, p5: int, p6: DefaultConstructorMarker) -> None: ...
    @overload
    def __init__(self, p0: str, p1: str, p2: int, p3: int, p4: str) -> None: ...
    @staticmethod
    def copy$default(p0: "OptionalHeaders", p1: str, p2: str, p3: int, p4: int, p5: str, p6: int, p7: Any) -> "OptionalHeaders": ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def copy(self, p0: str, p1: str, p2: int, p3: int, p4: str) -> "OptionalHeaders": ...
    def component1(self) -> str: ...
    def component2(self) -> str: ...
    def getRetryCount(self) -> int: ...
    def getSessionDuration(self) -> int: ...
    def getCacheKey(self) -> str: ...
    def getJwt(self) -> str: ...
    def component3(self) -> int: ...
    def component4(self) -> int: ...
    def component5(self) -> str: ...
    def getRywToken(self) -> str: ...

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class SSLSocketFactory:
    """Forward declaration for ``javax.net.ssl.SSLSocketFactory``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('javax.net.ssl.SSLSocketFactory')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/javax/net/ssl/SSLSocketFactory.html
    """
    ...
class InetAddress:
    """Forward declaration for ``java.net.InetAddress``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.net.InetAddress')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/net/InetAddress.html
    """
    ...
class Socket:
    """Forward declaration for ``java.net.Socket``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.net.Socket')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/net/Socket.html
    """
    ...

class TLS12SocketFactory:
    def __init__(self, p0: SSLSocketFactory) -> None: ...
    def getSslSocketFactory(self) -> SSLSocketFactory: ...
    def setSslSocketFactory(self, p0: SSLSocketFactory) -> None: ...
    def getDefaultCipherSuites(self) -> Any: ...
    def getSupportedCipherSuites(self) -> Any: ...
    @overload
    def createSocket(self, p0: InetAddress, p1: int, p2: InetAddress, p3: int) -> Socket: ...
    @overload
    def createSocket(self, p0: InetAddress, p1: int) -> Socket: ...
    @overload
    def createSocket(self, p0: str, p1: int, p2: InetAddress, p3: int) -> Socket: ...
    @overload
    def createSocket(self) -> Socket: ...
    @overload
    def createSocket(self, p0: Socket, p1: str, p2: int, p3: bool) -> Socket: ...
    @overload
    def createSocket(self, p0: str, p1: int) -> Socket: ...


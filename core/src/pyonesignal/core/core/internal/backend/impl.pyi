from typing import Any, ClassVar, overload
from core.internal.http.IHttpClient import IHttpClient

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

class FeatureFlagsBackendService:
    Companion: ClassVar[Any]
    TURBINE_FEATURES_PLATFORM_ANDROID: ClassVar[str]
    def __init__(self, p0: IHttpClient) -> None: ...
    def fetchRemoteFeatureFlags(self, p0: str, p1: Continuation) -> Any: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...
        def isValidFeaturesSdkVersionLabel(self, p0: str) -> bool: ...
        def buildFeatureFlagsGetPath$com_onesignal_core(self, p0: str, p1: str, p2: str) -> str: ...

from typing import Any, ClassVar, overload
from core.internal.backend.RemoteFeatureFlagsResult import RemoteFeatureFlagsResult

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Json:
    """Forward declaration for ``kotlinx.serialization.json.Json``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlinx.serialization.json.Json')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlinx/serialization/json/Json/
    """
    ...
class JsonObject:
    """Forward declaration for ``kotlinx.serialization.json.JsonObject``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlinx.serialization.json.JsonObject')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlinx/serialization/json/JsonObject/
    """
    ...

class FeatureFlagsJsonParser:
    INSTANCE: ClassVar["FeatureFlagsJsonParser"]
    def parse(self, p0: str) -> RemoteFeatureFlagsResult: ...
    def parseSuccessful(self, p0: str) -> RemoteFeatureFlagsResult: ...
    def getFormat(self) -> Json: ...
    def encodeMetadata(self, p0: JsonObject) -> str: ...
    def parseStoredMetadataMap(self, p0: str) -> dict: ...

from typing import Any, ClassVar, overload
from core.internal.backend.InfluenceParamsObject import InfluenceParamsObject
from core.internal.http.IHttpClient import IHttpClient

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
class JSONObject:
    """Forward declaration for ``org.json.JSONObject``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONObject')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class ParamsBackendService:
    def __init__(self, p0: IHttpClient) -> None: ...
    def fetchParams(self, p0: str, p1: str, p2: Continuation) -> Any: ...
    @staticmethod
    def access$processOutcomeJson(p0: "ParamsBackendService", p1: JSONObject) -> InfluenceParamsObject: ...

from typing import Any, ClassVar, overload

class TurbineSdkFeatureFlagsPath:
    INSTANCE: ClassVar["TurbineSdkFeatureFlagsPath"]
    def percentEncodePathSegmentUtf8$com_onesignal_core(self, p0: str) -> str: ...
    def buildGetPath(self, p0: str, p1: str, p2: str) -> str: ...
    def isValidFeaturesSdkVersionLabel(self, p0: str) -> bool: ...


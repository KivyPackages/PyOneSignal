from typing import Any, ClassVar, overload
from android.app.Activity import Activity
from android.content.Context import Context
from android.content.Intent import Intent
from android.net.Uri import Uri
from android.os.Bundle import Bundle
from core.internal.application.IApplicationService import IApplicationService

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
class EnumEntries:
    """Forward declaration for ``kotlin.enums.EnumEntries``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.enums.EnumEntries')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/enums/EnumEntries/
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

class AndroidUtils:
    INSTANCE: ClassVar["AndroidUtils"]
    def getManifestMetaBoolean(self, p0: Context, p1: str) -> bool: ...
    def getTargetSdkVersion(self, p0: Context) -> int: ...
    def getRandomDelay(self, p0: int, p1: int) -> int: ...
    def isStringNotEmpty(self, p0: str) -> bool: ...
    def isActivityFullyReady(self, p0: Activity) -> bool: ...
    def isAndroidUserUnlocked(self, p0: Context) -> bool: ...
    def hasConfigChangeFlag(self, p0: Activity, p1: int) -> bool: ...
    def getAppVersion(self, p0: Context) -> str: ...
    def getAndroidSDKInt(self) -> int: ...
    def getManifestMeta(self, p0: Context, p1: str) -> str: ...
    def getManifestMetaBundle(self, p0: Context) -> Bundle: ...
    def getResourceString(self, p0: Context, p1: str, p2: str) -> str: ...
    def isValidResourceName(self, p0: str) -> bool: ...
    def getRootCauseThrowable(self, p0: Throwable) -> Throwable: ...
    def getRootCauseMessage(self, p0: Throwable) -> str: ...
    def isRunningOnMainThread(self) -> bool: ...
    def hasNotificationManagerCompat(self) -> bool: ...
    @overload
    def openURLInBrowser(self, p0: Context, p1: Uri) -> None: ...
    @overload
    def openURLInBrowser(self, p0: Context, p1: str) -> None: ...
    def openURLInBrowserIntent(self, p0: Uri) -> Intent: ...
    def hasPermission(self, p0: str, p1: bool, p2: IApplicationService) -> bool: ...
    def filterManifestPermissions(self, p0: list, p1: IApplicationService) -> list: ...
    def opaqueHasClass(self, p0: type) -> bool: ...
    def finishSafely(self, p0: Activity) -> None: ...

    class SchemaType:
        DATA: ClassVar["SchemaType"]
        HTTPS: ClassVar["SchemaType"]
        HTTP: ClassVar["SchemaType"]
        Companion: ClassVar[Any]
        DATA: ClassVar[Any]
        HTTPS: ClassVar[Any]
        HTTP: ClassVar[Any]
        @staticmethod
        def getEntries() -> EnumEntries: ...
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
        @staticmethod
        def access$getText$p(p0: Any) -> str: ...

        class Companion:
            def __init__(self, p0: DefaultConstructorMarker) -> None: ...
            def fromString(self, p0: str) -> Any: ...

    class WhenMappings:
        $EnumSwitchMapping$0: ClassVar[Any]

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class SimpleDateFormat:
    """Forward declaration for ``java.text.SimpleDateFormat``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.text.SimpleDateFormat')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/text/SimpleDateFormat.html
    """
    ...

class DateUtils:
    INSTANCE: ClassVar["DateUtils"]
    def iso8601Format(self) -> SimpleDateFormat: ...

from typing import Any, ClassVar, overload

class IDManager:
    INSTANCE: ClassVar["IDManager"]
    LOCAL_PREFIX: ClassVar[str]
    def createLocalId(self) -> str: ...
    def isLocalId(self, p0: str) -> bool: ...

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
class Function1:
    """Forward declaration for ``kotlin.jvm.functions.Function1``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.functions.Function1')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/functions/Function1/
    """
    ...
class JSONArray:
    """Forward declaration for ``org.json.JSONArray``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONArray')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class JSONObjectExtensionsKt:
    @staticmethod
    def safeInt(p0: JSONObject, p1: str) -> int: ...
    @overload
    @staticmethod
    def putMap(p0: JSONObject, p1: dict) -> JSONObject: ...
    @overload
    @staticmethod
    def putMap(p0: JSONObject, p1: str, p2: dict) -> JSONObject: ...
    @staticmethod
    def safeLong(p0: JSONObject, p1: str) -> int: ...
    @staticmethod
    def safeDouble(p0: JSONObject, p1: str) -> float: ...
    @staticmethod
    def safeBool(p0: JSONObject, p1: str) -> bool: ...
    @staticmethod
    def safeString(p0: JSONObject, p1: str) -> str: ...
    @staticmethod
    def safeJSONObject(p0: JSONObject, p1: str) -> JSONObject: ...
    @staticmethod
    def expandJSONObject(p0: JSONObject, p1: str, p2: Function1) -> None: ...
    @staticmethod
    def expandJSONArray(p0: JSONObject, p1: str, p2: Function1) -> list: ...
    @staticmethod
    def putJSONObject(p0: JSONObject, p1: str, p2: Function1) -> JSONObject: ...
    @staticmethod
    def putJSONArray(p0: JSONObject, p1: str, p2: list, p3: Function1) -> JSONObject: ...
    @staticmethod
    def putSafe(p0: JSONObject, p1: str, p2: Any) -> JSONObject: ...
    @staticmethod
    def toList(p0: JSONArray) -> list: ...
    @staticmethod
    def toMap(p0: JSONObject) -> dict: ...

from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle

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
class JSONArray:
    """Forward declaration for ``org.json.JSONArray``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONArray')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class JSONUtils:
    INSTANCE: ClassVar["JSONUtils"]
    EXTERNAL_USER_ID: ClassVar[str]
    def wrapInJsonArray(self, p0: JSONObject) -> JSONArray: ...
    def bundleAsJSONObject(self, p0: Bundle) -> JSONObject: ...
    def jsonStringToBundle(self, p0: str) -> Bundle: ...
    def newStringMapFromJSONObject(self, p0: JSONObject) -> dict: ...
    def newStringSetFromJSONArray(self, p0: JSONArray) -> set: ...
    def toUnescapedEUIDString(self, p0: JSONObject) -> str: ...
    def compareJSONArrays(self, p0: JSONArray, p1: JSONArray) -> bool: ...
    def normalizeType(self, p0: Any) -> Any: ...
    def isValidJsonObject(self, p0: Any) -> bool: ...
    def mapToJson(self, p0: dict) -> JSONObject: ...
    def convertToJson(self, p0: Any) -> Any: ...

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class EnumEntries:
    """Forward declaration for ``kotlin.enums.EnumEntries``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.enums.EnumEntries')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/enums/EnumEntries/
    """
    ...

class NetworkUtils:
    INSTANCE: ClassVar["NetworkUtils"]
    def getResponseStatusType(self, p0: int) -> Any: ...
    def getMaxNetworkRequestAttemptCount(self) -> int: ...
    def setMaxNetworkRequestAttemptCount(self, p0: int) -> None: ...

    class ResponseStatusType:
        INVALID: ClassVar["ResponseStatusType"]
        RETRYABLE: ClassVar["ResponseStatusType"]
        UNAUTHORIZED: ClassVar["ResponseStatusType"]
        MISSING: ClassVar["ResponseStatusType"]
        CONFLICT: ClassVar["ResponseStatusType"]
        INVALID: ClassVar[Any]
        RETRYABLE: ClassVar[Any]
        UNAUTHORIZED: ClassVar[Any]
        MISSING: ClassVar[Any]
        CONFLICT: ClassVar[Any]
        @staticmethod
        def getEntries() -> EnumEntries: ...
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

from typing import Any, ClassVar, overload

class OneSignalUtils:
    INSTANCE: ClassVar["OneSignalUtils"]
    def getSdkVersion(self) -> str: ...
    def formatVersion$com_onesignal_core(self, p0: str) -> str: ...
    def isValidEmail(self, p0: str) -> bool: ...
    def isValidPhoneNumber(self, p0: str) -> bool: ...

from typing import Any, ClassVar, overload

class OneSignalWrapper:
    INSTANCE: ClassVar["OneSignalWrapper"]
    @staticmethod
    def getSdkVersion() -> str: ...
    @staticmethod
    def getSdkType$annotations() -> None: ...
    @staticmethod
    def getSdkType() -> str: ...
    @staticmethod
    def setSdkType(p0: str) -> None: ...
    @staticmethod
    def setSdkVersion(p0: str) -> None: ...
    @staticmethod
    def getSdkVersion$annotations() -> None: ...

from typing import Any, ClassVar, overload

class PIIHasher:
    INSTANCE: ClassVar["PIIHasher"]
    def isHashed(self, p0: str) -> bool: ...
    def hash(self, p0: str) -> str: ...

from typing import Any, ClassVar, overload

class RootToolsInternalMethods:
    INSTANCE: ClassVar["RootToolsInternalMethods"]
    def isRooted(self) -> bool: ...

from typing import Any, ClassVar, overload

class TimeUtils:
    INSTANCE: ClassVar["TimeUtils"]
    def getTimeZoneOffset(self) -> int: ...
    def getTimeZoneId(self) -> str: ...

from typing import Any, ClassVar, overload
from android.app.Activity import Activity

class ViewUtils:
    INSTANCE: ClassVar["ViewUtils"]
    def dpToPx(self, p0: int) -> int: ...
    def getWindowHeight(self, p0: Activity) -> int: ...
    def getCutoutAndStatusBarInsets(self, p0: Activity) -> Any: ...
    def getFullbleedWindowWidth(self, p0: Activity) -> int: ...
    def getWindowWidth(self, p0: Activity) -> int: ...


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

class IDeviceService:
    def isFireOSDeviceType(self) -> bool: ...
    def isAndroidDeviceType(self) -> bool: ...
    def isHuaweiDeviceType(self) -> bool: ...
    def getHasAllHMSLibrariesForPushKit(self) -> bool: ...
    def getHasFCMLibrary(self) -> bool: ...
    def getJetpackLibraryStatus(self) -> Any: ...
    def getSupportsHMS(self) -> bool: ...
    def supportsGooglePush(self) -> bool: ...
    def getDeviceType(self) -> Any: ...
    def isGMSInstalledAndEnabled(self) -> bool: ...

    class DeviceType:
        Fire: ClassVar["DeviceType"]
        Android: ClassVar["DeviceType"]
        Huawei: ClassVar["DeviceType"]
        Fire: ClassVar[Any]
        Android: ClassVar[Any]
        Huawei: ClassVar[Any]
        @staticmethod
        def getEntries() -> EnumEntries: ...
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
        def getValue(self) -> int: ...

    class JetpackLibraryStatus:
        MISSING: ClassVar["JetpackLibraryStatus"]
        OUTDATED: ClassVar["JetpackLibraryStatus"]
        OK: ClassVar["JetpackLibraryStatus"]
        MISSING: ClassVar[Any]
        OUTDATED: ClassVar[Any]
        OK: ClassVar[Any]
        @staticmethod
        def getEntries() -> EnumEntries: ...
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

from typing import Any, ClassVar, overload

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

class IInstallIdService:
    def getId(self, p0: Continuation) -> Any: ...


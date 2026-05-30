from typing import Any, ClassVar, overload
from core.internal.application.IApplicationService import IApplicationService

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

class DeviceService:
    Companion: ClassVar[Any]
    def __init__(self, p0: IApplicationService) -> None: ...
    def isGMSInstalledAndEnabled(self) -> bool: ...
    def isAndroidDeviceType(self) -> bool: ...
    def isFireOSDeviceType(self) -> bool: ...
    def isHuaweiDeviceType(self) -> bool: ...
    def getDeviceType(self) -> Any: ...
    def getHasAllHMSLibrariesForPushKit(self) -> bool: ...
    def getHasFCMLibrary(self) -> bool: ...
    def getJetpackLibraryStatus(self) -> Any: ...
    def getSupportsHMS(self) -> bool: ...
    def supportsGooglePush(self) -> bool: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

from typing import Any, ClassVar, overload
from core.internal.preferences.IPreferencesService import IPreferencesService

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

class InstallIdService:
    def __init__(self, p0: IPreferencesService) -> None: ...
    def getId(self, p0: Continuation) -> Any: ...
    @staticmethod
    def access$get_prefs$p(p0: "InstallIdService") -> IPreferencesService: ...


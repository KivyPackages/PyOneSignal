from typing import Any, ClassVar, overload
from android.app.Activity import Activity

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Function0:
    """Forward declaration for ``kotlin.jvm.functions.Function0``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.functions.Function0')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/functions/Function0/
    """
    ...

class AlertDialogPrepromptForAndroidSettings:
    INSTANCE: ClassVar["AlertDialogPrepromptForAndroidSettings"]
    @overload
    def show(self, p0: Activity, p1: str, p2: str, p3: Any) -> None: ...
    @overload
    def show(self, p0: Activity, p1: str, p2: str, p3: Any, p4: Function0) -> None: ...
    def dismissCurrentDialog(self) -> None: ...

    class Callback:
        def onDecline(self) -> None: ...
        def onAccept(self) -> None: ...

from typing import Any, ClassVar, overload

class IRequestPermissionService:
    def startPrompt(self, p0: bool, p1: str, p2: str, p3: type) -> None: ...
    def registerAsCallback(self, p0: str, p1: Any) -> None: ...

    class PermissionCallback:
        def onAccept(self) -> None: ...
        def onReject(self, p0: bool) -> None: ...

from typing import Any, ClassVar, overload
from android.app.Activity import Activity
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
class StateFlow:
    """Forward declaration for ``kotlinx.coroutines.flow.StateFlow``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlinx.coroutines.flow.StateFlow')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlinx/coroutines/flow/StateFlow/
    """
    ...
class MutableStateFlow:
    """Forward declaration for ``kotlinx.coroutines.flow.MutableStateFlow``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlinx.coroutines.flow.MutableStateFlow')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlinx/coroutines/flow/MutableStateFlow/
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

class PermissionsViewModel:
    Companion: ClassVar[Any]
    DELAY_TIME_CALLBACK_CALL: ClassVar[int]
    ONESIGNAL_PERMISSION_REQUEST_CODE: ClassVar[int]
    INTENT_EXTRA_PERMISSION_TYPE: ClassVar[str]
    INTENT_EXTRA_ANDROID_PERMISSION_STRING: ClassVar[str]
    INTENT_EXTRA_CALLBACK_CLASS: ClassVar[str]
    def __init__(self) -> None: ...
    def initialize(self, p0: Activity, p1: str, p2: str, p3: Continuation) -> Any: ...
    def onRequestPermissionsResult(self, p0: Any, p1: Any, p2: bool) -> None: ...
    def getShouldFinish(self) -> StateFlow: ...
    def getWaiting(self) -> StateFlow: ...
    def getPermissionRequestType(self) -> str: ...
    @staticmethod
    def onRequestPermissionsResult$default(p0: "PermissionsViewModel", p1: Any, p2: Any, p3: bool, p4: int, p5: Any) -> None: ...
    @staticmethod
    def access$getPreferenceService(p0: "PermissionsViewModel") -> IPreferencesService: ...
    @staticmethod
    def access$shouldShowSettings(p0: "PermissionsViewModel", p1: str, p2: bool) -> bool: ...
    @staticmethod
    def access$executeCallback(p0: "PermissionsViewModel", p1: bool, p2: bool) -> None: ...
    @staticmethod
    def access$get_shouldFinish$p(p0: "PermissionsViewModel") -> MutableStateFlow: ...
    def resetWaitingState(self) -> None: ...
    def shouldRequestPermission(self) -> bool: ...
    def recordRationaleState(self, p0: bool) -> None: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...


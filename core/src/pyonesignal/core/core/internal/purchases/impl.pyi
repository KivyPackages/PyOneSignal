from typing import Any, ClassVar, overload
from android.content.Context import Context
from core.internal.application.IApplicationService import IApplicationService
from core.internal.config.ConfigModelStore import ConfigModelStore
from core.internal.operations.IOperationRepo import IOperationRepo
from core.internal.preferences.IPreferencesService import IPreferencesService
from user.internal.identity.IdentityModelStore import IdentityModelStore

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
class Method:
    """Forward declaration for ``java.lang.reflect.Method``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.reflect.Method')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/Method.html
    """
    ...

class TrackGooglePurchase:
    Companion: ClassVar[Any]
    def __init__(self, p0: IApplicationService, p1: IPreferencesService, p2: IOperationRepo, p3: ConfigModelStore, p4: IdentityModelStore) -> None: ...
    def start(self) -> None: ...
    @staticmethod
    def access$setIapEnabled$cp(p0: int) -> None: ...
    @staticmethod
    def access$setMIInAppBillingService$p(p0: "TrackGooglePurchase", p1: Any) -> None: ...
    @staticmethod
    def access$queryBoughtItems(p0: "TrackGooglePurchase") -> None: ...
    @staticmethod
    def access$getIapEnabled$cp() -> int: ...
    @staticmethod
    def access$setIInAppBillingServiceClass$cp(p0: type) -> None: ...
    def onFocus(self, p0: bool) -> None: ...
    def onUnfocused(self) -> None: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...
        def canTrack(self, p0: Context) -> bool: ...
        @staticmethod
        def access$getGetSkuDetailsMethod(p0: Any, p1: type) -> Method: ...
        @staticmethod
        def access$getGetPurchasesMethod(p0: Any, p1: type) -> Method: ...
        @staticmethod
        def access$getAsInterfaceMethod(p0: Any, p1: type) -> Method: ...


from typing import Any, ClassVar, overload
from internal.InAppMessage import InAppMessage
from internal.preferences.IInAppPreferencesController import IInAppPreferencesController
from pyonesignal.core.internal.database.IDatabaseProvider import IDatabaseProvider
from pyonesignal.core.internal.time.ITime import ITime

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

class InAppRepository:
    Companion: ClassVar[Any]
    IAM_CACHE_DATA_LIFETIME: ClassVar[int]
    def __init__(self, p0: IDatabaseProvider, p1: ITime, p2: IInAppPreferencesController) -> None: ...
    def cleanCachedInAppMessages(self, p0: Continuation) -> Any: ...
    @staticmethod
    def access$get_databaseProvider$p(p0: "InAppRepository") -> IDatabaseProvider: ...
    def listInAppMessages(self, p0: Continuation) -> Any: ...
    def saveInAppMessage(self, p0: InAppMessage, p1: Continuation) -> Any: ...
    @staticmethod
    def access$get_time$p(p0: "InAppRepository") -> ITime: ...
    @staticmethod
    def access$get_prefs$p(p0: "InAppRepository") -> IInAppPreferencesController: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...


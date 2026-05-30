from typing import Any, ClassVar, overload

class IJwtUpdateListener:
    def onJwtUpdated(self, p0: str) -> None: ...

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
class DefaultConstructorMarker:
    """Forward declaration for ``kotlin.jvm.internal.DefaultConstructorMarker``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.internal.DefaultConstructorMarker')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/internal/DefaultConstructorMarker/
    """
    ...

class JwtRequirement:
    UNKNOWN: ClassVar["JwtRequirement"]
    NOT_REQUIRED: ClassVar["JwtRequirement"]
    REQUIRED: ClassVar["JwtRequirement"]
    Companion: ClassVar[Any]
    UNKNOWN: ClassVar["JwtRequirement"]
    NOT_REQUIRED: ClassVar["JwtRequirement"]
    REQUIRED: ClassVar["JwtRequirement"]
    @staticmethod
    def getEntries() -> EnumEntries: ...
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "JwtRequirement": ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...
        def fromBoolean(self, p0: bool) -> "JwtRequirement": ...

from typing import Any, ClassVar, overload
from IUserJwtInvalidatedListener import IUserJwtInvalidatedListener
from common.events.EventProducer import EventProducer
from core.internal.preferences.IPreferencesService import IPreferencesService
from user.internal.jwt.IJwtUpdateListener import IJwtUpdateListener

class JwtTokenStore:
    def __init__(self, p0: IPreferencesService) -> None: ...
    def addInternalUpdateListener(self, p0: IJwtUpdateListener) -> None: ...
    def addUserJwtInvalidatedListener(self, p0: IUserJwtInvalidatedListener) -> None: ...
    def removeUserJwtInvalidatedListener(self, p0: IUserJwtInvalidatedListener) -> None: ...
    @staticmethod
    def access$getPublicInvalidatedListeners$p(p0: "JwtTokenStore") -> EventProducer: ...
    def removeInternalUpdateListener(self, p0: IJwtUpdateListener) -> None: ...
    def putJwt(self, p0: str, p1: str) -> None: ...
    def invalidateJwt(self, p0: str) -> None: ...
    def pruneToExternalIds(self, p0: set) -> None: ...
    def getJwt(self, p0: str) -> str: ...


from typing import Any, ClassVar, overload
from debug.ILogListener import ILogListener
from debug.LogLevel import LogLevel

class IDebugManager:
    def getLogLevel(self) -> LogLevel: ...
    def setLogLevel(self, p0: LogLevel) -> None: ...
    def getAlertLevel(self) -> LogLevel: ...
    def setAlertLevel(self, p0: LogLevel) -> None: ...
    def addLogListener(self, p0: ILogListener) -> None: ...
    def removeLogListener(self, p0: ILogListener) -> None: ...

from typing import Any, ClassVar, overload
from debug.OneSignalLogEvent import OneSignalLogEvent

class ILogListener:
    def onLogEvent(self, p0: OneSignalLogEvent) -> None: ...

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

class LogLevel:
    NONE: ClassVar["LogLevel"]
    FATAL: ClassVar["LogLevel"]
    ERROR: ClassVar["LogLevel"]
    WARN: ClassVar["LogLevel"]
    INFO: ClassVar["LogLevel"]
    DEBUG: ClassVar["LogLevel"]
    VERBOSE: ClassVar["LogLevel"]
    Companion: ClassVar[Any]
    NONE: ClassVar["LogLevel"]
    FATAL: ClassVar["LogLevel"]
    ERROR: ClassVar["LogLevel"]
    WARN: ClassVar["LogLevel"]
    INFO: ClassVar["LogLevel"]
    DEBUG: ClassVar["LogLevel"]
    VERBOSE: ClassVar["LogLevel"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "LogLevel": ...
    @staticmethod
    def fromInt(p0: int) -> "LogLevel": ...
    @staticmethod
    def getEntries() -> EnumEntries: ...
    @staticmethod
    def fromString(p0: str) -> "LogLevel": ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...
        def fromInt(self, p0: int) -> "LogLevel": ...
        def fromString(self, p0: str) -> "LogLevel": ...

from typing import Any, ClassVar, overload
from debug.LogLevel import LogLevel

class OneSignalLogEvent:
    def __init__(self, p0: LogLevel, p1: str) -> None: ...
    @staticmethod
    def copy$default(p0: "OneSignalLogEvent", p1: LogLevel, p2: str, p3: int, p4: Any) -> "OneSignalLogEvent": ...
    def getEntry(self) -> str: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def copy(self, p0: LogLevel, p1: str) -> "OneSignalLogEvent": ...
    def component1(self) -> LogLevel: ...
    def component2(self) -> str: ...
    def getLevel(self) -> LogLevel: ...


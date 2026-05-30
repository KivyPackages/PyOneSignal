from typing import Any, ClassVar, overload

class IInfluenceManager:
    def onNotificationReceived(self, p0: str) -> None: ...
    def onInAppMessageDisplayed(self, p0: str) -> None: ...
    def onDirectInfluenceFromIAM(self, p0: str) -> None: ...
    def getInfluences(self) -> list: ...
    def onDirectInfluenceFromNotification(self, p0: str) -> None: ...
    def onInAppMessageDismissed(self) -> None: ...

from typing import Any, ClassVar, overload
from session.internal.influence.InfluenceChannel import InfluenceChannel
from session.internal.influence.InfluenceType import InfluenceType

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class JSONArray:
    """Forward declaration for ``org.json.JSONArray``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONArray')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
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

class Influence:
    Companion: ClassVar[Any]
    INFLUENCE_CHANNEL: ClassVar[str]
    INFLUENCE_TYPE: ClassVar[str]
    INFLUENCE_IDS: ClassVar[str]
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: InfluenceChannel, p1: InfluenceType, p2: JSONArray) -> None: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def copy(self) -> "Influence": ...
    def setIds(self, p0: JSONArray) -> None: ...
    def getInfluenceType(self) -> InfluenceType: ...
    def getIds(self) -> JSONArray: ...
    def setInfluenceType(self, p0: InfluenceType) -> None: ...
    def getInfluenceChannel(self) -> InfluenceChannel: ...
    def getDirectId(self) -> str: ...
    def toJSONString(self) -> str: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

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

class InfluenceChannel:
    IAM: ClassVar["InfluenceChannel"]
    NOTIFICATION: ClassVar["InfluenceChannel"]
    Companion: ClassVar[Any]
    IAM: ClassVar["InfluenceChannel"]
    NOTIFICATION: ClassVar["InfluenceChannel"]
    def toString(self) -> str: ...
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "InfluenceChannel": ...
    def equalsName(self, p0: str) -> bool: ...
    @staticmethod
    def getEntries() -> EnumEntries: ...
    @staticmethod
    def fromString(p0: str) -> "InfluenceChannel": ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...
        def fromString(self, p0: str) -> "InfluenceChannel": ...

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

class InfluenceType:
    DIRECT: ClassVar["InfluenceType"]
    INDIRECT: ClassVar["InfluenceType"]
    UNATTRIBUTED: ClassVar["InfluenceType"]
    DISABLED: ClassVar["InfluenceType"]
    Companion: ClassVar[Any]
    DIRECT: ClassVar["InfluenceType"]
    INDIRECT: ClassVar["InfluenceType"]
    UNATTRIBUTED: ClassVar["InfluenceType"]
    DISABLED: ClassVar["InfluenceType"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "InfluenceType": ...
    def isDirect(self) -> bool: ...
    def isAttributed(self) -> bool: ...
    def isIndirect(self) -> bool: ...
    def isUnattributed(self) -> bool: ...
    def isDisabled(self) -> bool: ...
    @staticmethod
    def getEntries() -> EnumEntries: ...
    @staticmethod
    def fromString(p0: str) -> "InfluenceType": ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...
        def fromString(self, p0: str) -> "InfluenceType": ...


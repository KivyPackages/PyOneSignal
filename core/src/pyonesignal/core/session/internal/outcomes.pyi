from typing import Any, ClassVar, overload
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

class IOutcomeEvent:
    def getTimestamp(self) -> int: ...
    def getName(self) -> str: ...
    def getSession(self) -> InfluenceType: ...
    def getWeight(self) -> float: ...
    def getNotificationIds(self) -> JSONArray: ...
    def getSessionTime(self) -> int: ...

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

class IOutcomeEventsController:
    def sendUniqueOutcomeEvent(self, p0: str, p1: Continuation) -> Any: ...
    def sendSessionEndOutcomeEvent(self, p0: int, p1: Continuation) -> Any: ...
    def sendOutcomeEvent(self, p0: str, p1: Continuation) -> Any: ...
    def sendOutcomeEventWithValue(self, p0: str, p1: float, p2: Continuation) -> Any: ...


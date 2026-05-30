from typing import Any, ClassVar, overload
from common.consistency.RywData import RywData

class ICondition:
    def getId(self) -> str: ...
    def isMet(self, p0: dict) -> bool: ...
    def getRywData(self, p0: dict) -> RywData: ...

from typing import Any, ClassVar, overload

class IConsistencyKeyEnum:
    ...

from typing import Any, ClassVar, overload
from common.consistency.RywData import RywData
from common.consistency.models.ICondition import ICondition
from common.consistency.models.IConsistencyKeyEnum import IConsistencyKeyEnum

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

class IConsistencyManager:
    def setRywData(self, p0: str, p1: IConsistencyKeyEnum, p2: RywData, p3: Continuation) -> Any: ...
    def getRywDataFromAwaitableCondition(self, p0: ICondition, p1: Continuation) -> Any: ...
    def resolveConditionsWithID(self, p0: str, p1: Continuation) -> Any: ...


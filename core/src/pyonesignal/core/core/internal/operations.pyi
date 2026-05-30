from typing import Any, ClassVar, overload
from core.internal.operations.ExecutionResult import ExecutionResult

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

class ExecutionResponse:
    @overload
    def __init__(self, p0: ExecutionResult, p1: dict, p2: list, p3: int) -> None: ...
    @overload
    def __init__(self, p0: ExecutionResult, p1: dict, p2: list, p3: int, p4: int, p5: DefaultConstructorMarker) -> None: ...
    def getRetryAfterSeconds(self) -> int: ...
    def getOperations(self) -> list: ...
    def getIdTranslations(self) -> dict: ...
    def getResult(self) -> ExecutionResult: ...

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

class ExecutionResult:
    SUCCESS: ClassVar["ExecutionResult"]
    SUCCESS_STARTING_ONLY: ClassVar["ExecutionResult"]
    FAIL_RETRY: ClassVar["ExecutionResult"]
    FAIL_NORETRY: ClassVar["ExecutionResult"]
    FAIL_UNAUTHORIZED: ClassVar["ExecutionResult"]
    FAIL_CONFLICT: ClassVar["ExecutionResult"]
    FAIL_PAUSE_OPREPO: ClassVar["ExecutionResult"]
    SUCCESS: ClassVar["ExecutionResult"]
    SUCCESS_STARTING_ONLY: ClassVar["ExecutionResult"]
    FAIL_RETRY: ClassVar["ExecutionResult"]
    FAIL_NORETRY: ClassVar["ExecutionResult"]
    FAIL_UNAUTHORIZED: ClassVar["ExecutionResult"]
    FAIL_CONFLICT: ClassVar["ExecutionResult"]
    FAIL_PAUSE_OPREPO: ClassVar["ExecutionResult"]
    @staticmethod
    def getEntries() -> EnumEntries: ...
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "ExecutionResult": ...

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

class GroupComparisonType:
    CREATE: ClassVar["GroupComparisonType"]
    ALTER: ClassVar["GroupComparisonType"]
    NONE: ClassVar["GroupComparisonType"]
    CREATE: ClassVar["GroupComparisonType"]
    ALTER: ClassVar["GroupComparisonType"]
    NONE: ClassVar["GroupComparisonType"]
    @staticmethod
    def getEntries() -> EnumEntries: ...
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "GroupComparisonType": ...

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

class IOperationExecutor:
    def execute(self, p0: list, p1: Continuation) -> Any: ...
    def getOperations(self) -> list: ...

from typing import Any, ClassVar, overload
from core.internal.operations.Operation import Operation

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
class KClass:
    """Forward declaration for ``kotlin.reflect.KClass``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.reflect.KClass')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/reflect/KClass/
    """
    ...

class IOperationRepo:
    def enqueue(self, p0: Operation, p1: bool) -> None: ...
    def enqueueAndWait(self, p0: Operation, p1: bool, p2: Continuation) -> Any: ...
    def containsInstanceOf(self, p0: KClass) -> bool: ...
    def awaitInitialized(self, p0: Continuation) -> Any: ...
    def forceExecuteOperations(self) -> None: ...

    class DefaultImpls:
        @staticmethod
        def enqueue$default(p0: "IOperationRepo", p1: Operation, p2: bool, p3: int, p4: Any) -> None: ...
        @staticmethod
        def enqueueAndWait$default(p0: "IOperationRepo", p1: Operation, p2: bool, p3: Continuation, p4: int, p5: Any) -> Any: ...

from typing import Any, ClassVar, overload
from core.internal.operations.IOperationRepo import IOperationRepo

class IOperationRepoKt:
    @staticmethod
    def containsInstanceOf(p0: IOperationRepo) -> bool: ...

from typing import Any, ClassVar, overload
from core.internal.operations.GroupComparisonType import GroupComparisonType

class Operation:
    def __init__(self, p0: str) -> None: ...
    def getExternalId(self) -> str: ...
    def getName(self) -> str: ...
    def toString(self) -> str: ...
    def getRequiresJwt(self) -> bool: ...
    def setExternalId$com_onesignal_core(self, p0: str) -> None: ...
    def getApplyToRecordId(self) -> str: ...
    def getCreateComparisonKey(self) -> str: ...
    def getModifyComparisonKey(self) -> str: ...
    def getGroupComparisonType(self) -> GroupComparisonType: ...
    def getCanStartExecute(self) -> bool: ...
    def translateIds(self, p0: dict) -> None: ...


from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class CoroutineDispatcher:
    """Forward declaration for ``kotlinx.coroutines.CoroutineDispatcher``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlinx.coroutines.CoroutineDispatcher')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlinx/coroutines/CoroutineDispatcher/
    """
    ...
class Function1:
    """Forward declaration for ``kotlin.jvm.functions.Function1``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.functions.Function1')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/functions/Function1/
    """
    ...
class Job:
    """Forward declaration for ``kotlinx.coroutines.Job``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlinx.coroutines.Job')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlinx/coroutines/Job/
    """
    ...
class Function0:
    """Forward declaration for ``kotlin.jvm.functions.Function0``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.functions.Function0')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/functions/Function0/
    """
    ...
class ThreadPoolExecutor:
    """Forward declaration for ``java.util.concurrent.ThreadPoolExecutor``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.util.concurrent.ThreadPoolExecutor')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ThreadPoolExecutor.html
    """
    ...
class ExecutorService:
    """Forward declaration for ``java.util.concurrent.ExecutorService``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.util.concurrent.ExecutorService')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ExecutorService.html
    """
    ...
class CoroutineScope:
    """Forward declaration for ``kotlinx.coroutines.CoroutineScope``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlinx.coroutines.CoroutineScope')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlinx/coroutines/CoroutineScope/
    """
    ...

class OneSignalDispatchers:
    INSTANCE: ClassVar["OneSignalDispatchers"]
    BASE_THREAD_NAME: ClassVar[str]
    def getDefault(self) -> CoroutineDispatcher: ...
    def getIO(self) -> CoroutineDispatcher: ...
    def getSerialIO(self) -> CoroutineDispatcher: ...
    def launchOnIO(self, p0: Function1) -> Job: ...
    def launchOnDefault(self, p0: Function1) -> Job: ...
    def launchOnSerialIO(self, p0: Function1) -> Job: ...
    def prewarm(self) -> None: ...
    def resetPrewarmForTest$com_onesignal_core(self) -> None: ...
    def getPerformanceMetrics$com_onesignal_core(self) -> str: ...
    def getStatus$com_onesignal_core(self) -> str: ...
    def executorStatus$com_onesignal_core(self, p0: str, p1: Function0) -> str: ...
    def scopeStatus$com_onesignal_core(self, p0: str, p1: Function0) -> str: ...
    @staticmethod
    def access$getIoExecutor(p0: "OneSignalDispatchers") -> ThreadPoolExecutor: ...
    @staticmethod
    def access$getDefaultExecutor(p0: "OneSignalDispatchers") -> ThreadPoolExecutor: ...
    @staticmethod
    def access$getSerialIOExecutor(p0: "OneSignalDispatchers") -> ExecutorService: ...
    @staticmethod
    def access$getIOScope(p0: "OneSignalDispatchers") -> CoroutineScope: ...
    @staticmethod
    def access$getDefaultScope(p0: "OneSignalDispatchers") -> CoroutineScope: ...
    @staticmethod
    def access$getSerialIOScope(p0: "OneSignalDispatchers") -> CoroutineScope: ...

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Function1:
    """Forward declaration for ``kotlin.jvm.functions.Function1``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.functions.Function1')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/functions/Function1/
    """
    ...
class Job:
    """Forward declaration for ``kotlinx.coroutines.Job``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlinx.coroutines.Job')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlinx/coroutines/Job/
    """
    ...
class Function0:
    """Forward declaration for ``kotlin.jvm.functions.Function0``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.functions.Function0')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/functions/Function0/
    """
    ...

class ThreadUtilsKt:
    @staticmethod
    def suspendifyOnMain(p0: Function1) -> None: ...
    @staticmethod
    def launchOnIO(p0: Function1) -> Job: ...
    @staticmethod
    def launchOnDefault(p0: Function1) -> Job: ...
    @overload
    @staticmethod
    def suspendifyOnIO(p0: Function1, p1: Function0) -> None: ...
    @overload
    @staticmethod
    def suspendifyOnIO(p0: Function1) -> None: ...
    @staticmethod
    def suspendifyWithCompletion(p0: bool, p1: Function1, p2: Function0) -> None: ...
    @staticmethod
    def suspendifyOnIO$default(p0: Function1, p1: Function0, p2: int, p3: Any) -> None: ...
    @staticmethod
    def suspendifyOnDefault(p0: Function1) -> None: ...
    @staticmethod
    def suspendifyOnSerialIO(p0: Function1) -> None: ...
    @staticmethod
    def runOnSerialIOIfBackgroundThreading(p0: Function0) -> None: ...
    @staticmethod
    def suspendifyWithCompletion$default(p0: bool, p1: Function1, p2: Function0, p3: int, p4: Any) -> None: ...
    @staticmethod
    def suspendifyWithErrorHandling(p0: bool, p1: Function1, p2: Function1, p3: Function0) -> None: ...
    @staticmethod
    def suspendifyWithErrorHandling$default(p0: bool, p1: Function1, p2: Function1, p3: Function0, p4: int, p5: Any) -> None: ...

from typing import Any, ClassVar, overload

class ThreadingMode:
    INSTANCE: ClassVar["ThreadingMode"]
    def setUseBackgroundThreading(self, p0: bool) -> None: ...
    def updateUseBackgroundThreading(self, p0: bool, p1: str) -> None: ...
    def getUseBackgroundThreading(self) -> bool: ...

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

class Waiter:
    def __init__(self) -> None: ...
    def wake(self) -> None: ...
    def waitForWake(self, p0: Continuation) -> Any: ...

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

class WaiterWithValue:
    def __init__(self) -> None: ...
    def wake(self, p0: Any) -> None: ...
    def waitForWake(self, p0: Continuation) -> Any: ...


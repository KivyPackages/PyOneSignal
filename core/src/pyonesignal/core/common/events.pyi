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
class Function2:
    """Forward declaration for ``kotlin.jvm.functions.Function2``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.functions.Function2')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/functions/Function2/
    """
    ...
class Continuation:
    """Forward declaration for ``kotlin.coroutines.Continuation``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.coroutines.Continuation')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/coroutines/Continuation/
    """
    ...

class CallbackProducer:
    def __init__(self) -> None: ...
    def set(self, p0: Any) -> None: ...
    def fire(self, p0: Function1) -> None: ...
    def getHasCallback(self) -> bool: ...
    def fireOnMain(self, p0: Function1) -> None: ...
    def suspendingFire(self, p0: Function2, p1: Continuation) -> Any: ...
    def suspendingFireOnMain(self, p0: Function2, p1: Continuation) -> Any: ...
    @staticmethod
    def access$getCallback$p(p0: "CallbackProducer") -> Any: ...

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
class Function2:
    """Forward declaration for ``kotlin.jvm.functions.Function2``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.functions.Function2')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/functions/Function2/
    """
    ...
class Continuation:
    """Forward declaration for ``kotlin.coroutines.Continuation``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.coroutines.Continuation')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/coroutines/Continuation/
    """
    ...

class EventProducer:
    def __init__(self) -> None: ...
    def fire(self, p0: Function1) -> None: ...
    def fireOnMain(self, p0: Function1) -> None: ...
    def suspendingFire(self, p0: Function2, p1: Continuation) -> Any: ...
    def suspendingFireOnMain(self, p0: Function2, p1: Continuation) -> Any: ...
    def getHasSubscribers(self) -> bool: ...
    def subscribe(self, p0: Any) -> None: ...
    def unsubscribe(self, p0: Any) -> None: ...
    def subscribeAll(self, p0: "EventProducer") -> None: ...
    @staticmethod
    def access$getSubscribers$p(p0: "EventProducer") -> list: ...

from typing import Any, ClassVar, overload

class ICallbackNotifier:
    def set(self, p0: Any) -> None: ...
    def getHasCallback(self) -> bool: ...

from typing import Any, ClassVar, overload

class IEventNotifier:
    def getHasSubscribers(self) -> bool: ...
    def subscribe(self, p0: Any) -> None: ...
    def unsubscribe(self, p0: Any) -> None: ...


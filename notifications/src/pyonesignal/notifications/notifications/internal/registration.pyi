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
class SubscriptionStatus:
    """Forward declaration for ``com.onesignal.user.internal.subscriptions.SubscriptionStatus``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.user.internal.subscriptions.SubscriptionStatus')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class IPushRegistrator:
    def registerForPush(self, p0: Continuation) -> Any: ...

    class RegisterResult:
        def __init__(self, p0: str, p1: SubscriptionStatus) -> None: ...
        def getId(self) -> str: ...
        def getStatus(self) -> SubscriptionStatus: ...


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

class IPushTokenManager:
    def retrievePushToken(self, p0: Continuation) -> Any: ...

from typing import Any, ClassVar, overload
from notifications.internal.registration.IPushRegistrator import IPushRegistrator
from pyonesignal.core.internal.device.IDeviceService import IDeviceService

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

class PushTokenManager:
    def __init__(self, p0: IPushRegistrator, p1: IDeviceService) -> None: ...
    def retrievePushToken(self, p0: Continuation) -> Any: ...
    def getPushTokenStatus(self) -> SubscriptionStatus: ...
    def setPushTokenStatus(self, p0: SubscriptionStatus) -> None: ...
    def getPushToken(self) -> str: ...
    def setPushToken(self, p0: str) -> None: ...

    class WhenMappings:
        $EnumSwitchMapping$0: ClassVar[Any]

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class SubscriptionStatus:
    """Forward declaration for ``com.onesignal.user.internal.subscriptions.SubscriptionStatus``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.user.internal.subscriptions.SubscriptionStatus')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class PushTokenResponse:
    def __init__(self, p0: str, p1: SubscriptionStatus) -> None: ...
    def getStatus(self) -> SubscriptionStatus: ...
    def getToken(self) -> str: ...


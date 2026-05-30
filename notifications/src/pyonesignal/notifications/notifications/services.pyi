from typing import Any, ClassVar, overload

class ADMMessageHandler:
    def __init__(self) -> None: ...

from typing import Any, ClassVar, overload

class ADMMessageHandlerJob:
    def __init__(self) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class RemoteMessage:
    """Forward declaration for ``com.huawei.hms.push.RemoteMessage``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.huawei.hms.push.RemoteMessage')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class HmsMessageServiceOneSignal:
    def __init__(self) -> None: ...
    @overload
    def onNewToken(self, p0: str) -> None: ...
    @overload
    def onNewToken(self, p0: str, p1: Bundle) -> None: ...
    def onMessageReceived(self, p0: RemoteMessage) -> None: ...


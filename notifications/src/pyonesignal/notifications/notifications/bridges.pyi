from typing import Any, ClassVar, overload
from android.content.Context import Context
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

class OneSignalHmsEventBridge:
    INSTANCE: ClassVar["OneSignalHmsEventBridge"]
    HMS_TTL_KEY: ClassVar[str]
    HMS_SENT_TIME_KEY: ClassVar[str]
    @overload
    def onNewToken(self, p0: Context, p1: str, p2: Bundle) -> None: ...
    @overload
    def onNewToken(self, p0: Context, p1: str) -> None: ...
    def onMessageReceived(self, p0: Context, p1: RemoteMessage) -> None: ...


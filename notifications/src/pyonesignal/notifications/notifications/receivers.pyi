from typing import Any, ClassVar, overload

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

class ADMMessageReceiver:
    Companion: ClassVar[Any]
    def __init__(self) -> None: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.content.Intent import Intent

class BootUpReceiver:
    def __init__(self) -> None: ...
    def onReceive(self, p0: Context, p1: Intent) -> None: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.content.Intent import Intent

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

class FCMBroadcastReceiver:
    Companion: ClassVar[Any]
    def __init__(self) -> None: ...
    def onReceive(self, p0: Context, p1: Intent) -> None: ...
    @staticmethod
    def access$setSuccessfulResultCode(p0: "FCMBroadcastReceiver") -> None: ...
    @staticmethod
    def access$setAbort(p0: "FCMBroadcastReceiver") -> None: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...
        @staticmethod
        def access$isFCMMessage(p0: Any, p1: Intent) -> bool: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.content.Intent import Intent

class NotificationDismissReceiver:
    def __init__(self) -> None: ...
    def onReceive(self, p0: Context, p1: Intent) -> None: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.content.Intent import Intent

class UpgradeReceiver:
    def __init__(self) -> None: ...
    def onReceive(self, p0: Context, p1: Intent) -> None: ...


from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class ILocationManager:
    """Forward declaration for ``com.onesignal.location.ILocationManager``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.location.ILocationManager')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
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

class InAppMessageLocationPrompt:
    def __init__(self, p0: ILocationManager) -> None: ...
    def getPromptKey(self) -> str: ...
    def handlePrompt(self, p0: Continuation) -> Any: ...

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
class EnumEntries:
    """Forward declaration for ``kotlin.enums.EnumEntries``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.enums.EnumEntries')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/enums/EnumEntries/
    """
    ...

class InAppMessagePrompt:
    def __init__(self) -> None: ...
    def getPromptKey(self) -> str: ...
    def toString(self) -> str: ...
    def hasPrompted(self) -> bool: ...
    def setPrompted(self, p0: bool) -> None: ...
    def handlePrompt(self, p0: Continuation) -> Any: ...

    class OSPromptActionCompletionCallback:
        def onCompleted(self, p0: Any) -> None: ...

    class PromptActionResult:
        PERMISSION_GRANTED: ClassVar["PromptActionResult"]
        PERMISSION_DENIED: ClassVar["PromptActionResult"]
        LOCATION_PERMISSIONS_MISSING_MANIFEST: ClassVar["PromptActionResult"]
        ERROR: ClassVar["PromptActionResult"]
        PERMISSION_GRANTED: ClassVar[Any]
        PERMISSION_DENIED: ClassVar[Any]
        LOCATION_PERMISSIONS_MISSING_MANIFEST: ClassVar[Any]
        ERROR: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
        @staticmethod
        def getEntries() -> EnumEntries: ...

from typing import Any, ClassVar, overload
from internal.prompt.impl.InAppMessagePrompt import InAppMessagePrompt

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class INotificationsManager:
    """Forward declaration for ``com.onesignal.notifications.INotificationsManager``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.notifications.INotificationsManager')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...
class ILocationManager:
    """Forward declaration for ``com.onesignal.location.ILocationManager``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.location.ILocationManager')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class InAppMessagePromptFactory:
    def __init__(self, p0: INotificationsManager, p1: ILocationManager) -> None: ...
    def createPrompt(self, p0: str) -> InAppMessagePrompt: ...

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class INotificationsManager:
    """Forward declaration for ``com.onesignal.notifications.INotificationsManager``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.notifications.INotificationsManager')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
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

class InAppMessagePushPrompt:
    def __init__(self, p0: INotificationsManager) -> None: ...
    def getPromptKey(self) -> str: ...
    def handlePrompt(self, p0: Continuation) -> Any: ...


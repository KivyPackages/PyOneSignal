from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.os.Bundle import Bundle
from notifications.internal.generation.INotificationGenerationWorkManager import INotificationGenerationWorkManager
from pyonesignal.core.internal.time.ITime import ITime

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

class NotificationBundleProcessor:
    Companion: ClassVar[Any]
    PUSH_ADDITIONAL_DATA_KEY: ClassVar[str]
    PUSH_MINIFIED_BUTTONS_LIST: ClassVar[str]
    PUSH_MINIFIED_BUTTON_ID: ClassVar[str]
    PUSH_MINIFIED_BUTTON_TEXT: ClassVar[str]
    PUSH_MINIFIED_BUTTON_ICON: ClassVar[str]
    DEFAULT_ACTION: ClassVar[str]
    def __init__(self, p0: INotificationGenerationWorkManager, p1: ITime) -> None: ...
    def processBundleFromReceiver(self, p0: Context, p1: Bundle) -> Any: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...


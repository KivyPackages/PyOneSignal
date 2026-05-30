from typing import Any, ClassVar, overload
from notifications.internal.common.NotificationGenerationJob import NotificationGenerationJob
from pyonesignal.core.internal.application.IApplicationService import IApplicationService
from pyonesignal.core.internal.language.ILanguageContext import ILanguageContext

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class JSONArray:
    """Forward declaration for ``org.json.JSONArray``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONArray')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...
class DefaultConstructorMarker:
    """Forward declaration for ``kotlin.jvm.internal.DefaultConstructorMarker``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.internal.DefaultConstructorMarker')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/internal/DefaultConstructorMarker/
    """
    ...

class NotificationChannelManager:
    Companion: ClassVar[Any]
    def __init__(self, p0: IApplicationService, p1: ILanguageContext) -> None: ...
    def processChannelList(self, p0: JSONArray) -> None: ...
    def createNotificationChannel(self, p0: NotificationGenerationJob) -> str: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...


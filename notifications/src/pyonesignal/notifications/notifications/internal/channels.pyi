from typing import Any, ClassVar, overload
from notifications.internal.common.NotificationGenerationJob import NotificationGenerationJob

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

class INotificationChannelManager:
    def processChannelList(self, p0: JSONArray) -> None: ...
    def createNotificationChannel(self, p0: NotificationGenerationJob) -> str: ...


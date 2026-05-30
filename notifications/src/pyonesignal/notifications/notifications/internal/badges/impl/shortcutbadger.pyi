from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Context import Context

class Badger:
    def executeBadge(self, p0: Context, p1: ComponentName, p2: int) -> None: ...
    def getSupportLaunchers(self) -> list: ...

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Exception:
    """Forward declaration for ``java.lang.Exception``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.Exception')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/Exception.html
    """
    ...

class ShortcutBadgeException:
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: str, p1: Exception) -> None: ...

from typing import Any, ClassVar, overload
from android.app.Notification import Notification
from android.content.Context import Context

class ShortcutBadger:
    @staticmethod
    def applyCountOrThrow(p0: Context, p1: int) -> None: ...
    @staticmethod
    def applyCount(p0: Context, p1: int) -> bool: ...
    @staticmethod
    def removeCount(p0: Context) -> bool: ...
    @staticmethod
    def removeCountOrThrow(p0: Context) -> None: ...
    @staticmethod
    def isBadgeCounterSupported(p0: Context) -> bool: ...
    @staticmethod
    def applyNotification(p0: Context, p1: Notification, p2: int) -> None: ...


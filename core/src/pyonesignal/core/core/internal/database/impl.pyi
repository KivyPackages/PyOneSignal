from typing import Any, ClassVar, overload
from android.database.Cursor import Cursor

class DatabaseCursor:
    def __init__(self, p0: Cursor) -> None: ...
    def getString(self, p0: str) -> str: ...
    def getInt(self, p0: str) -> int: ...
    def getLong(self, p0: str) -> int: ...
    def getFloat(self, p0: str) -> float: ...
    def getCount(self) -> int: ...
    def moveToNext(self) -> bool: ...
    def getOptString(self, p0: str) -> str: ...
    def moveToFirst(self) -> bool: ...
    def getOptFloat(self, p0: str) -> float: ...
    def getOptLong(self, p0: str) -> int: ...
    def getOptInt(self, p0: str) -> int: ...

from typing import Any, ClassVar, overload
from core.internal.application.IApplicationService import IApplicationService
from core.internal.database.IDatabase import IDatabase

class DatabaseProvider:
    def __init__(self, p0: IApplicationService) -> None: ...
    def getOs(self) -> IDatabase: ...

from typing import Any, ClassVar, overload
from android.content.ContentValues import ContentValues
from android.content.Context import Context
from android.database.sqlite.SQLiteDatabase import SQLiteDatabase
from session.internal.outcomes.impl.OutcomeTableProvider import OutcomeTableProvider

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
class Function1:
    """Forward declaration for ``kotlin.jvm.functions.Function1``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.functions.Function1')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/functions/Function1/
    """
    ...

class OSDatabase:
    Companion: ClassVar[Any]
    DEFAULT_TTL_IF_NOT_IN_PAYLOAD: ClassVar[int]
    @overload
    def __init__(self, p0: OutcomeTableProvider, p1: Context, p2: int) -> None: ...
    @overload
    def __init__(self, p0: OutcomeTableProvider, p1: Context, p2: int, p3: int, p4: DefaultConstructorMarker) -> None: ...
    def onCreate(self, p0: SQLiteDatabase) -> None: ...
    def query(self, p0: str, p1: Any, p2: str, p3: Any, p4: str, p5: str, p6: str, p7: str, p8: Function1) -> None: ...
    def update(self, p0: str, p1: ContentValues, p2: str, p3: Any) -> int: ...
    def insert(self, p0: str, p1: str, p2: ContentValues) -> None: ...
    def delete(self, p0: str, p1: str, p2: Any) -> None: ...
    def insertOrThrow(self, p0: str, p1: str, p2: ContentValues) -> None: ...
    def onUpgrade(self, p0: SQLiteDatabase, p1: int, p2: int) -> None: ...
    def onDowngrade(self, p0: SQLiteDatabase, p1: int, p2: int) -> None: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

from typing import Any, ClassVar, overload

class OneSignalDbContract:
    def __init__(self) -> None: ...

    class InAppMessageTable:
        INSTANCE: ClassVar[Any]
        TABLE_NAME: ClassVar[str]
        COLUMN_NAME_MESSAGE_ID: ClassVar[str]
        COLUMN_NAME_DISPLAY_QUANTITY: ClassVar[str]
        COLUMN_NAME_LAST_DISPLAY: ClassVar[str]
        COLUMN_CLICK_IDS: ClassVar[str]
        COLUMN_DISPLAYED_IN_SESSION: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]

    class NotificationTable:
        INSTANCE: ClassVar[Any]
        TABLE_NAME: ClassVar[str]
        COLUMN_NAME_NOTIFICATION_ID: ClassVar[str]
        COLUMN_NAME_ANDROID_NOTIFICATION_ID: ClassVar[str]
        COLUMN_NAME_GROUP_ID: ClassVar[str]
        COLUMN_NAME_COLLAPSE_ID: ClassVar[str]
        COLUMN_NAME_IS_SUMMARY: ClassVar[str]
        COLUMN_NAME_OPENED: ClassVar[str]
        COLUMN_NAME_DISMISSED: ClassVar[str]
        COLUMN_NAME_TITLE: ClassVar[str]
        COLUMN_NAME_MESSAGE: ClassVar[str]
        COLUMN_NAME_CREATED_TIME: ClassVar[str]
        COLUMN_NAME_EXPIRE_TIME: ClassVar[str]
        COLUMN_NAME_FULL_DATA: ClassVar[str]
        INDEX_CREATE_NOTIFICATION_ID: ClassVar[str]
        INDEX_CREATE_ANDROID_NOTIFICATION_ID: ClassVar[str]
        INDEX_CREATE_GROUP_ID: ClassVar[str]
        INDEX_CREATE_COLLAPSE_ID: ClassVar[str]
        INDEX_CREATE_CREATED_TIME: ClassVar[str]
        INDEX_CREATE_EXPIRE_TIME: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]


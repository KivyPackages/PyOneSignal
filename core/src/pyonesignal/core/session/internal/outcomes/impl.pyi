from typing import Any, ClassVar, overload
from session.internal.influence.InfluenceChannel import InfluenceChannel

class CachedUniqueOutcome:
    def __init__(self, p0: str, p1: InfluenceChannel) -> None: ...
    def getInfluenceId(self) -> str: ...
    def getChannel(self) -> InfluenceChannel: ...

from typing import Any, ClassVar, overload

class CachedUniqueOutcomeTable:
    INSTANCE: ClassVar["CachedUniqueOutcomeTable"]
    ID: ClassVar[str]
    TABLE_NAME_V2: ClassVar[str]
    TABLE_NAME: ClassVar[str]
    TABLE_NAME_V1: ClassVar[str]
    COLUMN_NAME_NOTIFICATION_ID: ClassVar[str]
    COLUMN_CHANNEL_INFLUENCE_ID: ClassVar[str]
    COLUMN_CHANNEL_TYPE: ClassVar[str]
    COLUMN_NAME_NAME: ClassVar[str]

from typing import Any, ClassVar, overload
from session.internal.outcomes.impl.OutcomeEvent import OutcomeEvent

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

class IOutcomeEventsBackendService:
    def sendOutcomeEvent(self, p0: str, p1: str, p2: str, p3: str, p4: bool, p5: OutcomeEvent, p6: Continuation) -> Any: ...

from typing import Any, ClassVar, overload

class IOutcomeEventsPreferences:
    def getUnattributedUniqueOutcomeEventsSentByChannel(self) -> set: ...
    def setUnattributedUniqueOutcomeEventsSentByChannel(self, p0: set) -> None: ...

from typing import Any, ClassVar, overload
from session.internal.outcomes.impl.OutcomeEventParams import OutcomeEventParams

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

class IOutcomeEventsRepository:
    def deleteOldOutcomeEvent(self, p0: OutcomeEventParams, p1: Continuation) -> Any: ...
    def saveUniqueOutcomeEventParams(self, p0: OutcomeEventParams, p1: Continuation) -> Any: ...
    def saveOutcomeEvent(self, p0: OutcomeEventParams, p1: Continuation) -> Any: ...
    def getAllEventsToSend(self, p0: Continuation) -> Any: ...
    def getNotCachedUniqueInfluencesForOutcome(self, p0: str, p1: list, p2: Continuation) -> Any: ...
    def cleanCachedUniqueOutcomeEventNotifications(self, p0: Continuation) -> Any: ...

from typing import Any, ClassVar, overload

class OutcomeConstants:
    INSTANCE: ClassVar["OutcomeConstants"]
    OUTCOME_ID: ClassVar[str]
    OUTCOME_SOURCES: ClassVar[str]
    WEIGHT: ClassVar[str]
    TIMESTAMP: ClassVar[str]
    SESSION_TIME: ClassVar[str]
    DIRECT: ClassVar[str]
    INDIRECT: ClassVar[str]
    NOTIFICATION_IDS: ClassVar[str]
    IAM_IDS: ClassVar[str]

from typing import Any, ClassVar, overload
from session.internal.influence.InfluenceType import InfluenceType
from session.internal.outcomes.impl.OutcomeEventParams import OutcomeEventParams

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
class JSONObject:
    """Forward declaration for ``org.json.JSONObject``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONObject')`` proxy; this empty class exists
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

class OutcomeEvent:
    Companion: ClassVar[Any]
    def __init__(self, p0: InfluenceType, p1: JSONArray, p2: str, p3: int, p4: int, p5: float) -> None: ...
    def getTimestamp(self) -> int: ...
    def getName(self) -> str: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def toJSONObject(self) -> JSONObject: ...
    def getSession(self) -> InfluenceType: ...
    def getWeight(self) -> float: ...
    def getNotificationIds(self) -> JSONArray: ...
    def getSessionTime(self) -> int: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...
        def fromOutcomeEventParamstoOutcomeEvent(self, p0: OutcomeEventParams) -> "OutcomeEvent": ...

from typing import Any, ClassVar, overload
from session.internal.outcomes.impl.OutcomeSource import OutcomeSource

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class JSONObject:
    """Forward declaration for ``org.json.JSONObject``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONObject')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class OutcomeEventParams:
    def __init__(self, p0: str, p1: OutcomeSource, p2: float, p3: int, p4: int) -> None: ...
    def getTimestamp(self) -> int: ...
    def toString(self) -> str: ...
    def isUnattributed(self) -> bool: ...
    def toJSONObject(self) -> JSONObject: ...
    def getWeight(self) -> float: ...
    def getSessionTime(self) -> int: ...
    def getOutcomeId(self) -> str: ...
    def getOutcomeSource(self) -> OutcomeSource: ...
    def setWeight(self, p0: float) -> None: ...
    def setSessionTime(self, p0: int) -> None: ...
    def setTimestamp(self, p0: int) -> None: ...

from typing import Any, ClassVar, overload
from core.internal.http.IHttpClient import IHttpClient
from session.internal.outcomes.impl.OutcomeEvent import OutcomeEvent

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

class OutcomeEventsBackendService:
    def __init__(self, p0: IHttpClient) -> None: ...
    def sendOutcomeEvent(self, p0: str, p1: str, p2: str, p3: str, p4: bool, p5: OutcomeEvent, p6: Continuation) -> Any: ...

from typing import Any, ClassVar, overload
from core.internal.config.ConfigModelStore import ConfigModelStore
from core.internal.device.IDeviceService import IDeviceService
from core.internal.time.ITime import ITime
from session.internal.influence.IInfluenceManager import IInfluenceManager
from session.internal.outcomes.impl.IOutcomeEventsBackendService import IOutcomeEventsBackendService
from session.internal.outcomes.impl.IOutcomeEventsPreferences import IOutcomeEventsPreferences
from session.internal.outcomes.impl.IOutcomeEventsRepository import IOutcomeEventsRepository
from session.internal.outcomes.impl.OutcomeEventParams import OutcomeEventParams
from session.internal.session.ISessionService import ISessionService
from user.internal.identity.IdentityModelStore import IdentityModelStore
from user.internal.subscriptions.ISubscriptionManager import ISubscriptionManager

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

class OutcomeEventsController:
    def __init__(self, p0: ISessionService, p1: IInfluenceManager, p2: IOutcomeEventsRepository, p3: IOutcomeEventsPreferences, p4: IOutcomeEventsBackendService, p5: ConfigModelStore, p6: IdentityModelStore, p7: ISubscriptionManager, p8: IDeviceService, p9: ITime) -> None: ...
    def start(self) -> None: ...
    def onSessionStarted(self) -> None: ...
    def onSessionActive(self) -> None: ...
    def onSessionEnded(self, p0: int) -> None: ...
    @staticmethod
    def access$sendSavedOutcomes(p0: "OutcomeEventsController", p1: Continuation) -> Any: ...
    @staticmethod
    def access$get_outcomeEventsCache$p(p0: "OutcomeEventsController") -> IOutcomeEventsRepository: ...
    @staticmethod
    def access$sendSavedOutcomeEvent(p0: "OutcomeEventsController", p1: OutcomeEventParams, p2: Continuation) -> Any: ...
    @staticmethod
    def access$sendUniqueOutcomeEvent(p0: "OutcomeEventsController", p1: str, p2: list, p3: Continuation) -> Any: ...
    @staticmethod
    def access$sendAndCreateOutcomeEvent(p0: "OutcomeEventsController", p1: str, p2: float, p3: int, p4: list, p5: Continuation) -> Any: ...
    @staticmethod
    def access$getUniqueIds(p0: "OutcomeEventsController", p1: str, p2: list, p3: Continuation) -> Any: ...
    @staticmethod
    def access$requestMeasureOutcomeEvent(p0: "OutcomeEventsController", p1: OutcomeEventParams, p2: Continuation) -> Any: ...
    def sendUniqueOutcomeEvent(self, p0: str, p1: Continuation) -> Any: ...
    def sendSessionEndOutcomeEvent(self, p0: int, p1: Continuation) -> Any: ...
    def sendOutcomeEvent(self, p0: str, p1: Continuation) -> Any: ...
    def sendOutcomeEventWithValue(self, p0: str, p1: float, p2: Continuation) -> Any: ...

    class WhenMappings:
        $EnumSwitchMapping$0: ClassVar[Any]
        $EnumSwitchMapping$1: ClassVar[Any]

from typing import Any, ClassVar, overload
from core.internal.preferences.IPreferencesService import IPreferencesService

class OutcomeEventsPreferences:
    def __init__(self, p0: IPreferencesService) -> None: ...
    def getUnattributedUniqueOutcomeEventsSentByChannel(self) -> set: ...
    def setUnattributedUniqueOutcomeEventsSentByChannel(self, p0: set) -> None: ...

from typing import Any, ClassVar, overload
from core.internal.database.IDatabaseProvider import IDatabaseProvider
from session.internal.influence.InfluenceType import InfluenceType
from session.internal.outcomes.impl.OutcomeEventParams import OutcomeEventParams
from session.internal.outcomes.impl.OutcomeSource import OutcomeSource
from session.internal.outcomes.impl.OutcomeSourceBody import OutcomeSourceBody

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

class OutcomeEventsRepository:
    def __init__(self, p0: IDatabaseProvider) -> None: ...
    def deleteOldOutcomeEvent(self, p0: OutcomeEventParams, p1: Continuation) -> Any: ...
    def saveUniqueOutcomeEventParams(self, p0: OutcomeEventParams, p1: Continuation) -> Any: ...
    def saveOutcomeEvent(self, p0: OutcomeEventParams, p1: Continuation) -> Any: ...
    def getAllEventsToSend(self, p0: Continuation) -> Any: ...
    def getNotCachedUniqueInfluencesForOutcome(self, p0: str, p1: list, p2: Continuation) -> Any: ...
    def cleanCachedUniqueOutcomeEventNotifications(self, p0: Continuation) -> Any: ...
    @staticmethod
    def access$get_databaseProvider$p(p0: "OutcomeEventsRepository") -> IDatabaseProvider: ...
    @staticmethod
    def access$getNotificationInfluenceSource(p0: "OutcomeEventsRepository", p1: InfluenceType, p2: OutcomeSourceBody, p3: OutcomeSourceBody, p4: str) -> OutcomeSource: ...
    @staticmethod
    def access$getIAMInfluenceSource(p0: "OutcomeEventsRepository", p1: InfluenceType, p2: OutcomeSourceBody, p3: OutcomeSourceBody, p4: str, p5: OutcomeSource) -> OutcomeSource: ...
    @staticmethod
    def access$addIdsToListFromSource(p0: "OutcomeEventsRepository", p1: list, p2: OutcomeSourceBody) -> None: ...

    class WhenMappings:
        $EnumSwitchMapping$0: ClassVar[Any]

from typing import Any, ClassVar, overload

class OutcomeEventsTable:
    INSTANCE: ClassVar["OutcomeEventsTable"]
    ID: ClassVar[str]
    TABLE_NAME: ClassVar[str]
    COLUMN_NAME_NOTIFICATION_IDS: ClassVar[str]
    COLUMN_NAME_IAM_IDS: ClassVar[str]
    COLUMN_NAME_SESSION: ClassVar[str]
    COLUMN_NAME_NOTIFICATION_INFLUENCE_TYPE: ClassVar[str]
    COLUMN_NAME_IAM_INFLUENCE_TYPE: ClassVar[str]
    COLUMN_NAME_NAME: ClassVar[str]
    COLUMN_NAME_WEIGHT: ClassVar[str]
    COLUMN_NAME_TIMESTAMP: ClassVar[str]
    COLUMN_NAME_PARAMS: ClassVar[str]
    COLUMN_NAME_SESSION_TIME: ClassVar[str]

from typing import Any, ClassVar, overload
from session.internal.outcomes.impl.OutcomeSourceBody import OutcomeSourceBody

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class JSONObject:
    """Forward declaration for ``org.json.JSONObject``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONObject')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class OutcomeSource:
    def __init__(self, p0: OutcomeSourceBody, p1: OutcomeSourceBody) -> None: ...
    def toString(self) -> str: ...
    def toJSONObject(self) -> JSONObject: ...
    def getDirectBody(self) -> OutcomeSourceBody: ...
    def getIndirectBody(self) -> OutcomeSourceBody: ...
    @overload
    def setDirectBody(self, p0: OutcomeSourceBody) -> "OutcomeSource": ...
    @overload
    def setDirectBody(self, p0: OutcomeSourceBody) -> None: ...
    @overload
    def setIndirectBody(self, p0: OutcomeSourceBody) -> "OutcomeSource": ...
    @overload
    def setIndirectBody(self, p0: OutcomeSourceBody) -> None: ...

from typing import Any, ClassVar, overload

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
class JSONObject:
    """Forward declaration for ``org.json.JSONObject``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONObject')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class OutcomeSourceBody:
    @overload
    def __init__(self, p0: JSONArray) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: JSONArray, p1: JSONArray) -> None: ...
    @overload
    def __init__(self, p0: JSONArray, p1: JSONArray, p2: int, p3: DefaultConstructorMarker) -> None: ...
    def toString(self) -> str: ...
    def toJSONObject(self) -> JSONObject: ...
    def getNotificationIds(self) -> JSONArray: ...
    def setInAppMessagesIds(self, p0: JSONArray) -> None: ...
    def setNotificationIds(self, p0: JSONArray) -> None: ...
    def getInAppMessagesIds(self) -> JSONArray: ...

from typing import Any, ClassVar, overload
from android.database.sqlite.SQLiteDatabase import SQLiteDatabase

class OutcomeTableProvider:
    def __init__(self) -> None: ...
    def upgradeOutcomeTableRevision1To2(self, p0: SQLiteDatabase) -> None: ...
    def upgradeOutcomeTableRevision2To3(self, p0: SQLiteDatabase) -> None: ...
    def upgradeCacheOutcomeTableRevision1To2(self, p0: SQLiteDatabase) -> None: ...
    def upgradeOutcomeTableRevision3To4(self, p0: SQLiteDatabase) -> None: ...

from typing import Any, ClassVar, overload

class OutcomesDbContract:
    INSTANCE: ClassVar["OutcomesDbContract"]
    OUTCOME_EVENT_TABLE: ClassVar[str]
    CACHE_UNIQUE_OUTCOME_TABLE: ClassVar[str]
    CACHE_UNIQUE_OUTCOME_COLUMN_CHANNEL_INFLUENCE_ID: ClassVar[str]
    CACHE_UNIQUE_OUTCOME_COLUMN_CHANNEL_TYPE: ClassVar[str]
    SQL_CREATE_OUTCOME_ENTRIES_V1: ClassVar[str]
    SQL_CREATE_OUTCOME_ENTRIES_V2: ClassVar[str]
    SQL_CREATE_OUTCOME_ENTRIES_V3: ClassVar[str]
    SQL_CREATE_OUTCOME_ENTRIES_V4: ClassVar[str]
    SQL_CREATE_UNIQUE_OUTCOME_ENTRIES_V1: ClassVar[str]
    SQL_CREATE_UNIQUE_OUTCOME_ENTRIES_V2: ClassVar[str]


from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.content.Intent import Intent

class GenerateNotificationOpenIntent:
    def __init__(self, p0: Context, p1: Intent, p2: bool) -> None: ...
    def getIntentVisible(self) -> Intent: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from notifications.internal.common.GenerateNotificationOpenIntent import GenerateNotificationOpenIntent

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

class GenerateNotificationOpenIntentFromPushPayload:
    INSTANCE: ClassVar["GenerateNotificationOpenIntentFromPushPayload"]
    def create(self, p0: Context, p1: JSONObject) -> GenerateNotificationOpenIntent: ...

from typing import Any, ClassVar, overload

class NotificationConstants:
    INSTANCE: ClassVar["NotificationConstants"]
    EXTENSION_SERVICE_META_DATA_TAG_NAME: ClassVar[str]
    DEFAULT_TTL_IF_NOT_IN_PAYLOAD: ClassVar[int]
    PUSH_ADDITIONAL_DATA_KEY: ClassVar[str]
    GOOGLE_SENT_TIME_KEY: ClassVar[str]
    GOOGLE_TTL_KEY: ClassVar[str]
    HMS_TTL_KEY: ClassVar[str]
    HMS_SENT_TIME_KEY: ClassVar[str]
    GENERATE_NOTIFICATION_BUNDLE_KEY_ACTION_ID: ClassVar[str]
    IAM_PREVIEW_KEY: ClassVar[str]
    BUNDLE_KEY_ANDROID_NOTIFICATION_ID: ClassVar[str]
    BUNDLE_KEY_ONESIGNAL_DATA: ClassVar[str]

from typing import Any, ClassVar, overload
from android.content.Intent import Intent
from android.os.Bundle import Bundle

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

class NotificationFormatHelper:
    INSTANCE: ClassVar["NotificationFormatHelper"]
    PAYLOAD_OS_ROOT_CUSTOM: ClassVar[str]
    PAYLOAD_OS_NOTIFICATION_ID: ClassVar[str]
    def isOneSignalBundle(self, p0: Bundle) -> bool: ...
    def getOSNotificationIdFromJson(self, p0: JSONObject) -> str: ...
    def isOneSignalIntent(self, p0: Intent) -> bool: ...

from typing import Any, ClassVar, overload
from android.net.Uri import Uri
from notifications.internal.Notification import Notification
from pyonesignal.core.internal.time.ITime import ITime

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

class NotificationGenerationJob:
    @overload
    def __init__(self, p0: JSONObject, p1: ITime) -> None: ...
    @overload
    def __init__(self, p0: Notification, p1: JSONObject) -> None: ...
    def getBody(self) -> str: ...
    def getAdditionalData(self) -> JSONObject: ...
    def toString(self) -> str: ...
    def isRestoring(self) -> bool: ...
    def getNotification(self) -> Notification: ...
    def getJsonPayload(self) -> JSONObject: ...
    def setJsonPayload(self, p0: JSONObject) -> None: ...
    def setRestoring(self, p0: bool) -> None: ...
    def isNotificationToDisplay(self) -> bool: ...
    def setNotificationToDisplay(self, p0: bool) -> None: ...
    def getShownTimeStamp(self) -> int: ...
    def setShownTimeStamp(self, p0: int) -> None: ...
    def getOverriddenBodyFromExtender(self) -> str: ...
    def setOverriddenBodyFromExtender(self, p0: str) -> None: ...
    def getOverriddenTitleFromExtender(self) -> str: ...
    def setOverriddenTitleFromExtender(self, p0: str) -> None: ...
    def getOverriddenSound(self) -> Uri: ...
    def setOverriddenSound(self, p0: Uri) -> None: ...
    def getOverriddenFlags(self) -> int: ...
    def setOverriddenFlags(self, p0: int) -> None: ...
    def getOrgFlags(self) -> int: ...
    def setOrgFlags(self, p0: int) -> None: ...
    def getOrgSound(self) -> Uri: ...
    def setOrgSound(self, p0: Uri) -> None: ...
    def hasExtender(self) -> bool: ...
    def getApiNotificationId(self) -> str: ...
    def getAndroidId(self) -> int: ...
    def getTitle(self) -> str: ...

from typing import Any, ClassVar, overload
from android.app.NotificationManager import NotificationManager
from android.content.Context import Context
from android.net.Uri import Uri
from android.service.notification.StatusBarNotification import StatusBarNotification
from notifications.internal.NotificationClickEvent import NotificationClickEvent
from pyonesignal.core.internal.time.ITime import ITime

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
class INotification:
    """Forward declaration for ``com.onesignal.notifications.INotification``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.notifications.INotification')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...
class JSONArray:
    """Forward declaration for ``org.json.JSONArray``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONArray')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class NotificationHelper:
    INSTANCE: ClassVar["NotificationHelper"]
    GROUPLESS_SUMMARY_KEY: ClassVar[str]
    GROUPLESS_SUMMARY_ID: ClassVar[int]
    def getActiveNotifications(self, p0: Context) -> Any: ...
    def isGroupSummary(self, p0: StatusBarNotification) -> bool: ...
    def getCustomJSONObject(self, p0: JSONObject) -> JSONObject: ...
    def getNotificationIdFromFCMJson(self, p0: JSONObject) -> str: ...
    def getNotificationManager(self, p0: Context) -> NotificationManager: ...
    def parseVibrationPattern(self, p0: JSONObject) -> Any: ...
    def getSoundUri(self, p0: Context, p1: str) -> Uri: ...
    def areNotificationsEnabled(self, p0: Context, p1: str) -> bool: ...
    def getGrouplessNotifsCount(self, p0: Context) -> int: ...
    def getActiveGrouplessNotifications(self, p0: Context) -> list: ...
    def assignGrouplessNotifications(self, p0: Context, p1: list) -> None: ...
    def getCampaignNameFromNotification(self, p0: INotification) -> str: ...
    def generateNotificationOpenedResult$com_onesignal_notifications(self, p0: JSONArray, p1: ITime) -> NotificationClickEvent: ...
    @staticmethod
    def areNotificationsEnabled$default(p0: "NotificationHelper", p1: Context, p2: str, p3: int, p4: Any) -> bool: ...

from typing import Any, ClassVar, overload

class NotificationPriorityMapper:
    INSTANCE: ClassVar["NotificationPriorityMapper"]
    def isHighPriority(self, p0: int) -> bool: ...
    def toAndroidPriority(self, p0: int) -> int: ...
    def toAndroidImportance(self, p0: int) -> int: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context

class OSNotificationOpenAppSettings:
    INSTANCE: ClassVar["OSNotificationOpenAppSettings"]
    def getShouldOpenActivity(self, p0: Context) -> bool: ...
    def getSuppressLaunchURL(self, p0: Context) -> bool: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.net.Uri import Uri

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

class OSNotificationOpenBehaviorFromPushPayload:
    def __init__(self, p0: Context, p1: JSONObject) -> None: ...
    def getUri(self) -> Uri: ...
    def getShouldOpenApp(self) -> bool: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from androidx.work.WorkManager import WorkManager

class OSWorkManagerHelper:
    INSTANCE: ClassVar["OSWorkManagerHelper"]
    def getInstance(self, p0: Context) -> WorkManager: ...


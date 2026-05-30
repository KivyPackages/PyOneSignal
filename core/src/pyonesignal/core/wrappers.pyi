from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Consumer:
    """Forward declaration for ``java.util.function.Consumer``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.util.function.Consumer')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/util/function/Consumer.html
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
class CoroutineContext:
    """Forward declaration for ``kotlin.coroutines.CoroutineContext``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.coroutines.CoroutineContext')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/coroutines/CoroutineContext/
    """
    ...

class Continue:
    INSTANCE: ClassVar["Continue"]
    @overload
    @staticmethod
    def with_(p0: Consumer) -> Continuation: ...
    @overload
    @staticmethod
    def with_(p0: Consumer, p1: CoroutineContext) -> Continuation: ...
    @staticmethod
    def with$default(p0: Consumer, p1: CoroutineContext, p2: int, p3: Any) -> Continuation: ...
    @staticmethod
    def none() -> Continuation: ...

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Throwable:
    """Forward declaration for ``java.lang.Throwable``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.Throwable')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html
    """
    ...

class ContinueResult:
    def __init__(self, p0: bool, p1: Any, p2: Throwable) -> None: ...
    def getData(self) -> Any: ...
    def isSuccess(self) -> bool: ...
    def getThrowable(self) -> Throwable: ...

from typing import Any, ClassVar, overload
from IUserJwtInvalidatedListener import IUserJwtInvalidatedListener
from android.content.Context import Context
from debug.IDebugManager import IDebugManager
from inAppMessages.IInAppMessagesManager import IInAppMessagesManager
from location.ILocationManager import ILocationManager
from notifications.INotificationsManager import INotificationsManager
from session.ISessionManager import ISessionManager
from user.IUserManager import IUserManager

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

class IOneSignal:
    @overload
    def getLocation(self) -> ILocationManager: ...
    @overload
    def getLocation(self, p0: Continuation) -> Any: ...
    def getDebug(self) -> IDebugManager: ...
    @overload
    def login(self, p0: str) -> None: ...
    @overload
    def login(self, p0: str, p1: str) -> None: ...
    def logout(self) -> None: ...
    @overload
    def getUser(self) -> IUserManager: ...
    @overload
    def getUser(self, p0: Continuation) -> Any: ...
    @overload
    def getSession(self, p0: Continuation) -> Any: ...
    @overload
    def getSession(self) -> ISessionManager: ...
    def isInitialized(self) -> bool: ...
    @overload
    def getDisableGMSMissingPrompt(self) -> bool: ...
    @overload
    def getDisableGMSMissingPrompt(self, p0: Continuation) -> Any: ...
    def getSdkVersion(self) -> str: ...
    @overload
    def getNotifications(self) -> INotificationsManager: ...
    @overload
    def getNotifications(self, p0: Continuation) -> Any: ...
    @overload
    def getInAppMessages(self) -> IInAppMessagesManager: ...
    @overload
    def getInAppMessages(self, p0: Continuation) -> Any: ...
    @overload
    def getConsentRequired(self) -> bool: ...
    @overload
    def getConsentRequired(self, p0: Continuation) -> Any: ...
    @overload
    def setConsentRequired(self, p0: bool, p1: Continuation) -> Any: ...
    @overload
    def setConsentRequired(self, p0: bool) -> None: ...
    @overload
    def getConsentGiven(self, p0: Continuation) -> Any: ...
    @overload
    def getConsentGiven(self) -> bool: ...
    @overload
    def setConsentGiven(self, p0: bool, p1: Continuation) -> Any: ...
    @overload
    def setConsentGiven(self, p0: bool) -> None: ...
    @overload
    def setDisableGMSMissingPrompt(self, p0: bool, p1: Continuation) -> Any: ...
    @overload
    def setDisableGMSMissingPrompt(self, p0: bool) -> None: ...
    @overload
    def initWithContext(self, p0: Context, p1: str) -> bool: ...
    @overload
    def initWithContext(self, p0: Context, p1: Continuation) -> Any: ...
    def updateUserJwt(self, p0: str, p1: str) -> None: ...
    def addUserJwtInvalidatedListener(self, p0: IUserJwtInvalidatedListener) -> None: ...
    def removeUserJwtInvalidatedListener(self, p0: IUserJwtInvalidatedListener) -> None: ...
    def initWithContextSuspend(self, p0: Context, p1: str, p2: Continuation) -> Any: ...
    def loginSuspend(self, p0: str, p1: str, p2: Continuation) -> Any: ...
    def logoutSuspend(self, p0: Continuation) -> Any: ...
    def updateUserJwtSuspend(self, p0: str, p1: str, p2: Continuation) -> Any: ...

    class DefaultImpls:
        @staticmethod
        def loginSuspend$default(p0: "IOneSignal", p1: str, p2: str, p3: Continuation, p4: int, p5: Any) -> Any: ...
        @staticmethod
        def login$default(p0: "IOneSignal", p1: str, p2: str, p3: int, p4: Any) -> None: ...
        @staticmethod
        def initWithContextSuspend$default(p0: "IOneSignal", p1: Context, p2: str, p3: Continuation, p4: int, p5: Any) -> Any: ...
        @staticmethod
        def login(p0: "IOneSignal", p1: str) -> None: ...

from typing import Any, ClassVar, overload
from UserJwtInvalidatedEvent import UserJwtInvalidatedEvent

class IUserJwtInvalidatedListener:
    def onUserJwtInvalidated(self, p0: UserJwtInvalidatedEvent) -> None: ...

from typing import Any, ClassVar, overload
from IUserJwtInvalidatedListener import IUserJwtInvalidatedListener
from android.content.Context import Context
from common.services.IServiceProvider import IServiceProvider
from debug.IDebugManager import IDebugManager
from inAppMessages.IInAppMessagesManager import IInAppMessagesManager
from location.ILocationManager import ILocationManager
from notifications.INotificationsManager import INotificationsManager
from session.ISessionManager import ISessionManager
from user.IUserManager import IUserManager

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

class OneSignal:
    INSTANCE: ClassVar["OneSignal"]
    @staticmethod
    def getLocation() -> ILocationManager: ...
    @staticmethod
    def getDebug() -> IDebugManager: ...
    @staticmethod
    def loginSuspend$default(p0: str, p1: str, p2: Continuation, p3: int, p4: Any) -> Any: ...
    @staticmethod
    def login$default(p0: str, p1: str, p2: int, p3: Any) -> None: ...
    @staticmethod
    def initWithContextSuspend$default(p0: Context, p1: str, p2: Continuation, p3: int, p4: Any) -> Any: ...
    @staticmethod
    def isInitialized$annotations() -> None: ...
    @staticmethod
    def getSdkVersion$annotations() -> None: ...
    @staticmethod
    def getUser$annotations() -> None: ...
    @staticmethod
    def getSession$annotations() -> None: ...
    @staticmethod
    def getNotifications$annotations() -> None: ...
    @staticmethod
    def getLocation$annotations() -> None: ...
    @staticmethod
    def getInAppMessages$annotations() -> None: ...
    @staticmethod
    def getDebug$annotations() -> None: ...
    @staticmethod
    def getConsentRequired$annotations() -> None: ...
    @staticmethod
    def getConsentGiven$annotations() -> None: ...
    @staticmethod
    def getDisableGMSMissingPrompt$annotations() -> None: ...
    @staticmethod
    def getUserSuspend(p0: Continuation) -> Any: ...
    @staticmethod
    def getSessionSuspend(p0: Continuation) -> Any: ...
    @staticmethod
    def getNotificationsSuspend(p0: Continuation) -> Any: ...
    @staticmethod
    def getLocationSuspend(p0: Continuation) -> Any: ...
    @staticmethod
    def getInAppMessagesSuspend(p0: Continuation) -> Any: ...
    @staticmethod
    def getConsentRequiredSuspend(p0: Continuation) -> Any: ...
    @staticmethod
    def setConsentRequiredSuspend(p0: bool, p1: Continuation) -> Any: ...
    @staticmethod
    def getConsentGivenSuspend(p0: Continuation) -> Any: ...
    @staticmethod
    def setConsentGivenSuspend(p0: bool, p1: Continuation) -> Any: ...
    @staticmethod
    def getDisableGMSMissingPromptSuspend(p0: Continuation) -> Any: ...
    @staticmethod
    def setDisableGMSMissingPromptSuspend(p0: bool, p1: Continuation) -> Any: ...
    def getServices(self) -> IServiceProvider: ...
    def getService(self) -> Any: ...
    def getServiceOrNull(self) -> Any: ...
    @overload
    @staticmethod
    def login(p0: str, p1: str) -> None: ...
    @overload
    @staticmethod
    def login(p0: str) -> None: ...
    @staticmethod
    def logout() -> None: ...
    @staticmethod
    def getUser() -> IUserManager: ...
    @staticmethod
    def getSession() -> ISessionManager: ...
    @staticmethod
    def isInitialized() -> bool: ...
    @staticmethod
    def getDisableGMSMissingPrompt() -> bool: ...
    @staticmethod
    def getSdkVersion() -> str: ...
    @staticmethod
    def getNotifications() -> INotificationsManager: ...
    @staticmethod
    def getInAppMessages() -> IInAppMessagesManager: ...
    @staticmethod
    def getConsentRequired() -> bool: ...
    @staticmethod
    def setConsentRequired(p0: bool) -> None: ...
    @staticmethod
    def getConsentGiven() -> bool: ...
    @staticmethod
    def setConsentGiven(p0: bool) -> None: ...
    @staticmethod
    def setDisableGMSMissingPrompt(p0: bool) -> None: ...
    @overload
    @staticmethod
    def initWithContext(p0: Context, p1: str) -> None: ...
    @overload
    @staticmethod
    def initWithContext(p0: Context, p1: Continuation) -> Any: ...
    @staticmethod
    def updateUserJwt(p0: str, p1: str) -> None: ...
    @staticmethod
    def addUserJwtInvalidatedListener(p0: IUserJwtInvalidatedListener) -> None: ...
    @staticmethod
    def removeUserJwtInvalidatedListener(p0: IUserJwtInvalidatedListener) -> None: ...
    @staticmethod
    def initWithContextSuspend(p0: Context, p1: str, p2: Continuation) -> Any: ...
    @staticmethod
    def loginSuspend(p0: str, p1: str, p2: Continuation) -> Any: ...
    @staticmethod
    def logoutSuspend(p0: Continuation) -> Any: ...
    @staticmethod
    def updateUserJwtSuspend(p0: str, p1: str, p2: Continuation) -> Any: ...

from typing import Any, ClassVar, overload
from android.app.job.JobParameters import JobParameters

class SyncJobService:
    JOB_END_NOTIFICATION_POLICY_DETACH: ClassVar[int]
    JOB_END_NOTIFICATION_POLICY_REMOVE: ClassVar[int]
    PERMISSION_BIND: ClassVar[str]
    START_CONTINUATION_MASK: ClassVar[int]
    START_FLAG_REDELIVERY: ClassVar[int]
    START_FLAG_RETRY: ClassVar[int]
    START_NOT_STICKY: ClassVar[int]
    START_REDELIVER_INTENT: ClassVar[int]
    START_STICKY: ClassVar[int]
    START_STICKY_COMPATIBILITY: ClassVar[int]
    STOP_FOREGROUND_DETACH: ClassVar[int]
    STOP_FOREGROUND_LEGACY: ClassVar[int]
    STOP_FOREGROUND_REMOVE: ClassVar[int]
    TRIM_MEMORY_BACKGROUND: ClassVar[int]
    TRIM_MEMORY_COMPLETE: ClassVar[int]
    TRIM_MEMORY_MODERATE: ClassVar[int]
    TRIM_MEMORY_RUNNING_CRITICAL: ClassVar[int]
    TRIM_MEMORY_RUNNING_LOW: ClassVar[int]
    TRIM_MEMORY_RUNNING_MODERATE: ClassVar[int]
    TRIM_MEMORY_UI_HIDDEN: ClassVar[int]
    ACCESSIBILITY_SERVICE: ClassVar[str]
    ACCOUNT_SERVICE: ClassVar[str]
    ACTIVITY_SERVICE: ClassVar[str]
    ADVANCED_PROTECTION_SERVICE: ClassVar[str]
    ALARM_SERVICE: ClassVar[str]
    APPWIDGET_SERVICE: ClassVar[str]
    APP_FUNCTION_SERVICE: ClassVar[str]
    APP_OPS_SERVICE: ClassVar[str]
    APP_SEARCH_SERVICE: ClassVar[str]
    AUDIO_SERVICE: ClassVar[str]
    BATTERY_SERVICE: ClassVar[str]
    BIND_ABOVE_CLIENT: ClassVar[int]
    BIND_ADJUST_WITH_ACTIVITY: ClassVar[int]
    BIND_ALLOW_ACTIVITY_STARTS: ClassVar[int]
    BIND_ALLOW_OOM_MANAGEMENT: ClassVar[int]
    BIND_AUTO_CREATE: ClassVar[int]
    BIND_DEBUG_UNBIND: ClassVar[int]
    BIND_EXTERNAL_SERVICE: ClassVar[int]
    BIND_EXTERNAL_SERVICE_LONG: ClassVar[int]
    BIND_IMPORTANT: ClassVar[int]
    BIND_INCLUDE_CAPABILITIES: ClassVar[int]
    BIND_NOT_FOREGROUND: ClassVar[int]
    BIND_NOT_PERCEPTIBLE: ClassVar[int]
    BIND_PACKAGE_ISOLATED_PROCESS: ClassVar[int]
    BIND_SHARED_ISOLATED_PROCESS: ClassVar[int]
    BIND_WAIVE_PRIORITY: ClassVar[int]
    BIOMETRIC_SERVICE: ClassVar[str]
    BLOB_STORE_SERVICE: ClassVar[str]
    BLUETOOTH_SERVICE: ClassVar[str]
    BUGREPORT_SERVICE: ClassVar[str]
    CAMERA_SERVICE: ClassVar[str]
    CAPTIONING_SERVICE: ClassVar[str]
    CARRIER_CONFIG_SERVICE: ClassVar[str]
    CLIPBOARD_SERVICE: ClassVar[str]
    COMPANION_DEVICE_SERVICE: ClassVar[str]
    CONNECTIVITY_DIAGNOSTICS_SERVICE: ClassVar[str]
    CONNECTIVITY_SERVICE: ClassVar[str]
    CONSUMER_IR_SERVICE: ClassVar[str]
    CONTACT_KEYS_SERVICE: ClassVar[str]
    CONTEXT_IGNORE_SECURITY: ClassVar[int]
    CONTEXT_INCLUDE_CODE: ClassVar[int]
    CONTEXT_RESTRICTED: ClassVar[int]
    CREDENTIAL_SERVICE: ClassVar[str]
    CROSS_PROFILE_APPS_SERVICE: ClassVar[str]
    DEVICE_ID_DEFAULT: ClassVar[int]
    DEVICE_ID_INVALID: ClassVar[int]
    DEVICE_LOCK_SERVICE: ClassVar[str]
    DEVICE_POLICY_SERVICE: ClassVar[str]
    DISPLAY_HASH_SERVICE: ClassVar[str]
    DISPLAY_SERVICE: ClassVar[str]
    DOMAIN_VERIFICATION_SERVICE: ClassVar[str]
    DOWNLOAD_SERVICE: ClassVar[str]
    DROPBOX_SERVICE: ClassVar[str]
    EUICC_SERVICE: ClassVar[str]
    FILE_INTEGRITY_SERVICE: ClassVar[str]
    FINGERPRINT_SERVICE: ClassVar[str]
    GAME_SERVICE: ClassVar[str]
    GRAMMATICAL_INFLECTION_SERVICE: ClassVar[str]
    HARDWARE_PROPERTIES_SERVICE: ClassVar[str]
    HEALTHCONNECT_SERVICE: ClassVar[str]
    INPUT_METHOD_SERVICE: ClassVar[str]
    INPUT_SERVICE: ClassVar[str]
    IPSEC_SERVICE: ClassVar[str]
    JOB_SCHEDULER_SERVICE: ClassVar[str]
    KEYGUARD_SERVICE: ClassVar[str]
    KEYSTORE_SERVICE: ClassVar[str]
    LAUNCHER_APPS_SERVICE: ClassVar[str]
    LAYOUT_INFLATER_SERVICE: ClassVar[str]
    LOCALE_SERVICE: ClassVar[str]
    LOCATION_SERVICE: ClassVar[str]
    MEDIA_COMMUNICATION_SERVICE: ClassVar[str]
    MEDIA_METRICS_SERVICE: ClassVar[str]
    MEDIA_PROJECTION_SERVICE: ClassVar[str]
    MEDIA_QUALITY_SERVICE: ClassVar[str]
    MEDIA_ROUTER_SERVICE: ClassVar[str]
    MEDIA_SESSION_SERVICE: ClassVar[str]
    MIDI_SERVICE: ClassVar[str]
    MODE_APPEND: ClassVar[int]
    MODE_ENABLE_WRITE_AHEAD_LOGGING: ClassVar[int]
    MODE_MULTI_PROCESS: ClassVar[int]
    MODE_NO_LOCALIZED_COLLATORS: ClassVar[int]
    MODE_PRIVATE: ClassVar[int]
    MODE_WORLD_READABLE: ClassVar[int]
    MODE_WORLD_WRITEABLE: ClassVar[int]
    NETWORK_STATS_SERVICE: ClassVar[str]
    NFC_SERVICE: ClassVar[str]
    NOTIFICATION_SERVICE: ClassVar[str]
    NSD_SERVICE: ClassVar[str]
    OVERLAY_SERVICE: ClassVar[str]
    PEOPLE_SERVICE: ClassVar[str]
    PERFORMANCE_HINT_SERVICE: ClassVar[str]
    PERSISTENT_DATA_BLOCK_SERVICE: ClassVar[str]
    POWER_SERVICE: ClassVar[str]
    PRINT_SERVICE: ClassVar[str]
    PROFILING_SERVICE: ClassVar[str]
    RECEIVER_EXPORTED: ClassVar[int]
    RECEIVER_NOT_EXPORTED: ClassVar[int]
    RECEIVER_VISIBLE_TO_INSTANT_APPS: ClassVar[int]
    RESTRICTIONS_SERVICE: ClassVar[str]
    ROLE_SERVICE: ClassVar[str]
    SATELLITE_SERVICE: ClassVar[str]
    SEARCH_SERVICE: ClassVar[str]
    SECURITY_STATE_SERVICE: ClassVar[str]
    SENSOR_SERVICE: ClassVar[str]
    SHORTCUT_SERVICE: ClassVar[str]
    STATUS_BAR_SERVICE: ClassVar[str]
    STORAGE_SERVICE: ClassVar[str]
    STORAGE_STATS_SERVICE: ClassVar[str]
    SYSTEM_HEALTH_SERVICE: ClassVar[str]
    TELECOM_SERVICE: ClassVar[str]
    TELEPHONY_IMS_SERVICE: ClassVar[str]
    TELEPHONY_SERVICE: ClassVar[str]
    TELEPHONY_SUBSCRIPTION_SERVICE: ClassVar[str]
    TETHERING_SERVICE: ClassVar[str]
    TEXT_CLASSIFICATION_SERVICE: ClassVar[str]
    TEXT_SERVICES_MANAGER_SERVICE: ClassVar[str]
    TV_AD_SERVICE: ClassVar[str]
    TV_INPUT_SERVICE: ClassVar[str]
    TV_INTERACTIVE_APP_SERVICE: ClassVar[str]
    UI_MODE_SERVICE: ClassVar[str]
    USAGE_STATS_SERVICE: ClassVar[str]
    USB_SERVICE: ClassVar[str]
    USER_SERVICE: ClassVar[str]
    VIBRATOR_MANAGER_SERVICE: ClassVar[str]
    VIBRATOR_SERVICE: ClassVar[str]
    VIRTUAL_DEVICE_SERVICE: ClassVar[str]
    VPN_MANAGEMENT_SERVICE: ClassVar[str]
    WALLPAPER_SERVICE: ClassVar[str]
    WIFI_AWARE_SERVICE: ClassVar[str]
    WIFI_P2P_SERVICE: ClassVar[str]
    WIFI_RTT_RANGING_SERVICE: ClassVar[str]
    WIFI_SERVICE: ClassVar[str]
    WINDOW_SERVICE: ClassVar[str]
    def __init__(self) -> None: ...
    def onStopJob(self, p0: JobParameters) -> bool: ...
    def onStartJob(self, p0: JobParameters) -> bool: ...

from typing import Any, ClassVar, overload

class UserJwtInvalidatedEvent:
    def __init__(self, p0: str) -> None: ...
    def getExternalId(self) -> str: ...


from typing import Any, ClassVar, overload

class IPreferencesService:
    def getInt(self, p0: str, p1: str, p2: int) -> int: ...
    def getLong(self, p0: str, p1: str, p2: int) -> int: ...
    def getString(self, p0: str, p1: str, p2: str) -> str: ...
    def getStringSet(self, p0: str, p1: str, p2: set) -> set: ...
    def getBool(self, p0: str, p1: str, p2: bool) -> bool: ...
    def saveBool(self, p0: str, p1: str, p2: bool) -> None: ...
    def saveInt(self, p0: str, p1: str, p2: int) -> None: ...
    def saveLong(self, p0: str, p1: str, p2: int) -> None: ...
    def saveStringSet(self, p0: str, p1: str, p2: set) -> None: ...
    def saveString(self, p0: str, p1: str, p2: str) -> None: ...

    class DefaultImpls:
        @staticmethod
        def getBool$default(p0: "IPreferencesService", p1: str, p2: str, p3: bool, p4: int, p5: Any) -> bool: ...
        @staticmethod
        def getInt$default(p0: "IPreferencesService", p1: str, p2: str, p3: int, p4: int, p5: Any) -> int: ...
        @staticmethod
        def getLong$default(p0: "IPreferencesService", p1: str, p2: str, p3: int, p4: int, p5: Any) -> int: ...
        @staticmethod
        def getStringSet$default(p0: "IPreferencesService", p1: str, p2: str, p3: set, p4: int, p5: Any) -> set: ...
        @staticmethod
        def getString$default(p0: "IPreferencesService", p1: str, p2: str, p3: str, p4: int, p5: Any) -> str: ...

from typing import Any, ClassVar, overload

class PreferenceOneSignalKeys:
    INSTANCE: ClassVar["PreferenceOneSignalKeys"]
    PREFS_LEGACY_APP_ID: ClassVar[str]
    PREFS_LEGACY_PLAYER_ID: ClassVar[str]
    PREFS_LEGACY_USER_SYNCVALUES: ClassVar[str]
    PREFS_OS_LAST_LOCATION_TIME: ClassVar[str]
    PREFS_OS_LOCATION_SHARED: ClassVar[str]
    PREFS_OS_JWT_TOKENS: ClassVar[str]
    PREFS_OS_USER_RESOLVED_PERMISSION_PREFIX: ClassVar[str]
    PREFS_OS_ETAG_PREFIX: ClassVar[str]
    PREFS_OS_INSTALL_ID: ClassVar[str]
    PREFS_OS_HTTP_CACHE_PREFIX: ClassVar[str]
    PREFS_OS_UNATTRIBUTED_UNIQUE_OUTCOME_EVENTS_SENT: ClassVar[str]
    PREFS_OS_CACHED_IAMS: ClassVar[str]
    PREFS_OS_DISMISSED_IAMS: ClassVar[str]
    PREFS_OS_IMPRESSIONED_IAMS: ClassVar[str]
    PREFS_OS_CLICKED_CLICK_IDS_IAMS: ClassVar[str]
    PREFS_OS_PAGE_IMPRESSIONED_IAMS: ClassVar[str]
    PREFS_OS_IAM_LAST_DISMISSED_TIME: ClassVar[str]
    MODEL_STORE_PREFIX: ClassVar[str]

from typing import Any, ClassVar, overload

class PreferencePlayerPurchasesKeys:
    INSTANCE: ClassVar["PreferencePlayerPurchasesKeys"]
    PREFS_PURCHASE_TOKENS: ClassVar[str]
    PREFS_EXISTING_PURCHASES: ClassVar[str]

from typing import Any, ClassVar, overload
from android.content.Context import Context

class PreferenceStoreFix:
    INSTANCE: ClassVar["PreferenceStoreFix"]
    def ensureNoObfuscatedPrefStore(self, p0: Context) -> None: ...

from typing import Any, ClassVar, overload

class PreferenceStores:
    INSTANCE: ClassVar["PreferenceStores"]
    ONESIGNAL: ClassVar[str]
    PLAYER_PURCHASES: ClassVar[str]

from typing import Any, ClassVar, overload
from core.internal.preferences.IPreferencesService import IPreferencesService

class PreferencesExtensionV4Kt:
    @staticmethod
    def getLegacyAppId(p0: IPreferencesService) -> str: ...
    @staticmethod
    def getLegacyPlayerId(p0: IPreferencesService) -> str: ...
    @staticmethod
    def getLegacyUserSyncValues(p0: IPreferencesService) -> str: ...
    @staticmethod
    def clearLegacyPlayerId(p0: IPreferencesService) -> None: ...


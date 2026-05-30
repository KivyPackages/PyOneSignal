from typing import Any, ClassVar, overload
from common.modeling.ModelChangedArgs import ModelChangedArgs
from user.subscriptions.ISubscription import ISubscription

class ISubscriptionChangedHandler:
    def onSubscriptionAdded(self, p0: ISubscription) -> None: ...
    def onSubscriptionChanged(self, p0: ISubscription, p1: ModelChangedArgs) -> None: ...
    def onSubscriptionRemoved(self, p0: ISubscription) -> None: ...

from typing import Any, ClassVar, overload
from user.internal.subscriptions.SubscriptionList import SubscriptionList
from user.internal.subscriptions.SubscriptionModel import SubscriptionModel
from user.internal.subscriptions.SubscriptionStatus import SubscriptionStatus

class ISubscriptionManager:
    def getSubscriptions(self) -> SubscriptionList: ...
    def getPushSubscriptionModel(self) -> SubscriptionModel: ...
    def setSubscriptions(self, p0: SubscriptionList) -> None: ...
    def addEmailSubscription(self, p0: str) -> None: ...
    def addOrUpdatePushSubscriptionToken(self, p0: str, p1: SubscriptionStatus) -> None: ...
    def addSmsSubscription(self, p0: str) -> None: ...
    def removeEmailSubscription(self, p0: str) -> None: ...
    def removeSmsSubscription(self, p0: str) -> None: ...

from typing import Any, ClassVar, overload
from user.subscriptions.IEmailSubscription import IEmailSubscription
from user.subscriptions.IPushSubscription import IPushSubscription
from user.subscriptions.ISmsSubscription import ISmsSubscription

class SubscriptionList:
    def __init__(self, p0: list, p1: IPushSubscription) -> None: ...
    def getPush(self) -> IPushSubscription: ...
    def getCollection(self) -> list: ...
    def getEmails(self) -> list: ...
    def getSmss(self) -> list: ...
    def getByEmail(self, p0: str) -> IEmailSubscription: ...
    def getBySMS(self, p0: str) -> ISmsSubscription: ...

from typing import Any, ClassVar, overload
from user.internal.subscriptions.SubscriptionStatus import SubscriptionStatus
from user.internal.subscriptions.SubscriptionType import SubscriptionType

class SubscriptionModel:
    def __init__(self) -> None: ...
    def getType(self) -> SubscriptionType: ...
    def getAddress(self) -> str: ...
    def getAppVersion(self) -> str: ...
    def setType(self, p0: SubscriptionType) -> None: ...
    def setDisabledInternally(self, p0: bool) -> None: ...
    def isDisabledInternally(self) -> bool: ...
    def getStatus(self) -> SubscriptionStatus: ...
    def setSdk(self, p0: str) -> None: ...
    def getSdk(self) -> str: ...
    def getDeviceOS(self) -> str: ...
    def setDeviceOS(self, p0: str) -> None: ...
    def getCarrier(self) -> str: ...
    def setCarrier(self, p0: str) -> None: ...
    def setAppVersion(self, p0: str) -> None: ...
    def setStatus(self, p0: SubscriptionStatus) -> None: ...
    def getOptedIn(self) -> bool: ...
    def setOptedIn(self, p0: bool) -> None: ...
    def setAddress(self, p0: str) -> None: ...

from typing import Any, ClassVar, overload
from common.modeling.Model import Model
from core.internal.preferences.IPreferencesService import IPreferencesService

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

class SubscriptionModelStore:
    def __init__(self, p0: IPreferencesService) -> None: ...
    def replaceAll(self, p0: list, p1: str) -> None: ...
    def transformJsonForPersistence(self, p0: Model, p1: JSONObject) -> JSONObject: ...

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class EnumEntries:
    """Forward declaration for ``kotlin.enums.EnumEntries``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.enums.EnumEntries')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/enums/EnumEntries/
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

class SubscriptionStatus:
    SUBSCRIBED: ClassVar["SubscriptionStatus"]
    NO_PERMISSION: ClassVar["SubscriptionStatus"]
    UNSUBSCRIBE: ClassVar["SubscriptionStatus"]
    MISSING_JETPACK_LIBRARY: ClassVar["SubscriptionStatus"]
    MISSING_FIREBASE_FCM_LIBRARY: ClassVar["SubscriptionStatus"]
    OUTDATED_JETPACK_LIBRARY: ClassVar["SubscriptionStatus"]
    INVALID_FCM_SENDER_ID: ClassVar["SubscriptionStatus"]
    OUTDATED_GOOGLE_PLAY_SERVICES_APP: ClassVar["SubscriptionStatus"]
    FIREBASE_FCM_INIT_ERROR: ClassVar["SubscriptionStatus"]
    FIREBASE_FCM_ERROR_IOEXCEPTION_SERVICE_NOT_AVAILABLE: ClassVar["SubscriptionStatus"]
    FIREBASE_FCM_ERROR_IOEXCEPTION_OTHER: ClassVar["SubscriptionStatus"]
    FIREBASE_FCM_ERROR_MISC_EXCEPTION: ClassVar["SubscriptionStatus"]
    HMS_TOKEN_TIMEOUT: ClassVar["SubscriptionStatus"]
    HMS_ARGUMENTS_INVALID: ClassVar["SubscriptionStatus"]
    HMS_API_EXCEPTION_OTHER: ClassVar["SubscriptionStatus"]
    MISSING_HMS_PUSHKIT_LIBRARY: ClassVar["SubscriptionStatus"]
    FIREBASE_FCM_ERROR_IOEXCEPTION_AUTHENTICATION_FAILED: ClassVar["SubscriptionStatus"]
    DISABLED_FROM_REST_API_DEFAULT_REASON: ClassVar["SubscriptionStatus"]
    ERROR: ClassVar["SubscriptionStatus"]
    Companion: ClassVar[Any]
    SUBSCRIBED: ClassVar["SubscriptionStatus"]
    NO_PERMISSION: ClassVar["SubscriptionStatus"]
    UNSUBSCRIBE: ClassVar["SubscriptionStatus"]
    MISSING_JETPACK_LIBRARY: ClassVar["SubscriptionStatus"]
    MISSING_FIREBASE_FCM_LIBRARY: ClassVar["SubscriptionStatus"]
    OUTDATED_JETPACK_LIBRARY: ClassVar["SubscriptionStatus"]
    INVALID_FCM_SENDER_ID: ClassVar["SubscriptionStatus"]
    OUTDATED_GOOGLE_PLAY_SERVICES_APP: ClassVar["SubscriptionStatus"]
    FIREBASE_FCM_INIT_ERROR: ClassVar["SubscriptionStatus"]
    FIREBASE_FCM_ERROR_IOEXCEPTION_SERVICE_NOT_AVAILABLE: ClassVar["SubscriptionStatus"]
    FIREBASE_FCM_ERROR_IOEXCEPTION_OTHER: ClassVar["SubscriptionStatus"]
    FIREBASE_FCM_ERROR_MISC_EXCEPTION: ClassVar["SubscriptionStatus"]
    HMS_TOKEN_TIMEOUT: ClassVar["SubscriptionStatus"]
    HMS_ARGUMENTS_INVALID: ClassVar["SubscriptionStatus"]
    HMS_API_EXCEPTION_OTHER: ClassVar["SubscriptionStatus"]
    MISSING_HMS_PUSHKIT_LIBRARY: ClassVar["SubscriptionStatus"]
    FIREBASE_FCM_ERROR_IOEXCEPTION_AUTHENTICATION_FAILED: ClassVar["SubscriptionStatus"]
    DISABLED_FROM_REST_API_DEFAULT_REASON: ClassVar["SubscriptionStatus"]
    ERROR: ClassVar["SubscriptionStatus"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "SubscriptionStatus": ...
    def getValue(self) -> int: ...
    @staticmethod
    def getEntries() -> EnumEntries: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...
        def fromInt(self, p0: int) -> "SubscriptionStatus": ...

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class EnumEntries:
    """Forward declaration for ``kotlin.enums.EnumEntries``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.enums.EnumEntries')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/enums/EnumEntries/
    """
    ...

class SubscriptionType:
    EMAIL: ClassVar["SubscriptionType"]
    SMS: ClassVar["SubscriptionType"]
    PUSH: ClassVar["SubscriptionType"]
    EMAIL: ClassVar["SubscriptionType"]
    SMS: ClassVar["SubscriptionType"]
    PUSH: ClassVar["SubscriptionType"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "SubscriptionType": ...
    @staticmethod
    def getEntries() -> EnumEntries: ...


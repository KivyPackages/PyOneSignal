from typing import Any, ClassVar, overload
from common.consistency.RywData import RywData
from user.internal.backend.PropertiesObject import PropertiesObject

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

class CreateUserResponse:
    @overload
    def __init__(self, p0: dict, p1: PropertiesObject, p2: list, p3: RywData) -> None: ...
    @overload
    def __init__(self, p0: dict, p1: PropertiesObject, p2: list, p3: RywData, p4: int, p5: DefaultConstructorMarker) -> None: ...
    def getProperties(self) -> PropertiesObject: ...
    def getIdentities(self) -> dict: ...
    def getSubscriptions(self) -> list: ...
    def getRywData(self) -> RywData: ...

from typing import Any, ClassVar, overload

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

class IIdentityBackendService:
    def setAlias(self, p0: str, p1: str, p2: str, p3: dict, p4: str, p5: Continuation) -> Any: ...
    def deleteAlias(self, p0: str, p1: str, p2: str, p3: str, p4: str, p5: Continuation) -> Any: ...

    class DefaultImpls:
        @staticmethod
        def setAlias$default(p0: "IIdentityBackendService", p1: str, p2: str, p3: str, p4: dict, p5: str, p6: Continuation, p7: int, p8: Any) -> Any: ...
        @staticmethod
        def deleteAlias$default(p0: "IIdentityBackendService", p1: str, p2: str, p3: str, p4: str, p5: str, p6: Continuation, p7: int, p8: Any) -> Any: ...

from typing import Any, ClassVar, overload
from user.internal.backend.SubscriptionObject import SubscriptionObject

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

class ISubscriptionBackendService:
    def createSubscription(self, p0: str, p1: str, p2: str, p3: SubscriptionObject, p4: str, p5: Continuation) -> Any: ...
    def getIdentityFromSubscription(self, p0: str, p1: str, p2: Continuation) -> Any: ...
    def deleteSubscription(self, p0: str, p1: str, p2: str, p3: Continuation) -> Any: ...
    def updateSubscription(self, p0: str, p1: str, p2: SubscriptionObject, p3: str, p4: Continuation) -> Any: ...
    def transferSubscription(self, p0: str, p1: str, p2: str, p3: str, p4: str, p5: Continuation) -> Any: ...

    class DefaultImpls:
        @staticmethod
        def createSubscription$default(p0: "ISubscriptionBackendService", p1: str, p2: str, p3: str, p4: SubscriptionObject, p5: str, p6: Continuation, p7: int, p8: Any) -> Any: ...
        @staticmethod
        def updateSubscription$default(p0: "ISubscriptionBackendService", p1: str, p2: str, p3: SubscriptionObject, p4: str, p5: Continuation, p6: int, p7: Any) -> Any: ...
        @staticmethod
        def transferSubscription$default(p0: "ISubscriptionBackendService", p1: str, p2: str, p3: str, p4: str, p5: str, p6: Continuation, p7: int, p8: Any) -> Any: ...
        @staticmethod
        def deleteSubscription$default(p0: "ISubscriptionBackendService", p1: str, p2: str, p3: str, p4: Continuation, p5: int, p6: Any) -> Any: ...

from typing import Any, ClassVar, overload
from user.internal.backend.PropertiesDeltasObject import PropertiesDeltasObject
from user.internal.backend.PropertiesObject import PropertiesObject

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

class IUserBackendService:
    def createUser(self, p0: str, p1: dict, p2: list, p3: dict, p4: str, p5: Continuation) -> Any: ...
    def updateUser(self, p0: str, p1: str, p2: str, p3: PropertiesObject, p4: bool, p5: PropertiesDeltasObject, p6: str, p7: Continuation) -> Any: ...
    def getUser(self, p0: str, p1: str, p2: str, p3: str, p4: Continuation) -> Any: ...

    class DefaultImpls:
        @staticmethod
        def createUser$default(p0: "IUserBackendService", p1: str, p2: dict, p3: list, p4: dict, p5: str, p6: Continuation, p7: int, p8: Any) -> Any: ...
        @staticmethod
        def getUser$default(p0: "IUserBackendService", p1: str, p2: str, p3: str, p4: str, p5: Continuation, p6: int, p7: Any) -> Any: ...
        @staticmethod
        def updateUser$default(p0: "IUserBackendService", p1: str, p2: str, p3: str, p4: PropertiesObject, p5: bool, p6: PropertiesDeltasObject, p7: str, p8: Continuation, p9: int, p10: Any) -> Any: ...

from typing import Any, ClassVar, overload

class IdentityConstants:
    INSTANCE: ClassVar["IdentityConstants"]
    EXTERNAL_ID: ClassVar[str]
    ONESIGNAL_ID: ClassVar[str]

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class BigDecimal:
    """Forward declaration for ``java.math.BigDecimal``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.math.BigDecimal')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/math/BigDecimal.html
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

class PropertiesDeltasObject:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: BigDecimal, p3: list, p4: int, p5: DefaultConstructorMarker) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: BigDecimal, p3: list) -> None: ...
    def getSessionCount(self) -> int: ...
    def getAmountSpent(self) -> BigDecimal: ...
    def getPurchases(self) -> list: ...
    def getSessionTime(self) -> int: ...
    def getHasAtLeastOnePropertySet(self) -> bool: ...

from typing import Any, ClassVar, overload

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

class PropertiesObject:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: dict, p1: str, p2: str, p3: str, p4: float, p5: float) -> None: ...
    @overload
    def __init__(self, p0: dict, p1: str, p2: str, p3: str, p4: float, p5: float, p6: int, p7: DefaultConstructorMarker) -> None: ...
    def getCountry(self) -> str: ...
    def getTags(self) -> dict: ...
    def getHasAtLeastOnePropertySet(self) -> bool: ...
    def getTimezoneId(self) -> str: ...
    def getLatitude(self) -> float: ...
    def getLongitude(self) -> float: ...
    def getLanguage(self) -> str: ...

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class BigDecimal:
    """Forward declaration for ``java.math.BigDecimal``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.math.BigDecimal')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/math/BigDecimal.html
    """
    ...

class PurchaseObject:
    def __init__(self, p0: str, p1: str, p2: BigDecimal) -> None: ...
    def getSku(self) -> str: ...
    def getIso(self) -> str: ...
    def getAmount(self) -> BigDecimal: ...

from typing import Any, ClassVar, overload
from user.internal.backend.SubscriptionObjectType import SubscriptionObjectType

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

class SubscriptionObject:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: str, p1: SubscriptionObjectType, p2: str, p3: bool, p4: int, p5: str, p6: str, p7: str, p8: bool, p9: int, p10: str, p11: str, p12: int, p13: DefaultConstructorMarker) -> None: ...
    @overload
    def __init__(self, p0: str, p1: SubscriptionObjectType, p2: str, p3: bool, p4: int, p5: str, p6: str, p7: str, p8: bool, p9: int, p10: str, p11: str) -> None: ...
    def getId(self) -> str: ...
    def getType(self) -> SubscriptionObjectType: ...
    def getNetType(self) -> int: ...
    def getAppVersion(self) -> str: ...
    def getNotificationTypes(self) -> int: ...
    def getEnabled(self) -> bool: ...
    def getRooted(self) -> bool: ...
    def getDeviceModel(self) -> str: ...
    def getToken(self) -> str: ...
    def getSdk(self) -> str: ...
    def getDeviceOS(self) -> str: ...
    def getCarrier(self) -> str: ...

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

class SubscriptionObjectType:
    IOS_PUSH: ClassVar["SubscriptionObjectType"]
    ANDROID_PUSH: ClassVar["SubscriptionObjectType"]
    FIREOS_PUSH: ClassVar["SubscriptionObjectType"]
    CHROME_EXTENSION: ClassVar["SubscriptionObjectType"]
    CHROME_PUSH: ClassVar["SubscriptionObjectType"]
    WINDOWS_PUSH: ClassVar["SubscriptionObjectType"]
    SAFARI_PUSH: ClassVar["SubscriptionObjectType"]
    SAFARI_PUSH_LEGACY: ClassVar["SubscriptionObjectType"]
    FIREFOX_PUSH: ClassVar["SubscriptionObjectType"]
    MACOS_PUSH: ClassVar["SubscriptionObjectType"]
    EMAIL: ClassVar["SubscriptionObjectType"]
    HUAWEI_PUSH: ClassVar["SubscriptionObjectType"]
    SMS: ClassVar["SubscriptionObjectType"]
    Companion: ClassVar[Any]
    IOS_PUSH: ClassVar["SubscriptionObjectType"]
    ANDROID_PUSH: ClassVar["SubscriptionObjectType"]
    FIREOS_PUSH: ClassVar["SubscriptionObjectType"]
    CHROME_EXTENSION: ClassVar["SubscriptionObjectType"]
    CHROME_PUSH: ClassVar["SubscriptionObjectType"]
    WINDOWS_PUSH: ClassVar["SubscriptionObjectType"]
    SAFARI_PUSH: ClassVar["SubscriptionObjectType"]
    SAFARI_PUSH_LEGACY: ClassVar["SubscriptionObjectType"]
    FIREFOX_PUSH: ClassVar["SubscriptionObjectType"]
    MACOS_PUSH: ClassVar["SubscriptionObjectType"]
    EMAIL: ClassVar["SubscriptionObjectType"]
    HUAWEI_PUSH: ClassVar["SubscriptionObjectType"]
    SMS: ClassVar["SubscriptionObjectType"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "SubscriptionObjectType": ...
    def getValue(self) -> str: ...
    @staticmethod
    def getEntries() -> EnumEntries: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...
        def fromString(self, p0: str) -> "SubscriptionObjectType": ...
        def fromDeviceType(self, p0: Any) -> "SubscriptionObjectType": ...

        class WhenMappings:
            $EnumSwitchMapping$0: ClassVar[Any]


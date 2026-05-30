from typing import Any, ClassVar, overload
from core.internal.application.IApplicationService import IApplicationService
from core.internal.config.impl.IdentityVerificationService import IdentityVerificationService
from core.internal.device.IDeviceService import IDeviceService
from user.internal.customEvents.ICustomEventBackendService import ICustomEventBackendService
from user.internal.jwt.JwtTokenStore import JwtTokenStore

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
class DefaultConstructorMarker:
    """Forward declaration for ``kotlin.jvm.internal.DefaultConstructorMarker``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.internal.DefaultConstructorMarker')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/internal/DefaultConstructorMarker/
    """
    ...

class CustomEventOperationExecutor:
    Companion: ClassVar[Any]
    CUSTOM_EVENT: ClassVar[str]
    def __init__(self, p0: ICustomEventBackendService, p1: IApplicationService, p2: IDeviceService, p3: JwtTokenStore, p4: IdentityVerificationService) -> None: ...
    def execute(self, p0: list, p1: Continuation) -> Any: ...
    def getOperations(self) -> list: ...
    @staticmethod
    def access$getDeviceService$p(p0: "CustomEventOperationExecutor") -> IDeviceService: ...
    @staticmethod
    def access$getApplicationService$p(p0: "CustomEventOperationExecutor") -> IApplicationService: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

    class WhenMappings:
        $EnumSwitchMapping$0: ClassVar[Any]

from typing import Any, ClassVar, overload
from core.internal.config.impl.IdentityVerificationService import IdentityVerificationService
from core.internal.operations.Operation import Operation
from user.internal.jwt.JwtTokenStore import JwtTokenStore
from user.internal.operations.impl.executors.IvBackendParams import IvBackendParams

class ExecutorsIvExtensionsKt:
    @staticmethod
    def resolveBackendParams(p0: Operation, p1: str, p2: JwtTokenStore, p3: IdentityVerificationService) -> IvBackendParams: ...
    @staticmethod
    def resolveIvBackendParams(p0: Operation, p1: str, p2: JwtTokenStore, p3: bool) -> IvBackendParams: ...
    @staticmethod
    def resolveIvJwt(p0: Operation, p1: JwtTokenStore, p2: bool) -> str: ...
    @staticmethod
    def shouldFailLoginUserFromSubscription(p0: bool) -> bool: ...
    @staticmethod
    def resolveJwt(p0: Operation, p1: JwtTokenStore, p2: IdentityVerificationService) -> str: ...

from typing import Any, ClassVar, overload
from core.internal.config.impl.IdentityVerificationService import IdentityVerificationService
from user.internal.backend.IIdentityBackendService import IIdentityBackendService
from user.internal.builduser.IRebuildUserService import IRebuildUserService
from user.internal.identity.IdentityModelStore import IdentityModelStore
from user.internal.jwt.JwtTokenStore import JwtTokenStore
from user.internal.operations.impl.states.NewRecordsState import NewRecordsState

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
class DefaultConstructorMarker:
    """Forward declaration for ``kotlin.jvm.internal.DefaultConstructorMarker``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.internal.DefaultConstructorMarker')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/internal/DefaultConstructorMarker/
    """
    ...

class IdentityOperationExecutor:
    Companion: ClassVar[Any]
    SET_ALIAS: ClassVar[str]
    DELETE_ALIAS: ClassVar[str]
    def __init__(self, p0: IIdentityBackendService, p1: IdentityModelStore, p2: IRebuildUserService, p3: NewRecordsState, p4: JwtTokenStore, p5: IdentityVerificationService) -> None: ...
    def execute(self, p0: list, p1: Continuation) -> Any: ...
    def getOperations(self) -> list: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

    class WhenMappings:
        $EnumSwitchMapping$0: ClassVar[Any]

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

class IvBackendParams:
    Companion: ClassVar[Any]
    def __init__(self, p0: str, p1: str, p2: str) -> None: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def copy(self, p0: str, p1: str, p2: str) -> "IvBackendParams": ...
    def getAliasLabel(self) -> str: ...
    def getAliasValue(self) -> str: ...
    def component1(self) -> str: ...
    def component2(self) -> str: ...
    @staticmethod
    def copy$default(p0: "IvBackendParams", p1: str, p2: str, p3: str, p4: int, p5: Any) -> "IvBackendParams": ...
    def component3(self) -> str: ...
    def getJwt(self) -> str: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...
        def legacyFor(self, p0: str) -> "IvBackendParams": ...

from typing import Any, ClassVar, overload
from core.internal.config.impl.IdentityVerificationService import IdentityVerificationService
from user.internal.backend.ISubscriptionBackendService import ISubscriptionBackendService
from user.internal.identity.IdentityModelStore import IdentityModelStore
from user.internal.operations.LoginUserFromSubscriptionOperation import LoginUserFromSubscriptionOperation
from user.internal.properties.PropertiesModelStore import PropertiesModelStore

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
class DefaultConstructorMarker:
    """Forward declaration for ``kotlin.jvm.internal.DefaultConstructorMarker``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.internal.DefaultConstructorMarker')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/internal/DefaultConstructorMarker/
    """
    ...

class LoginUserFromSubscriptionOperationExecutor:
    Companion: ClassVar[Any]
    LOGIN_USER_FROM_SUBSCRIPTION_USER: ClassVar[str]
    def __init__(self, p0: ISubscriptionBackendService, p1: IdentityModelStore, p2: PropertiesModelStore, p3: IdentityVerificationService) -> None: ...
    def execute(self, p0: list, p1: Continuation) -> Any: ...
    def getOperations(self) -> list: ...
    @staticmethod
    def access$loginUser(p0: "LoginUserFromSubscriptionOperationExecutor", p1: LoginUserFromSubscriptionOperation, p2: Continuation) -> Any: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

    class WhenMappings:
        $EnumSwitchMapping$0: ClassVar[Any]

from typing import Any, ClassVar, overload
from common.consistency.models.IConsistencyManager import IConsistencyManager
from core.internal.application.IApplicationService import IApplicationService
from core.internal.config.ConfigModelStore import ConfigModelStore
from core.internal.config.impl.IdentityVerificationService import IdentityVerificationService
from core.internal.device.IDeviceService import IDeviceService
from core.internal.language.ILanguageContext import ILanguageContext
from user.internal.backend.IUserBackendService import IUserBackendService
from user.internal.identity.IdentityModelStore import IdentityModelStore
from user.internal.jwt.JwtTokenStore import JwtTokenStore
from user.internal.operations.LoginUserOperation import LoginUserOperation
from user.internal.operations.impl.executors.IdentityOperationExecutor import IdentityOperationExecutor
from user.internal.properties.PropertiesModelStore import PropertiesModelStore
from user.internal.subscriptions.SubscriptionModelStore import SubscriptionModelStore

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
class DefaultConstructorMarker:
    """Forward declaration for ``kotlin.jvm.internal.DefaultConstructorMarker``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.internal.DefaultConstructorMarker')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/internal/DefaultConstructorMarker/
    """
    ...

class LoginUserOperationExecutor:
    Companion: ClassVar[Any]
    LOGIN_USER: ClassVar[str]
    def __init__(self, p0: IdentityOperationExecutor, p1: IApplicationService, p2: IDeviceService, p3: IUserBackendService, p4: IdentityModelStore, p5: PropertiesModelStore, p6: SubscriptionModelStore, p7: ConfigModelStore, p8: ILanguageContext, p9: JwtTokenStore, p10: IdentityVerificationService, p11: IConsistencyManager) -> None: ...
    def execute(self, p0: list, p1: Continuation) -> Any: ...
    def getOperations(self) -> list: ...
    @staticmethod
    def access$loginUser(p0: "LoginUserOperationExecutor", p1: LoginUserOperation, p2: list, p3: Continuation) -> Any: ...
    @staticmethod
    def access$createUser(p0: "LoginUserOperationExecutor", p1: LoginUserOperation, p2: list, p3: Continuation) -> Any: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

    class WhenMappings:
        $EnumSwitchMapping$0: ClassVar[Any]
        $EnumSwitchMapping$1: ClassVar[Any]
        $EnumSwitchMapping$2: ClassVar[Any]

from typing import Any, ClassVar, overload
from user.internal.backend.PropertiesObject import PropertiesObject
from user.internal.operations.DeleteTagOperation import DeleteTagOperation
from user.internal.operations.SetPropertyOperation import SetPropertyOperation
from user.internal.operations.SetTagOperation import SetTagOperation

class PropertyOperationHelper:
    INSTANCE: ClassVar["PropertyOperationHelper"]
    @overload
    def createPropertiesFromOperation(self, p0: SetTagOperation, p1: PropertiesObject) -> PropertiesObject: ...
    @overload
    def createPropertiesFromOperation(self, p0: SetPropertyOperation, p1: PropertiesObject) -> PropertiesObject: ...
    @overload
    def createPropertiesFromOperation(self, p0: DeleteTagOperation, p1: PropertiesObject) -> PropertiesObject: ...

from typing import Any, ClassVar, overload
from core.internal.config.ConfigModelStore import ConfigModelStore
from core.internal.config.impl.IdentityVerificationService import IdentityVerificationService
from user.internal.backend.IUserBackendService import IUserBackendService
from user.internal.builduser.IRebuildUserService import IRebuildUserService
from user.internal.identity.IdentityModelStore import IdentityModelStore
from user.internal.jwt.JwtTokenStore import JwtTokenStore
from user.internal.operations.RefreshUserOperation import RefreshUserOperation
from user.internal.operations.impl.states.NewRecordsState import NewRecordsState
from user.internal.properties.PropertiesModelStore import PropertiesModelStore
from user.internal.subscriptions.SubscriptionModelStore import SubscriptionModelStore

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
class DefaultConstructorMarker:
    """Forward declaration for ``kotlin.jvm.internal.DefaultConstructorMarker``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.internal.DefaultConstructorMarker')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/internal/DefaultConstructorMarker/
    """
    ...

class RefreshUserOperationExecutor:
    Companion: ClassVar[Any]
    REFRESH_USER: ClassVar[str]
    def __init__(self, p0: IUserBackendService, p1: IdentityModelStore, p2: PropertiesModelStore, p3: SubscriptionModelStore, p4: ConfigModelStore, p5: IRebuildUserService, p6: NewRecordsState, p7: JwtTokenStore, p8: IdentityVerificationService) -> None: ...
    def execute(self, p0: list, p1: Continuation) -> Any: ...
    def getOperations(self) -> list: ...
    @staticmethod
    def access$getUser(p0: "RefreshUserOperationExecutor", p1: RefreshUserOperation, p2: Continuation) -> Any: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

    class WhenMappings:
        $EnumSwitchMapping$0: ClassVar[Any]
        $EnumSwitchMapping$1: ClassVar[Any]

from typing import Any, ClassVar, overload
from common.consistency.models.IConsistencyManager import IConsistencyManager
from core.internal.application.IApplicationService import IApplicationService
from core.internal.config.ConfigModelStore import ConfigModelStore
from core.internal.config.impl.IdentityVerificationService import IdentityVerificationService
from core.internal.device.IDeviceService import IDeviceService
from user.internal.backend.ISubscriptionBackendService import ISubscriptionBackendService
from user.internal.builduser.IRebuildUserService import IRebuildUserService
from user.internal.jwt.JwtTokenStore import JwtTokenStore
from user.internal.operations.CreateSubscriptionOperation import CreateSubscriptionOperation
from user.internal.operations.DeleteSubscriptionOperation import DeleteSubscriptionOperation
from user.internal.operations.TransferSubscriptionOperation import TransferSubscriptionOperation
from user.internal.operations.UpdateSubscriptionOperation import UpdateSubscriptionOperation
from user.internal.operations.impl.states.NewRecordsState import NewRecordsState
from user.internal.subscriptions.SubscriptionModelStore import SubscriptionModelStore

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
class DefaultConstructorMarker:
    """Forward declaration for ``kotlin.jvm.internal.DefaultConstructorMarker``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.internal.DefaultConstructorMarker')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/internal/DefaultConstructorMarker/
    """
    ...

class SubscriptionOperationExecutor:
    Companion: ClassVar[Any]
    CREATE_SUBSCRIPTION: ClassVar[str]
    UPDATE_SUBSCRIPTION: ClassVar[str]
    DELETE_SUBSCRIPTION: ClassVar[str]
    TRANSFER_SUBSCRIPTION: ClassVar[str]
    def __init__(self, p0: ISubscriptionBackendService, p1: IDeviceService, p2: IApplicationService, p3: SubscriptionModelStore, p4: ConfigModelStore, p5: IRebuildUserService, p6: NewRecordsState, p7: IConsistencyManager, p8: JwtTokenStore, p9: IdentityVerificationService) -> None: ...
    def execute(self, p0: list, p1: Continuation) -> Any: ...
    def getOperations(self) -> list: ...
    @staticmethod
    def access$createSubscription(p0: "SubscriptionOperationExecutor", p1: CreateSubscriptionOperation, p2: list, p3: Continuation) -> Any: ...
    @staticmethod
    def access$updateExistingSubscriptionFromCreate(p0: "SubscriptionOperationExecutor", p1: CreateSubscriptionOperation, p2: list, p3: Continuation) -> Any: ...
    @staticmethod
    def access$updateSubscription(p0: "SubscriptionOperationExecutor", p1: UpdateSubscriptionOperation, p2: list, p3: Continuation) -> Any: ...
    @staticmethod
    def access$transferSubscription(p0: "SubscriptionOperationExecutor", p1: TransferSubscriptionOperation, p2: Continuation) -> Any: ...
    @staticmethod
    def access$deleteSubscription(p0: "SubscriptionOperationExecutor", p1: DeleteSubscriptionOperation, p2: Continuation) -> Any: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

    class WhenMappings:
        $EnumSwitchMapping$0: ClassVar[Any]
        $EnumSwitchMapping$1: ClassVar[Any]

from typing import Any, ClassVar, overload
from common.consistency.models.IConsistencyManager import IConsistencyManager
from core.internal.config.impl.IdentityVerificationService import IdentityVerificationService
from user.internal.backend.IUserBackendService import IUserBackendService
from user.internal.builduser.IRebuildUserService import IRebuildUserService
from user.internal.identity.IdentityModelStore import IdentityModelStore
from user.internal.jwt.JwtTokenStore import JwtTokenStore
from user.internal.operations.impl.states.NewRecordsState import NewRecordsState
from user.internal.properties.PropertiesModelStore import PropertiesModelStore

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
class DefaultConstructorMarker:
    """Forward declaration for ``kotlin.jvm.internal.DefaultConstructorMarker``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.internal.DefaultConstructorMarker')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/internal/DefaultConstructorMarker/
    """
    ...

class UpdateUserOperationExecutor:
    Companion: ClassVar[Any]
    SET_TAG: ClassVar[str]
    DELETE_TAG: ClassVar[str]
    SET_PROPERTY: ClassVar[str]
    TRACK_SESSION_START: ClassVar[str]
    TRACK_SESSION_END: ClassVar[str]
    TRACK_PURCHASE: ClassVar[str]
    def __init__(self, p0: IUserBackendService, p1: IdentityModelStore, p2: PropertiesModelStore, p3: IRebuildUserService, p4: NewRecordsState, p5: IConsistencyManager, p6: JwtTokenStore, p7: IdentityVerificationService) -> None: ...
    def execute(self, p0: list, p1: Continuation) -> Any: ...
    def getOperations(self) -> list: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

    class WhenMappings:
        $EnumSwitchMapping$0: ClassVar[Any]


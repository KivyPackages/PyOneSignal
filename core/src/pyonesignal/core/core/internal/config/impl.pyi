from typing import Any, ClassVar, overload
from common.modeling.Model import Model
from common.modeling.ModelChangedArgs import ModelChangedArgs
from core.internal.backend.IParamsBackendService import IParamsBackendService
from core.internal.config.ConfigModel import ConfigModel
from core.internal.config.ConfigModelStore import ConfigModelStore
from user.internal.subscriptions.ISubscriptionManager import ISubscriptionManager

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

class ConfigModelStoreListener:
    Companion: ClassVar[Any]
    def __init__(self, p0: ConfigModelStore, p1: IParamsBackendService, p2: ISubscriptionManager) -> None: ...
    def start(self) -> None: ...
    def onModelUpdated(self, p0: ModelChangedArgs, p1: str) -> None: ...
    @overload
    def onModelReplaced(self, p0: Model, p1: str) -> None: ...
    @overload
    def onModelReplaced(self, p0: ConfigModel, p1: str) -> None: ...
    @staticmethod
    def access$get_paramsBackendService$p(p0: "ConfigModelStoreListener") -> IParamsBackendService: ...
    @staticmethod
    def access$get_configModelStore$p(p0: "ConfigModelStoreListener") -> ConfigModelStore: ...
    @staticmethod
    def access$get_subscriptionManager$p(p0: "ConfigModelStoreListener") -> ISubscriptionManager: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

from typing import Any, ClassVar, overload
from common.modeling.Model import Model
from common.modeling.ModelChangedArgs import ModelChangedArgs
from core.internal.application.IApplicationService import IApplicationService
from core.internal.backend.IFeatureFlagsBackendService import IFeatureFlagsBackendService
from core.internal.config.ConfigModel import ConfigModel
from core.internal.config.ConfigModelStore import ConfigModelStore

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Job:
    """Forward declaration for ``kotlinx.coroutines.Job``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlinx.coroutines.Job')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlinx/coroutines/Job/
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
class DefaultConstructorMarker:
    """Forward declaration for ``kotlin.jvm.internal.DefaultConstructorMarker``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.internal.DefaultConstructorMarker')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/internal/DefaultConstructorMarker/
    """
    ...

class FeatureFlagsRefreshService:
    Companion: ClassVar[Any]
    def __init__(self, p0: IApplicationService, p1: ConfigModelStore, p2: IFeatureFlagsBackendService) -> None: ...
    def start(self) -> None: ...
    def onModelUpdated(self, p0: ModelChangedArgs, p1: str) -> None: ...
    @overload
    def onModelReplaced(self, p0: Model, p1: str) -> None: ...
    @overload
    def onModelReplaced(self, p0: ConfigModel, p1: str) -> None: ...
    def onFocus(self, p0: bool) -> None: ...
    def onUnfocused(self) -> None: ...
    def getRefreshIntervalMs$com_onesignal_core(self) -> int: ...
    def setRefreshIntervalMs$com_onesignal_core(self, p0: int) -> None: ...
    @staticmethod
    def access$restartForegroundPolling(p0: "FeatureFlagsRefreshService") -> None: ...
    @staticmethod
    def access$getPollJob$p(p0: "FeatureFlagsRefreshService") -> Job: ...
    @staticmethod
    def access$setPollJob$p(p0: "FeatureFlagsRefreshService", p1: Job) -> None: ...
    @staticmethod
    def access$setPollingAppId$p(p0: "FeatureFlagsRefreshService", p1: str) -> None: ...
    @staticmethod
    def access$fetchAndApply(p0: "FeatureFlagsRefreshService", p1: str, p2: Continuation) -> Any: ...
    @staticmethod
    def access$getApplicationService$p(p0: "FeatureFlagsRefreshService") -> IApplicationService: ...
    @staticmethod
    def access$getConfigModelStore$p(p0: "FeatureFlagsRefreshService") -> ConfigModelStore: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

from typing import Any, ClassVar, overload
from common.modeling.Model import Model
from common.modeling.ModelChangedArgs import ModelChangedArgs
from core.internal.config.ConfigModel import ConfigModel
from core.internal.config.ConfigModelStore import ConfigModelStore
from core.internal.features.IFeatureManager import IFeatureManager

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Function1:
    """Forward declaration for ``kotlin.jvm.functions.Function1``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.functions.Function1')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/functions/Function1/
    """
    ...

class IdentityVerificationService:
    def __init__(self, p0: IFeatureManager, p1: ConfigModelStore) -> None: ...
    def start(self) -> None: ...
    def onModelUpdated(self, p0: ModelChangedArgs, p1: str) -> None: ...
    @overload
    def onModelReplaced(self, p0: Model, p1: str) -> None: ...
    @overload
    def onModelReplaced(self, p0: ConfigModel, p1: str) -> None: ...
    def getIvBehaviorActive(self) -> bool: ...
    def getNewCodePathsRun(self) -> bool: ...
    def setOnJwtConfigHydratedHandler(self, p0: Function1) -> None: ...


from typing import Any, ClassVar, overload
from common.modeling.Model import Model
from core.internal.config.ConfigModelStore import ConfigModelStore
from core.internal.operations.IOperationRepo import IOperationRepo
from core.internal.operations.Operation import Operation
from user.internal.identity.IdentityModel import IdentityModel
from user.internal.identity.IdentityModelStore import IdentityModelStore

class IdentityModelStoreListener:
    def __init__(self, p0: IdentityModelStore, p1: IOperationRepo, p2: ConfigModelStore) -> None: ...
    @overload
    def getUpdateOperation(self, p0: Model, p1: str, p2: str, p3: Any, p4: Any) -> Operation: ...
    @overload
    def getUpdateOperation(self, p0: IdentityModel, p1: str, p2: str, p3: Any, p4: Any) -> Operation: ...
    @overload
    def getReplaceOperation(self, p0: Model) -> Operation: ...
    @overload
    def getReplaceOperation(self, p0: IdentityModel) -> Operation: ...

from typing import Any, ClassVar, overload
from common.modeling.Model import Model
from core.internal.config.ConfigModelStore import ConfigModelStore
from core.internal.operations.IOperationRepo import IOperationRepo
from core.internal.operations.Operation import Operation
from user.internal.identity.IdentityModelStore import IdentityModelStore
from user.internal.properties.PropertiesModel import PropertiesModel
from user.internal.properties.PropertiesModelStore import PropertiesModelStore

class PropertiesModelStoreListener:
    def __init__(self, p0: PropertiesModelStore, p1: IOperationRepo, p2: ConfigModelStore, p3: IdentityModelStore) -> None: ...
    @overload
    def getUpdateOperation(self, p0: Model, p1: str, p2: str, p3: Any, p4: Any) -> Operation: ...
    @overload
    def getUpdateOperation(self, p0: PropertiesModel, p1: str, p2: str, p3: Any, p4: Any) -> Operation: ...
    @overload
    def getReplaceOperation(self, p0: Model) -> Operation: ...
    @overload
    def getReplaceOperation(self, p0: PropertiesModel) -> Operation: ...

from typing import Any, ClassVar, overload
from common.modeling.Model import Model
from core.internal.config.ConfigModelStore import ConfigModelStore
from core.internal.operations.IOperationRepo import IOperationRepo
from core.internal.operations.Operation import Operation
from user.internal.identity.IdentityModelStore import IdentityModelStore
from user.internal.subscriptions.SubscriptionModel import SubscriptionModel
from user.internal.subscriptions.SubscriptionModelStore import SubscriptionModelStore

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
class Pair:
    """Forward declaration for ``kotlin.Pair``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.Pair')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/Pair/
    """
    ...

class SubscriptionModelStoreListener:
    Companion: ClassVar[Any]
    def __init__(self, p0: SubscriptionModelStore, p1: IOperationRepo, p2: IdentityModelStore, p3: ConfigModelStore) -> None: ...
    @overload
    def getUpdateOperation(self, p0: Model, p1: str, p2: str, p3: Any, p4: Any) -> Operation: ...
    @overload
    def getUpdateOperation(self, p0: SubscriptionModel, p1: str, p2: str, p3: Any, p4: Any) -> Operation: ...
    @overload
    def getAddOperation(self, p0: Model) -> Operation: ...
    @overload
    def getAddOperation(self, p0: SubscriptionModel) -> Operation: ...
    @overload
    def getRemoveOperation(self, p0: SubscriptionModel) -> Operation: ...
    @overload
    def getRemoveOperation(self, p0: Model) -> Operation: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...
        def getSubscriptionEnabledAndStatus(self, p0: SubscriptionModel) -> Pair: ...


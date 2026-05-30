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

class FeatureActivationMode:
    IMMEDIATE: ClassVar["FeatureActivationMode"]
    APP_STARTUP: ClassVar["FeatureActivationMode"]
    IMMEDIATE: ClassVar["FeatureActivationMode"]
    APP_STARTUP: ClassVar["FeatureActivationMode"]
    @staticmethod
    def getEntries() -> EnumEntries: ...
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "FeatureActivationMode": ...

from typing import Any, ClassVar, overload
from core.internal.features.FeatureActivationMode import FeatureActivationMode

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

class FeatureFlag:
    SDK_BACKGROUND_THREADING: ClassVar["FeatureFlag"]
    SDK_IDENTITY_VERIFICATION: ClassVar["FeatureFlag"]
    SDK_BACKGROUND_THREADING: ClassVar["FeatureFlag"]
    SDK_IDENTITY_VERIFICATION: ClassVar["FeatureFlag"]
    @staticmethod
    def getEntries() -> EnumEntries: ...
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "FeatureFlag": ...
    def getKey(self) -> str: ...
    def getActivationMode(self) -> FeatureActivationMode: ...
    def isEnabledIn(self, p0: set) -> bool: ...

from typing import Any, ClassVar, overload
from common.modeling.Model import Model
from common.modeling.ModelChangedArgs import ModelChangedArgs
from core.internal.config.ConfigModel import ConfigModel
from core.internal.config.ConfigModelStore import ConfigModelStore
from core.internal.features.FeatureFlag import FeatureFlag

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

class FeatureManager:
    Companion: ClassVar[Any]
    def __init__(self, p0: ConfigModelStore) -> None: ...
    def isEnabled(self, p0: FeatureFlag) -> bool: ...
    def onModelUpdated(self, p0: ModelChangedArgs, p1: str) -> None: ...
    @overload
    def onModelReplaced(self, p0: ConfigModel, p1: str) -> None: ...
    @overload
    def onModelReplaced(self, p0: Model, p1: str) -> None: ...
    def enabledFeatureKeys(self) -> list: ...
    def remoteFeatureFlagMetadata(self) -> dict: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

    class WhenMappings:
        $EnumSwitchMapping$0: ClassVar[Any]
        $EnumSwitchMapping$1: ClassVar[Any]

from typing import Any, ClassVar, overload
from core.internal.features.FeatureFlag import FeatureFlag

class IFeatureManager:
    def isEnabled(self, p0: FeatureFlag) -> bool: ...
    def enabledFeatureKeys(self) -> list: ...
    def remoteFeatureFlagMetadata(self) -> dict: ...


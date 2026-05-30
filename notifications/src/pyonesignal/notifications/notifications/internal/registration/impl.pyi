from typing import Any, ClassVar, overload
from android.app.Activity import Activity
from pyonesignal.core.internal.application.IApplicationService import IApplicationService
from pyonesignal.core.internal.config.ConfigModelStore import ConfigModelStore
from pyonesignal.core.internal.device.IDeviceService import IDeviceService

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

class GooglePlayServicesUpgradePrompt:
    Companion: ClassVar[Any]
    def __init__(self, p0: IApplicationService, p1: IDeviceService, p2: ConfigModelStore) -> None: ...
    @staticmethod
    def access$get_configModelStore$p(p0: "GooglePlayServicesUpgradePrompt") -> ConfigModelStore: ...
    def showUpdateGPSDialog(self, p0: Continuation) -> Any: ...
    @staticmethod
    def access$openPlayStoreToApp(p0: "GooglePlayServicesUpgradePrompt", p1: Activity) -> None: ...
    @staticmethod
    def access$get_applicationService$p(p0: "GooglePlayServicesUpgradePrompt") -> IApplicationService: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

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

class IPushRegistratorCallback:
    def fireCallback(self, p0: str, p1: Continuation) -> Any: ...

from typing import Any, ClassVar, overload
from pyonesignal.core.internal.application.IApplicationService import IApplicationService
from pyonesignal.core.threading.WaiterWithValue import WaiterWithValue

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

class PushRegistratorADM:
    def __init__(self, p0: IApplicationService) -> None: ...
    def registerForPush(self, p0: Continuation) -> Any: ...
    def fireCallback(self, p0: str, p1: Continuation) -> Any: ...
    @staticmethod
    def access$getWaiter$p(p0: "PushRegistratorADM") -> WaiterWithValue: ...

from typing import Any, ClassVar, overload
from notifications.internal.registration.impl.GooglePlayServicesUpgradePrompt import GooglePlayServicesUpgradePrompt
from pyonesignal.core.internal.config.ConfigModelStore import ConfigModelStore
from pyonesignal.core.internal.device.IDeviceService import IDeviceService

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

class PushRegistratorAbstractGoogle:
    Companion: ClassVar[Any]
    def __init__(self, p0: IDeviceService, p1: ConfigModelStore, p2: GooglePlayServicesUpgradePrompt) -> None: ...
    def registerForPush(self, p0: Continuation) -> Any: ...
    def getToken(self, p0: str, p1: Continuation) -> Any: ...
    def fireCallback(self, p0: str, p1: Continuation) -> Any: ...
    def getProviderName(self) -> str: ...
    @staticmethod
    def access$internalRegisterForPush(p0: "PushRegistratorAbstractGoogle", p1: str, p2: Continuation) -> Any: ...
    @staticmethod
    def access$registerInBackground(p0: "PushRegistratorAbstractGoogle", p1: str, p2: Continuation) -> Any: ...
    @staticmethod
    def access$attemptRegistration(p0: "PushRegistratorAbstractGoogle", p1: str, p2: int, p3: Continuation) -> Any: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

from typing import Any, ClassVar, overload
from notifications.internal.registration.impl.GooglePlayServicesUpgradePrompt import GooglePlayServicesUpgradePrompt
from pyonesignal.core.internal.application.IApplicationService import IApplicationService
from pyonesignal.core.internal.config.ConfigModelStore import ConfigModelStore
from pyonesignal.core.internal.device.IDeviceService import IDeviceService

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

class PushRegistratorFCM:
    Companion: ClassVar[Any]
    Companion: ClassVar[Any]
    def __init__(self, p0: ConfigModelStore, p1: IApplicationService, p2: GooglePlayServicesUpgradePrompt, p3: IDeviceService) -> None: ...
    def getToken(self, p0: str, p1: Continuation) -> Any: ...
    def getProviderName(self) -> str: ...
    def get_configModelStore(self) -> ConfigModelStore: ...
    def set_configModelStore(self, p0: ConfigModelStore) -> None: ...
    def get_applicationService(self) -> IApplicationService: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

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

class PushRegistratorNone:
    def __init__(self) -> None: ...
    def registerForPush(self, p0: Continuation) -> Any: ...
    def fireCallback(self, p0: str, p1: Continuation) -> Any: ...


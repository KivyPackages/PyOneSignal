from typing import Any, ClassVar, overload
from common.services.ServiceProvider import ServiceProvider
from common.services.ServiceRegistration import ServiceRegistration

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

class IServiceBuilder:
    @overload
    def register(self, p0: Any) -> ServiceRegistration: ...
    @overload
    def register(self, p0: Function1) -> ServiceRegistration: ...
    @overload
    def register(self, p0: type) -> ServiceRegistration: ...
    def build(self) -> ServiceProvider: ...

from typing import Any, ClassVar, overload

class IServiceProvider:
    def getService(self, p0: type) -> Any: ...
    def getServiceOrNull(self, p0: type) -> Any: ...
    def hasService(self, p0: type) -> bool: ...
    def getAllServices(self, p0: type) -> list: ...

from typing import Any, ClassVar, overload
from common.services.ServiceProvider import ServiceProvider
from common.services.ServiceRegistration import ServiceRegistration

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

class ServiceBuilder:
    def __init__(self) -> None: ...
    @overload
    def register(self, p0: Any) -> ServiceRegistration: ...
    @overload
    def register(self, p0: Function1) -> ServiceRegistration: ...
    @overload
    def register(self, p0: type) -> ServiceRegistration: ...
    @overload
    def register(self) -> ServiceRegistration: ...
    def build(self) -> ServiceProvider: ...

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

class ServiceProvider:
    Companion: ClassVar[Any]
    def __init__(self, p0: list) -> None: ...
    def getService(self, p0: type) -> Any: ...
    def getServiceOrNull(self, p0: type) -> Any: ...
    def hasService(self, p0: type) -> bool: ...
    def getAllServices(self, p0: type) -> list: ...
    def hasService$com_onesignal_core(self) -> bool: ...
    def getAllServices$com_onesignal_core(self) -> list: ...
    def getService$com_onesignal_core(self) -> Any: ...
    def getServiceOrNull$com_onesignal_core(self) -> Any: ...
    @staticmethod
    def access$getIndent$cp() -> str: ...
    @staticmethod
    def access$setIndent$cp(p0: str) -> None: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...
        def getIndent(self) -> str: ...
        def setIndent(self, p0: str) -> None: ...

from typing import Any, ClassVar, overload
from common.services.IServiceProvider import IServiceProvider

class ServiceRegistration:
    def __init__(self) -> None: ...
    def resolve(self, p0: IServiceProvider) -> Any: ...
    @overload
    def provides(self, p0: type) -> "ServiceRegistration": ...
    @overload
    def provides(self) -> "ServiceRegistration": ...
    def getServices(self) -> set: ...

from typing import Any, ClassVar, overload
from common.services.IServiceProvider import IServiceProvider

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

class ServiceRegistrationLambda:
    def __init__(self, p0: Function1) -> None: ...
    def resolve(self, p0: IServiceProvider) -> Any: ...

from typing import Any, ClassVar, overload
from common.services.IServiceProvider import IServiceProvider

class ServiceRegistrationReflection:
    def __init__(self, p0: type) -> None: ...
    def resolve(self, p0: IServiceProvider) -> Any: ...

from typing import Any, ClassVar, overload
from common.services.IServiceProvider import IServiceProvider

class ServiceRegistrationSingleton:
    def __init__(self, p0: Any) -> None: ...
    def resolve(self, p0: IServiceProvider) -> Any: ...


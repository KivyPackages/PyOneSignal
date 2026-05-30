from typing import Any, ClassVar, overload
from common.services.ServiceBuilder import ServiceBuilder

class CoreModule:
    def __init__(self) -> None: ...
    def register(self, p0: ServiceBuilder) -> None: ...

from typing import Any, ClassVar, overload

class BuildConfig:
    DEBUG: ClassVar[bool]
    LIBRARY_PACKAGE_NAME: ClassVar[str]
    BUILD_TYPE: ClassVar[str]
    SDK_VERSION: ClassVar[str]
    def __init__(self) -> None: ...


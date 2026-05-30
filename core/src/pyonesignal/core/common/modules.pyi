from typing import Any, ClassVar, overload
from common.services.ServiceBuilder import ServiceBuilder

class IModule:
    def register(self, p0: ServiceBuilder) -> None: ...


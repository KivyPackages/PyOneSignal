from typing import Any, ClassVar, overload

class IBootstrapService:
    def bootstrap(self) -> None: ...

from typing import Any, ClassVar, overload

class IStartableService:
    def start(self) -> None: ...

from typing import Any, ClassVar, overload
from common.services.ServiceProvider import ServiceProvider

class StartupService:
    def __init__(self, p0: ServiceProvider) -> None: ...
    def bootstrap(self) -> None: ...
    def scheduleStart(self) -> None: ...
    @staticmethod
    def access$getServices$p(p0: "StartupService") -> ServiceProvider: ...


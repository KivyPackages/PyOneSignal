from typing import Any, ClassVar, overload

class IRebuildUserService:
    def getRebuildOperationsIfCurrentUser(self, p0: str, p1: str) -> list: ...


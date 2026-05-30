from typing import Any, ClassVar, overload
from core.internal.database.IDatabaseProvider import IDatabaseProvider

class RemoveInvalidSessionTimeRecords:
    INSTANCE: ClassVar["RemoveInvalidSessionTimeRecords"]
    def run(self, p0: IDatabaseProvider) -> None: ...


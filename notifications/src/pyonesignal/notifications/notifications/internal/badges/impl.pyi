from typing import Any, ClassVar, overload
from notifications.internal.data.INotificationQueryHelper import INotificationQueryHelper
from pyonesignal.core.internal.application.IApplicationService import IApplicationService
from pyonesignal.core.internal.database.IDatabaseProvider import IDatabaseProvider

class BadgeCountUpdater:
    def __init__(self, p0: IApplicationService, p1: INotificationQueryHelper, p2: IDatabaseProvider) -> None: ...
    def update(self) -> None: ...
    def updateCount(self, p0: int) -> None: ...


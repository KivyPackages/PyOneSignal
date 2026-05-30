from typing import Any, ClassVar, overload
from core.internal.config.ConfigModelStore import ConfigModelStore
from user.internal.identity.IdentityModelStore import IdentityModelStore
from user.internal.properties.PropertiesModelStore import PropertiesModelStore
from user.internal.subscriptions.SubscriptionModelStore import SubscriptionModelStore

class RebuildUserService:
    def __init__(self, p0: IdentityModelStore, p1: PropertiesModelStore, p2: SubscriptionModelStore, p3: ConfigModelStore) -> None: ...
    def getRebuildOperationsIfCurrentUser(self, p0: str, p1: str) -> list: ...


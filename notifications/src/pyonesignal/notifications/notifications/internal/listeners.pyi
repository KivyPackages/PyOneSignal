from typing import Any, ClassVar, overload
from notifications.internal.channels.INotificationChannelManager import INotificationChannelManager
from notifications.internal.pushtoken.IPushTokenManager import IPushTokenManager
from pyonesignal.core.internal.config.ConfigModel import ConfigModel
from pyonesignal.core.internal.config.ConfigModelStore import ConfigModelStore
from pyonesignal.core.modeling.Model import Model
from pyonesignal.core.modeling.ModelChangedArgs import ModelChangedArgs

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class INotificationsManager:
    """Forward declaration for ``com.onesignal.notifications.INotificationsManager``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.notifications.INotificationsManager')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...
class ISubscriptionManager:
    """Forward declaration for ``com.onesignal.user.internal.subscriptions.ISubscriptionManager``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.user.internal.subscriptions.ISubscriptionManager')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...
class ISubscription:
    """Forward declaration for ``com.onesignal.user.subscriptions.ISubscription``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.user.subscriptions.ISubscription')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class DeviceRegistrationListener:
    def __init__(self, p0: ConfigModelStore, p1: INotificationChannelManager, p2: IPushTokenManager, p3: INotificationsManager, p4: ISubscriptionManager) -> None: ...
    def start(self) -> None: ...
    def onModelUpdated(self, p0: ModelChangedArgs, p1: str) -> None: ...
    def onNotificationPermissionChange(self, p0: bool) -> None: ...
    @staticmethod
    def access$get_pushTokenManager$p(p0: "DeviceRegistrationListener") -> IPushTokenManager: ...
    @overload
    def onModelReplaced(self, p0: Model, p1: str) -> None: ...
    @overload
    def onModelReplaced(self, p0: ConfigModel, p1: str) -> None: ...
    def onSubscriptionRemoved(self, p0: ISubscription) -> None: ...
    def onSubscriptionAdded(self, p0: ISubscription) -> None: ...
    def onSubscriptionChanged(self, p0: ISubscription, p1: ModelChangedArgs) -> None: ...
    @staticmethod
    def access$get_notificationsManager$p(p0: "DeviceRegistrationListener") -> INotificationsManager: ...
    @staticmethod
    def access$get_subscriptionManager$p(p0: "DeviceRegistrationListener") -> ISubscriptionManager: ...


from typing import Any, ClassVar, overload
from internal.Trigger import Trigger
from internal.state.InAppStateService import InAppStateService
from internal.triggers.ITriggerHandler import ITriggerHandler
from pyonesignal.core.events.EventProducer import EventProducer
from pyonesignal.core.internal.time.ITime import ITime

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class ISessionService:
    """Forward declaration for ``com.onesignal.session.internal.session.ISessionService``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.session.internal.session.ISessionService')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
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

class DynamicTriggerController:
    Companion: ClassVar[Any]
    def __init__(self, p0: InAppStateService, p1: ISessionService, p2: ITime) -> None: ...
    def dynamicTriggerShouldFire(self, p0: Trigger) -> bool: ...
    def getEvents(self) -> EventProducer: ...
    @staticmethod
    def access$getScheduledMessages$p(p0: "DynamicTriggerController") -> list: ...
    @overload
    def subscribe(self, p0: ITriggerHandler) -> None: ...
    @overload
    def subscribe(self, p0: Any) -> None: ...
    @overload
    def unsubscribe(self, p0: Any) -> None: ...
    @overload
    def unsubscribe(self, p0: ITriggerHandler) -> None: ...
    def getHasSubscribers(self) -> bool: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

    class WhenMappings:
        $EnumSwitchMapping$0: ClassVar[Any]
        $EnumSwitchMapping$1: ClassVar[Any]

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class TimerTask:
    """Forward declaration for ``java.util.TimerTask``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.util.TimerTask')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/util/TimerTask.html
    """
    ...

class DynamicTriggerTimer:
    INSTANCE: ClassVar["DynamicTriggerTimer"]
    def scheduleTrigger(self, p0: TimerTask, p1: str, p2: int) -> None: ...

from typing import Any, ClassVar, overload
from internal.InAppMessage import InAppMessage
from internal.triggers.ITriggerHandler import ITriggerHandler
from internal.triggers.TriggerModel import TriggerModel
from internal.triggers.TriggerModelStore import TriggerModelStore
from internal.triggers.impl.DynamicTriggerController import DynamicTriggerController
from pyonesignal.core.modeling.Model import Model
from pyonesignal.core.modeling.ModelChangedArgs import ModelChangedArgs

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class ConcurrentHashMap:
    """Forward declaration for ``java.util.concurrent.ConcurrentHashMap``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.util.concurrent.ConcurrentHashMap')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentHashMap.html
    """
    ...

class TriggerController:
    def __init__(self, p0: TriggerModelStore, p1: DynamicTriggerController) -> None: ...
    @overload
    def onModelAdded(self, p0: Model, p1: str) -> None: ...
    @overload
    def onModelAdded(self, p0: TriggerModel, p1: str) -> None: ...
    @overload
    def onModelRemoved(self, p0: TriggerModel, p1: str) -> None: ...
    @overload
    def onModelRemoved(self, p0: Model, p1: str) -> None: ...
    def getTriggers(self) -> ConcurrentHashMap: ...
    @overload
    def subscribe(self, p0: ITriggerHandler) -> None: ...
    @overload
    def subscribe(self, p0: Any) -> None: ...
    @overload
    def unsubscribe(self, p0: Any) -> None: ...
    @overload
    def unsubscribe(self, p0: ITriggerHandler) -> None: ...
    def onModelUpdated(self, p0: ModelChangedArgs, p1: str) -> None: ...
    def isTriggerOnMessage(self, p0: InAppMessage, p1: list) -> bool: ...
    def evaluateMessageTriggers(self, p0: InAppMessage) -> bool: ...
    def messageHasOnlyDynamicTriggers(self, p0: InAppMessage) -> bool: ...
    def getHasSubscribers(self) -> bool: ...

    class WhenMappings:
        $EnumSwitchMapping$0: ClassVar[Any]


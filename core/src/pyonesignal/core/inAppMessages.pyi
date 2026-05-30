from typing import Any, ClassVar, overload

class IInAppMessage:
    def getMessageId(self) -> str: ...

from typing import Any, ClassVar, overload
from inAppMessages.IInAppMessage import IInAppMessage
from inAppMessages.IInAppMessageClickResult import IInAppMessageClickResult

class IInAppMessageClickEvent:
    def getMessage(self) -> IInAppMessage: ...
    def getResult(self) -> IInAppMessageClickResult: ...

from typing import Any, ClassVar, overload
from inAppMessages.IInAppMessageClickEvent import IInAppMessageClickEvent

class IInAppMessageClickListener:
    def onClick(self, p0: IInAppMessageClickEvent) -> None: ...

from typing import Any, ClassVar, overload
from inAppMessages.InAppMessageActionUrlType import InAppMessageActionUrlType

class IInAppMessageClickResult:
    def getUrl(self) -> str: ...
    def getActionId(self) -> str: ...
    def getUrlTarget(self) -> InAppMessageActionUrlType: ...
    def getClosingMessage(self) -> bool: ...

from typing import Any, ClassVar, overload
from inAppMessages.IInAppMessage import IInAppMessage

class IInAppMessageDidDismissEvent:
    def getMessage(self) -> IInAppMessage: ...

from typing import Any, ClassVar, overload
from inAppMessages.IInAppMessage import IInAppMessage

class IInAppMessageDidDisplayEvent:
    def getMessage(self) -> IInAppMessage: ...

from typing import Any, ClassVar, overload
from inAppMessages.IInAppMessageDidDismissEvent import IInAppMessageDidDismissEvent
from inAppMessages.IInAppMessageDidDisplayEvent import IInAppMessageDidDisplayEvent
from inAppMessages.IInAppMessageWillDismissEvent import IInAppMessageWillDismissEvent
from inAppMessages.IInAppMessageWillDisplayEvent import IInAppMessageWillDisplayEvent

class IInAppMessageLifecycleListener:
    def onWillDisplay(self, p0: IInAppMessageWillDisplayEvent) -> None: ...
    def onDidDisplay(self, p0: IInAppMessageDidDisplayEvent) -> None: ...
    def onWillDismiss(self, p0: IInAppMessageWillDismissEvent) -> None: ...
    def onDidDismiss(self, p0: IInAppMessageDidDismissEvent) -> None: ...

from typing import Any, ClassVar, overload
from inAppMessages.IInAppMessage import IInAppMessage

class IInAppMessageWillDismissEvent:
    def getMessage(self) -> IInAppMessage: ...

from typing import Any, ClassVar, overload
from inAppMessages.IInAppMessage import IInAppMessage

class IInAppMessageWillDisplayEvent:
    def getMessage(self) -> IInAppMessage: ...

from typing import Any, ClassVar, overload
from inAppMessages.IInAppMessageClickListener import IInAppMessageClickListener
from inAppMessages.IInAppMessageLifecycleListener import IInAppMessageLifecycleListener

class IInAppMessagesManager:
    def removeLifecycleListener(self, p0: IInAppMessageLifecycleListener) -> None: ...
    def getPaused(self) -> bool: ...
    def setPaused(self, p0: bool) -> None: ...
    def addTrigger(self, p0: str, p1: str) -> None: ...
    def addTriggers(self, p0: dict) -> None: ...
    def removeTrigger(self, p0: str) -> None: ...
    def removeTriggers(self, p0: list) -> None: ...
    def clearTriggers(self) -> None: ...
    def addLifecycleListener(self, p0: IInAppMessageLifecycleListener) -> None: ...
    def addClickListener(self, p0: IInAppMessageClickListener) -> None: ...
    def removeClickListener(self, p0: IInAppMessageClickListener) -> None: ...

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class EnumEntries:
    """Forward declaration for ``kotlin.enums.EnumEntries``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.enums.EnumEntries')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/enums/EnumEntries/
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

class InAppMessageActionUrlType:
    IN_APP_WEBVIEW: ClassVar["InAppMessageActionUrlType"]
    BROWSER: ClassVar["InAppMessageActionUrlType"]
    REPLACE_CONTENT: ClassVar["InAppMessageActionUrlType"]
    Companion: ClassVar[Any]
    IN_APP_WEBVIEW: ClassVar["InAppMessageActionUrlType"]
    BROWSER: ClassVar["InAppMessageActionUrlType"]
    REPLACE_CONTENT: ClassVar["InAppMessageActionUrlType"]
    def toString(self) -> str: ...
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "InAppMessageActionUrlType": ...
    @staticmethod
    def getEntries() -> EnumEntries: ...
    @staticmethod
    def access$getText$p(p0: "InAppMessageActionUrlType") -> str: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...
        def fromString(self, p0: str) -> "InAppMessageActionUrlType": ...


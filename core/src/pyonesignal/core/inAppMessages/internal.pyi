from typing import Any, ClassVar, overload
from inAppMessages.IInAppMessageClickListener import IInAppMessageClickListener
from inAppMessages.IInAppMessageLifecycleListener import IInAppMessageLifecycleListener

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Void:
    """Forward declaration for ``java.lang.Void``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.Void')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html
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
class Exception:
    """Forward declaration for ``java.lang.Exception``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.Exception')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/Exception.html
    """
    ...

class MisconfiguredIAMManager:
    Companion: ClassVar[Any]
    def __init__(self) -> None: ...
    @overload
    def addClickListener(self, p0: IInAppMessageClickListener) -> None: ...
    @overload
    def addClickListener(self, p0: IInAppMessageClickListener) -> Void: ...
    @overload
    def removeClickListener(self, p0: IInAppMessageClickListener) -> None: ...
    @overload
    def removeClickListener(self, p0: IInAppMessageClickListener) -> Void: ...
    @overload
    def removeLifecycleListener(self, p0: IInAppMessageLifecycleListener) -> Void: ...
    @overload
    def removeLifecycleListener(self, p0: IInAppMessageLifecycleListener) -> None: ...
    def getPaused(self) -> bool: ...
    def setPaused(self, p0: bool) -> None: ...
    @overload
    def addTrigger(self, p0: str, p1: str) -> Void: ...
    @overload
    def addTrigger(self, p0: str, p1: str) -> None: ...
    @overload
    def addTriggers(self, p0: dict) -> Void: ...
    @overload
    def addTriggers(self, p0: dict) -> None: ...
    @overload
    def removeTrigger(self, p0: str) -> None: ...
    @overload
    def removeTrigger(self, p0: str) -> Void: ...
    @overload
    def removeTriggers(self, p0: list) -> None: ...
    @overload
    def removeTriggers(self, p0: list) -> Void: ...
    @overload
    def clearTriggers(self) -> Void: ...
    @overload
    def clearTriggers(self) -> None: ...
    @overload
    def addLifecycleListener(self, p0: IInAppMessageLifecycleListener) -> Void: ...
    @overload
    def addLifecycleListener(self, p0: IInAppMessageLifecycleListener) -> None: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...
        @staticmethod
        def access$getEXCEPTION(p0: Any) -> Exception: ...


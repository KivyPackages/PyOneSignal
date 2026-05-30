from typing import Any, ClassVar, overload

class IEmailSubscription:
    def getEmail(self) -> str: ...

from typing import Any, ClassVar, overload
from user.subscriptions.IPushSubscriptionObserver import IPushSubscriptionObserver

class IPushSubscription:
    def getOptedIn(self) -> bool: ...
    def addObserver(self, p0: IPushSubscriptionObserver) -> None: ...
    def removeObserver(self, p0: IPushSubscriptionObserver) -> None: ...
    def optOut(self) -> None: ...
    def optIn(self) -> None: ...
    def getToken(self) -> str: ...

from typing import Any, ClassVar, overload
from user.subscriptions.PushSubscriptionChangedState import PushSubscriptionChangedState

class IPushSubscriptionObserver:
    def onPushSubscriptionChange(self, p0: PushSubscriptionChangedState) -> None: ...

from typing import Any, ClassVar, overload

class ISmsSubscription:
    def getNumber(self) -> str: ...

from typing import Any, ClassVar, overload

class ISubscription:
    def getId(self) -> str: ...

from typing import Any, ClassVar, overload
from user.subscriptions.PushSubscriptionState import PushSubscriptionState

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class JSONObject:
    """Forward declaration for ``org.json.JSONObject``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONObject')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class PushSubscriptionChangedState:
    def __init__(self, p0: PushSubscriptionState, p1: PushSubscriptionState) -> None: ...
    def getCurrent(self) -> PushSubscriptionState: ...
    def toJSONObject(self) -> JSONObject: ...
    def getPrevious(self) -> PushSubscriptionState: ...

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class JSONObject:
    """Forward declaration for ``org.json.JSONObject``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONObject')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class PushSubscriptionState:
    def __init__(self, p0: str, p1: str, p2: bool) -> None: ...
    def getOptedIn(self) -> bool: ...
    def getId(self) -> str: ...
    def toJSONObject(self) -> JSONObject: ...
    def getToken(self) -> str: ...


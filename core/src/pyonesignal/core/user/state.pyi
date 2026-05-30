from typing import Any, ClassVar, overload
from user.state.UserChangedState import UserChangedState

class IUserStateObserver:
    def onUserStateChange(self, p0: UserChangedState) -> None: ...

from typing import Any, ClassVar, overload
from user.state.UserState import UserState

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

class UserChangedState:
    def __init__(self, p0: UserState) -> None: ...
    def toJSONObject(self) -> JSONObject: ...
    def getCurrent(self) -> UserState: ...

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

class UserState:
    def __init__(self, p0: str, p1: str) -> None: ...
    def toJSONObject(self) -> JSONObject: ...
    def getOnesignalId(self) -> str: ...
    def getExternalId(self) -> str: ...


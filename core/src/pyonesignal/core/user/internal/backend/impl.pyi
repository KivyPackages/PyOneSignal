from typing import Any, ClassVar, overload
from core.internal.http.IHttpClient import IHttpClient

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Continuation:
    """Forward declaration for ``kotlin.coroutines.Continuation``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.coroutines.Continuation')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/coroutines/Continuation/
    """
    ...

class IdentityBackendService:
    def __init__(self, p0: IHttpClient) -> None: ...
    def deleteAlias(self, p0: str, p1: str, p2: str, p3: str, p4: str, p5: Continuation) -> Any: ...
    def setAlias(self, p0: str, p1: str, p2: str, p3: dict, p4: str, p5: Continuation) -> Any: ...

from typing import Any, ClassVar, overload
from user.internal.backend.CreateUserResponse import CreateUserResponse
from user.internal.backend.PropertiesDeltasObject import PropertiesDeltasObject
from user.internal.backend.PropertiesObject import PropertiesObject
from user.internal.backend.SubscriptionObject import SubscriptionObject

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
class JSONArray:
    """Forward declaration for ``org.json.JSONArray``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONArray')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class JSONConverter:
    INSTANCE: ClassVar["JSONConverter"]
    def convertToCreateUserResponse(self, p0: JSONObject) -> CreateUserResponse: ...
    @overload
    def convertToJSON(self, p0: list) -> JSONArray: ...
    @overload
    def convertToJSON(self, p0: SubscriptionObject) -> JSONObject: ...
    @overload
    def convertToJSON(self, p0: PropertiesObject) -> JSONObject: ...
    @overload
    def convertToJSON(self, p0: PropertiesDeltasObject) -> JSONObject: ...

from typing import Any, ClassVar, overload
from core.internal.http.IHttpClient import IHttpClient
from user.internal.backend.SubscriptionObject import SubscriptionObject

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Continuation:
    """Forward declaration for ``kotlin.coroutines.Continuation``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.coroutines.Continuation')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/coroutines/Continuation/
    """
    ...

class SubscriptionBackendService:
    def __init__(self, p0: IHttpClient) -> None: ...
    def deleteSubscription(self, p0: str, p1: str, p2: str, p3: Continuation) -> Any: ...
    def updateSubscription(self, p0: str, p1: str, p2: SubscriptionObject, p3: str, p4: Continuation) -> Any: ...
    def createSubscription(self, p0: str, p1: str, p2: str, p3: SubscriptionObject, p4: str, p5: Continuation) -> Any: ...
    def getIdentityFromSubscription(self, p0: str, p1: str, p2: Continuation) -> Any: ...
    def transferSubscription(self, p0: str, p1: str, p2: str, p3: str, p4: str, p5: Continuation) -> Any: ...

from typing import Any, ClassVar, overload
from core.internal.http.IHttpClient import IHttpClient
from user.internal.backend.PropertiesDeltasObject import PropertiesDeltasObject
from user.internal.backend.PropertiesObject import PropertiesObject

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Continuation:
    """Forward declaration for ``kotlin.coroutines.Continuation``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.coroutines.Continuation')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/coroutines/Continuation/
    """
    ...

class UserBackendService:
    def __init__(self, p0: IHttpClient) -> None: ...
    def getUser(self, p0: str, p1: str, p2: str, p3: str, p4: Continuation) -> Any: ...
    def createUser(self, p0: str, p1: dict, p2: list, p3: dict, p4: str, p5: Continuation) -> Any: ...
    def updateUser(self, p0: str, p1: str, p2: str, p3: PropertiesObject, p4: bool, p5: PropertiesDeltasObject, p6: str, p7: Continuation) -> Any: ...


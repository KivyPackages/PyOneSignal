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

class IamFetchRywTokenKey:
    USER: ClassVar["IamFetchRywTokenKey"]
    SUBSCRIPTION: ClassVar["IamFetchRywTokenKey"]
    USER: ClassVar["IamFetchRywTokenKey"]
    SUBSCRIPTION: ClassVar["IamFetchRywTokenKey"]
    @staticmethod
    def getEntries() -> EnumEntries: ...
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "IamFetchRywTokenKey": ...


from typing import Any, ClassVar, overload

class AnrConstants:
    INSTANCE: ClassVar["AnrConstants"]
    DEFAULT_ANR_THRESHOLD_MS: ClassVar[int]
    DEFAULT_CHECK_INTERVAL_MS: ClassVar[int]

from typing import Any, ClassVar, overload
from android.content.Context import Context

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class IOtelLogger:
    """Forward declaration for ``com.onesignal.otel.IOtelLogger``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.otel.IOtelLogger')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...
class Function0:
    """Forward declaration for ``kotlin.jvm.functions.Function0``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.functions.Function0')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/functions/Function0/
    """
    ...
class IOtelCrashHandler:
    """Forward declaration for ``com.onesignal.otel.IOtelCrashHandler``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.otel.IOtelCrashHandler')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class OneSignalCrashHandlerFactory:
    INSTANCE: ClassVar["OneSignalCrashHandlerFactory"]
    def createCrashHandler(self, p0: Context, p1: IOtelLogger, p2: Function0) -> IOtelCrashHandler: ...

from typing import Any, ClassVar, overload
from core.internal.application.IApplicationService import IApplicationService
from core.internal.features.IFeatureManager import IFeatureManager

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class OtelCrashUploader:
    """Forward declaration for ``com.onesignal.otel.crash.OtelCrashUploader``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.otel.crash.OtelCrashUploader')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class OneSignalCrashUploaderWrapper:
    def __init__(self, p0: IApplicationService, p1: IFeatureManager) -> None: ...
    def start(self) -> None: ...
    @staticmethod
    def access$getFeatureManager$p(p0: "OneSignalCrashUploaderWrapper") -> IFeatureManager: ...
    @staticmethod
    def access$getUploader(p0: "OneSignalCrashUploaderWrapper") -> OtelCrashUploader: ...
    @staticmethod
    def access$getApplicationService$p(p0: "OneSignalCrashUploaderWrapper") -> IApplicationService: ...

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class IOtelOpenTelemetryCrash:
    """Forward declaration for ``com.onesignal.otel.IOtelOpenTelemetryCrash``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.otel.IOtelOpenTelemetryCrash')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...
class IOtelLogger:
    """Forward declaration for ``com.onesignal.otel.IOtelLogger``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.otel.IOtelLogger')`` proxy; this empty class exists
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
class IOtelCrashReporter:
    """Forward declaration for ``com.onesignal.otel.IOtelCrashReporter``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.otel.IOtelCrashReporter')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class OtelAnrDetector:
    Companion: ClassVar[Any]
    @overload
    def __init__(self, p0: IOtelOpenTelemetryCrash, p1: IOtelLogger, p2: int, p3: int) -> None: ...
    @overload
    def __init__(self, p0: IOtelOpenTelemetryCrash, p1: IOtelLogger, p2: int, p3: int, p4: int, p5: DefaultConstructorMarker) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    @staticmethod
    def access$getCrashReporter$p(p0: "OtelAnrDetector") -> IOtelCrashReporter: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class IOtelPlatformProvider:
    """Forward declaration for ``com.onesignal.otel.IOtelPlatformProvider``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.otel.IOtelPlatformProvider')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...
class IOtelLogger:
    """Forward declaration for ``com.onesignal.otel.IOtelLogger``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.otel.IOtelLogger')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...
class IOtelAnrDetector:
    """Forward declaration for ``com.onesignal.otel.crash.IOtelAnrDetector``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.otel.crash.IOtelAnrDetector')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class OtelAnrDetectorKt:
    @staticmethod
    def createAnrDetector(p0: IOtelPlatformProvider, p1: IOtelLogger, p2: int, p3: int) -> IOtelAnrDetector: ...
    @staticmethod
    def createAnrDetector$default(p0: IOtelPlatformProvider, p1: IOtelLogger, p2: int, p3: int, p4: int, p5: Any) -> IOtelAnrDetector: ...

from typing import Any, ClassVar, overload

class OtelSdkSupport:
    INSTANCE: ClassVar["OtelSdkSupport"]
    MIN_SDK_VERSION: ClassVar[int]
    def reset(self) -> None: ...
    def isSupported(self) -> bool: ...
    def setSupported$com_onesignal_core(self, p0: bool) -> None: ...


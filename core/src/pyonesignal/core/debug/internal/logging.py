from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class Logging(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/debug/internal/logging/Logging"
    INSTANCE = JavaStaticField("Lcom/onesignal/debug/internal/logging/Logging;")
    getVisualLogLevel = JavaStaticMethod("()Lcom/onesignal/debug/LogLevel;")
    addListener = JavaMethod("(Lcom/onesignal/debug/ILogListener;)V")
    setVisualLogLevel = JavaStaticMethod("(Lcom/onesignal/debug/LogLevel;)V")
    removeListener = JavaMethod("(Lcom/onesignal/debug/ILogListener;)V")
    getLogLevel = JavaStaticMethod("()Lcom/onesignal/debug/LogLevel;")
    setLogLevel = JavaStaticMethod("(Lcom/onesignal/debug/LogLevel;)V")
    error = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/Throwable;)V")
    log = JavaMultipleMethod([("(Lcom/onesignal/debug/LogLevel;Ljava/lang/String;)V", True, False), ("(Lcom/onesignal/debug/LogLevel;Ljava/lang/String;Ljava/lang/Throwable;)V", True, False)])
    info = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/Throwable;)V")
    debug = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/Throwable;)V")
    error$default = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/Throwable;ILjava/lang/Object;)V")
    info$default = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/Throwable;ILjava/lang/Object;)V")
    verbose = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/Throwable;)V")
    debug$default = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/Throwable;ILjava/lang/Object;)V")
    atLogLevel = JavaStaticMethod("(Lcom/onesignal/debug/LogLevel;)Z")
    fatal = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/Throwable;)V")
    getApplicationService = JavaMethod("()Lcom/onesignal/core/internal/application/IApplicationService;")
    setApplicationService = JavaMethod("(Lcom/onesignal/core/internal/application/IApplicationService;)V")
    setOtelTelemetry = JavaMethod("(Lcom/onesignal/otel/IOtelOpenTelemetryRemote;Lkotlin/jvm/functions/Function1;)V")
    setOtelTelemetry$default = JavaStaticMethod("(Lcom/onesignal/debug/internal/logging/Logging;Lcom/onesignal/otel/IOtelOpenTelemetryRemote;Lkotlin/jvm/functions/Function1;ILjava/lang/Object;)V")
    getLogLevel$annotations = JavaStaticMethod("()V")
    getVisualLogLevel$annotations = JavaStaticMethod("()V")
    fatal$default = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/Throwable;ILjava/lang/Object;)V")
    verbose$default = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/Throwable;ILjava/lang/Object;)V")
    warn$default = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/Throwable;ILjava/lang/Object;)V")
    warn = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/Throwable;)V")

    class WhenMappings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/debug/internal/logging/Logging$WhenMappings"
        $EnumSwitchMapping$0 = JavaStaticField("[I")
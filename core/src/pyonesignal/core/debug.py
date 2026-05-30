from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IDebugManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/debug/IDebugManager"
    getLogLevel = JavaMethod("()Lcom/onesignal/debug/LogLevel;")
    setLogLevel = JavaMethod("(Lcom/onesignal/debug/LogLevel;)V")
    getAlertLevel = JavaMethod("()Lcom/onesignal/debug/LogLevel;")
    setAlertLevel = JavaMethod("(Lcom/onesignal/debug/LogLevel;)V")
    addLogListener = JavaMethod("(Lcom/onesignal/debug/ILogListener;)V")
    removeLogListener = JavaMethod("(Lcom/onesignal/debug/ILogListener;)V")

class ILogListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/debug/ILogListener"
    onLogEvent = JavaMethod("(Lcom/onesignal/debug/OneSignalLogEvent;)V")

class LogLevel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/debug/LogLevel"
    Companion = JavaStaticField("Lcom/onesignal/debug/LogLevel$Companion;")
    NONE = JavaStaticField("Lcom/onesignal/debug/LogLevel;")
    FATAL = JavaStaticField("Lcom/onesignal/debug/LogLevel;")
    ERROR = JavaStaticField("Lcom/onesignal/debug/LogLevel;")
    WARN = JavaStaticField("Lcom/onesignal/debug/LogLevel;")
    INFO = JavaStaticField("Lcom/onesignal/debug/LogLevel;")
    DEBUG = JavaStaticField("Lcom/onesignal/debug/LogLevel;")
    VERBOSE = JavaStaticField("Lcom/onesignal/debug/LogLevel;")
    values = JavaStaticMethod("()[Lcom/onesignal/debug/LogLevel;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/debug/LogLevel;")
    fromInt = JavaStaticMethod("(I)Lcom/onesignal/debug/LogLevel;")
    getEntries = JavaStaticMethod("()Lkotlin/enums/EnumEntries;")
    fromString = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/debug/LogLevel;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/debug/LogLevel$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        fromInt = JavaMethod("(I)Lcom/onesignal/debug/LogLevel;")
        fromString = JavaMethod("(Ljava/lang/String;)Lcom/onesignal/debug/LogLevel;")
    NONE = JavaStaticField("Lcom/onesignal/debug/LogLevel;")
    FATAL = JavaStaticField("Lcom/onesignal/debug/LogLevel;")
    ERROR = JavaStaticField("Lcom/onesignal/debug/LogLevel;")
    WARN = JavaStaticField("Lcom/onesignal/debug/LogLevel;")
    INFO = JavaStaticField("Lcom/onesignal/debug/LogLevel;")
    DEBUG = JavaStaticField("Lcom/onesignal/debug/LogLevel;")
    VERBOSE = JavaStaticField("Lcom/onesignal/debug/LogLevel;")

class OneSignalLogEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/debug/OneSignalLogEvent"
    __javaconstructor__ = [("(Lcom/onesignal/debug/LogLevel;Ljava/lang/String;)V", False)]
    copy$default = JavaStaticMethod("(Lcom/onesignal/debug/OneSignalLogEvent;Lcom/onesignal/debug/LogLevel;Ljava/lang/String;ILjava/lang/Object;)Lcom/onesignal/debug/OneSignalLogEvent;")
    getEntry = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    copy = JavaMethod("(Lcom/onesignal/debug/LogLevel;Ljava/lang/String;)Lcom/onesignal/debug/OneSignalLogEvent;")
    component1 = JavaMethod("()Lcom/onesignal/debug/LogLevel;")
    component2 = JavaMethod("()Ljava/lang/String;")
    getLevel = JavaMethod("()Lcom/onesignal/debug/LogLevel;")
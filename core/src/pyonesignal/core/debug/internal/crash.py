from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class AnrConstants(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/debug/internal/crash/AnrConstants"
    INSTANCE = JavaStaticField("Lcom/onesignal/debug/internal/crash/AnrConstants;")
    DEFAULT_ANR_THRESHOLD_MS = JavaStaticField("J")
    DEFAULT_CHECK_INTERVAL_MS = JavaStaticField("J")

class OneSignalCrashHandlerFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/debug/internal/crash/OneSignalCrashHandlerFactory"
    INSTANCE = JavaStaticField("Lcom/onesignal/debug/internal/crash/OneSignalCrashHandlerFactory;")
    createCrashHandler = JavaMethod("(Landroid/content/Context;Lcom/onesignal/otel/IOtelLogger;Lkotlin/jvm/functions/Function0;)Lcom/onesignal/otel/IOtelCrashHandler;")

class OneSignalCrashUploaderWrapper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/debug/internal/crash/OneSignalCrashUploaderWrapper"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/core/internal/features/IFeatureManager;)V", False)]
    start = JavaMethod("()V")
    access$getFeatureManager$p = JavaStaticMethod("(Lcom/onesignal/debug/internal/crash/OneSignalCrashUploaderWrapper;)Lcom/onesignal/core/internal/features/IFeatureManager;")
    access$getUploader = JavaStaticMethod("(Lcom/onesignal/debug/internal/crash/OneSignalCrashUploaderWrapper;)Lcom/onesignal/otel/crash/OtelCrashUploader;")
    access$getApplicationService$p = JavaStaticMethod("(Lcom/onesignal/debug/internal/crash/OneSignalCrashUploaderWrapper;)Lcom/onesignal/core/internal/application/IApplicationService;")

class OtelAnrDetector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/debug/internal/crash/OtelAnrDetector"
    __javaconstructor__ = [("(Lcom/onesignal/otel/IOtelOpenTelemetryCrash;Lcom/onesignal/otel/IOtelLogger;JJ)V", False), ("(Lcom/onesignal/otel/IOtelOpenTelemetryCrash;Lcom/onesignal/otel/IOtelLogger;JJILkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/debug/internal/crash/OtelAnrDetector$Companion;")
    start = JavaMethod("()V")
    stop = JavaMethod("()V")
    access$getCrashReporter$p = JavaStaticMethod("(Lcom/onesignal/debug/internal/crash/OtelAnrDetector;)Lcom/onesignal/otel/IOtelCrashReporter;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/debug/internal/crash/OtelAnrDetector$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

class OtelAnrDetectorKt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/debug/internal/crash/OtelAnrDetectorKt"
    createAnrDetector = JavaStaticMethod("(Lcom/onesignal/otel/IOtelPlatformProvider;Lcom/onesignal/otel/IOtelLogger;JJ)Lcom/onesignal/otel/crash/IOtelAnrDetector;")
    createAnrDetector$default = JavaStaticMethod("(Lcom/onesignal/otel/IOtelPlatformProvider;Lcom/onesignal/otel/IOtelLogger;JJILjava/lang/Object;)Lcom/onesignal/otel/crash/IOtelAnrDetector;")

class OtelSdkSupport(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/debug/internal/crash/OtelSdkSupport"
    INSTANCE = JavaStaticField("Lcom/onesignal/debug/internal/crash/OtelSdkSupport;")
    MIN_SDK_VERSION = JavaStaticField("I")
    reset = JavaMethod("()V")
    isSupported = JavaMethod("()Z")
    setSupported$com_onesignal_core = JavaMethod("(Z)V")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class FirebaseAnalyticsTracker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/analytics/impl/FirebaseAnalyticsTracker"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/core/internal/time/ITime;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/notifications/internal/analytics/impl/FirebaseAnalyticsTracker$Companion;")
    trackInfluenceOpenEvent = JavaMethod("()V")
    trackOpenedEvent = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    trackReceivedEvent = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    access$setFirebaseAnalyticsClass$cp = JavaStaticMethod("(Ljava/lang/Class;)V")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/analytics/impl/FirebaseAnalyticsTracker$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        access$getTrackMethod = JavaStaticMethod("(Lcom/onesignal/notifications/internal/analytics/impl/FirebaseAnalyticsTracker$Companion;Ljava/lang/Class;)Ljava/lang/reflect/Method;")
        access$getInstanceMethod = JavaStaticMethod("(Lcom/onesignal/notifications/internal/analytics/impl/FirebaseAnalyticsTracker$Companion;Ljava/lang/Class;)Ljava/lang/reflect/Method;")
        canTrack = JavaMethod("()Z")

class NoAnalyticsTracker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/analytics/impl/NoAnalyticsTracker"
    __javaconstructor__ = [("()V", False)]
    trackInfluenceOpenEvent = JavaMethod("()V")
    trackOpenedEvent = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    trackReceivedEvent = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")